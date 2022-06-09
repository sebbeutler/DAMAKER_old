from inspect import signature
from lib2to3.pytree import type_repr
import os, json
import os.path
import re
from tokenize import Single
from .Channel import Channel, Channels, SingleChannel
from .utils import *
import enum

class Operation:    
    def __init__(self, func=None, args=[], name="", enabled=True):
        self.func = func
        self.args = args
        self.name = name
        self.output = None
        self.enabled = enabled
        self.type = Operation
        self.outputPath = ""

    def run(self):       
        arg_id = 0
        sign = signature(self.func)
        arguments = []
        
        for arg in self.args:
            if type(arg) is list:
                outputs = []                    
                for i in range(len(arg)):
                    if type(arg[i]) is Operation:
                        outputs.append(arg[i].output)
                    else:
                        outputs.append(arg[i])                
                arguments.append(outputs)
            elif type(arg) is Operation:
                arguments.append(arg.output)                    
            else:
                arguments.append(arg)    
                
        batch_size = 0     
        sign = signature(self.func)
        arg_id = 0
        for name in sign.parameters:
            param = sign.parameters[name]
            if arg_id < len(arguments):
                arg = arguments[arg_id]
            else:
                arg = param.default
            
            if param.annotation is Channel and type(arg) is list:
                batch_size = max(batch_size, len(arg))
            elif param.annotation is Channel and arg == None and param.default != None:
                return
            arg_id += 1
        
        if batch_size == 0:
            self.output = self.func(*arguments)
            return
        
        self.output = []
        for i in range(batch_size):
            arg_id = 0
            args_tmp = arguments.copy()
            for name in sign.parameters:
                param = sign.parameters[name]
                arg = arguments[arg_id]
                if param.annotation is Channel and type(arg) is list:
                    if i >= len(arg):
                        args_tmp[arg_id] = arguments[arg_id][-1]
                    else:
                        args_tmp[arg_id] = arguments[arg_id][i]
                if param.annotation is Channel and arg == None and param.default != None:
                    return
                arg_id += 1
                
            if sign.return_annotation is Channels:
                self.output += self.func(*args_tmp)
            else:
                self.output.append(self.func(*args_tmp))
    
    def __str__(self) -> str:
        return self.name

class BatchParameters:
    folder: str=""
    mods: list[str] = []
    file: str=""
    associated: bool=True
     
    output: list=[]
    fileList: list=[]
    fileListId: int=0
    
    type: type=Channel
    
    def load(self):
        self.fileList = []
        
        if self.file == "*":
            for file in os.listdir(self.folder):
                if os.path.isfile(self.folder + "/" + file):
                    self.fileList.append(file)
            print(f'batch files: {self.fileList}')
            return
        
        def applyMod(file, modId, mods):
            fileList = []
            for mod in mods[modId].split(";"):
                fileModded = re.sub('{(%d)}' % (modId+1), mod, file)
                if modId+1 >= len(mods):                    
                    if os.path.isfile(self.folder + "/" + fileModded):
                        fileList.append(fileModded)
                    else:
                        print("Batch file: '%s' not found" % fileModded)
                else:
                    applyMod(fileModded, modId+1, mods)
            if len(fileList) == 0:
                return
            if self.associated:
                self.fileList += fileList
            else:
                self.fileList.append(fileList)
        if len(self.mods) == 0:
            self.mods = [""]
        applyMod(self.file, 0, self.mods)
        
        self.fileListId = 0
                    
        print(f'batch files: {self.fileList}')
    
    def next(self):
        if self.type is Channel: 
            self.output = loadChannelsFromFile(self.folder + "/" + self.fileList[self.fileListId])
        elif self.type is Mesh:
            self.output = [Mesh(self.folder + "/" + self.fileList[self.fileListId])]
        elif self.type is Channels:
            self.output = []
            if self.associated:
                for file in self.fileList:
                    self.output += loadChannelsFromFile(self.folder + "/" + file)
                self.fileListId = len(self.fileList)
            else:
                for file in self.fileList[self.fileListId]:
                    self.output += loadChannelsFromFile(self.folder + "/" + file)
                self.fileListId += 1
        return self.output

    def all(self):
        chns = []
        while not self.finished():
            chns += self.next()
        return chns
        
    def finished(self):
        return self.fileListId >= len(self.fileList)

    def asDict(self):
        d = {"folder": self.folder, "file": self.file, "associated": self.associated}
        for i in range(len(self.mods)):
            d[i] = self.mods[i]
        return d

    def fromDict(self, d: dict):
        self.folder = d["folder"]
        self.file = d["file"]
        self.mods = [None] * (len(d)-2)
        self.associated = d["associated"]
        for key in d.keys():
            if type(key) is int:
                self.mods[key] = d[key]

class BatchOperation(Operation):
    def __init__(self, func=None, args=[], name="", enabled=True, outputPath=""):
        self.func = func
        self.args = args
        self.name = name
        self.enabled = enabled
        self.type = BatchOperation
        self.outputPath = outputPath
    
    def run(self):
        parameters: list[BatchParameters] = []
        
        argId = 0
        sign = signature(self.func)        
        arguments = []
        for name in sign.parameters:
            param = sign.parameters[name]
            if param.annotation in [Channel, Mesh] and type(self.args[argId]) is BatchParameters:
                self.args[argId].load()
                parameters.append(self.args[argId])
            
            if argId >= len(self.args):
                continue
            elif param.annotation is SingleChannel:
                arguments.append(loadChannelsFromFile(self.args[argId]))
            elif param.annotation is Channels and type(self.args[argId]) is BatchParameters:
                self.args[argId].load()
                self.args[argId].type = Channels
                if self.args[argId].associated:
                    arguments.append(self.args[argId].all())
                else:
                    arguments.append(self.args[argId])
                    parameters.append(self.args[argId])
            else:
                arguments.append(self.args[argId])
            argId += 1
        
        if len(parameters) == 0:
            outputs = self.func(*arguments)
            if self.outputPath != "":
                channelsSave(outputs, self.outputPath)
            return
    
        while not parameters[0].finished():
            for param in parameters:
                param.next()
        
            outputs = []
            if not parameters[0].associated:
                nb_channels = 1
            else:
                nb_channels = len(parameters[0].output)
            for i in range(nb_channels):   
                argId = 0
                batch_args = []         
                for name in sign.parameters:
                    param = sign.parameters[name]
                    if param.annotation is Channel and type(arguments[argId]) is BatchParameters:
                        batch_args.append(parameters[argId].output[i])
                    elif param.annotation is Channels and type(arguments[argId]) is BatchParameters:
                        batch_args.append(parameters[argId].output)
                    else:
                        if argId < len(arguments):
                            batch_args.append(arguments[argId])
                    argId += 1
                outputs.append(self.func(*batch_args))
            if self.outputPath != "" and sign.return_annotation in [Channel, Channels]:
                channelsSave(outputs, self.outputPath)
            elif self.outputPath != "" and sign.return_annotation is NamedArray:
                for out in outputs:
                    listSaveCSV(out, self.outputPath)
            
    
class Pipeline:
    def __init__(self):
        self.operations: list[Operation] = []
    
    def add(self, func, *args):
        op = Operation(func, args)
        self.operations.append(op)
        return op

    def addOperation(self, op):
        self.operations.append(op)
        return op
    
    def run(self):
        for op in self.operations:
            op.run()
    
    def load(self, filepath: str, functions: list):
        if not os.path.isfile(filepath):
            print(f'pipeline load: unkown file {filepath}')
            return
        with open(filepath, 'r') as f:
            data: dict = json.load(f)
        operations = {}
        for op_json in data:
            if "type" in op_json.keys():
                if op_json["type"] == "BatchOperation":
                    op = BatchOperation()
                elif op_json["type"] == "Operation":
                    op = Operation()
                else:
                    print("Unknown operation type while loading file: " + filepath)
            op.name = op_json["name"]
            op.enabled = op_json["enabled"]
            op.func = functions[op_json["function"]]
            op.outputPath = op_json["outputPath"]
            op.args = []
            for arg in op_json["args"]:
                if type(arg) is str and len(arg) > 0 and arg[0] == '%':
                    op.args.append(operations[arg[1:]])
                if type(arg) is dict:
                    param = BatchParameters()
                    param.fromDict(arg)
                    op.args.append(param)
                else:
                    op.args.append(arg)
                operations[op.name] = op
        self.operations = list(operations.values())
    
    def save(self, filepath: str):
        operations_json = []
        for op in self.operations:
            op_json = {}
            if op.type is BatchOperation:
                op_json["type"] = "BatchOperation"
            elif op.type is Operation:
                op_json["type"] = "Operation"
            else:
                print("Unknown operation type: " + str(op.type))
            op_json["name"] = op.name
            op_json["enabled"] = op.enabled
            op_json["function"] = op.func.__name__
            op_json["outputPath"] = op.outputPath
            op_json["args"] = []
            for arg in op.args:
                if type(arg) is Operation:
                    op_json["args"].append("%" + arg.name)
                elif type(arg) is BatchParameters:
                    op_json["args"].append(arg.asDict())
                elif type(arg) is type(enum.Enum.value):
                    print("enum", arg)
                elif type(arg) is list:
                    print("cannot save:", arg)
                    continue
                else:
                    op_json["args"].append(arg)
            operations_json.append(op_json)
        with open(filepath, 'w') as f:
            json.dump(operations_json, f)

if __name__ == '__main__':
    def addition(a, b):
        return a + b
    
    def print_list(l):
        for e in l:
            print(e)

    p = Pipeline()
    
    step1 = p.add(addition, 1, 2)
    step2 = p.add(addition, 5, 6)
    step3 = p.add(print_list, [step1, step2])
    
    p.run()
    
    