# TODO: take **kwargs into account
from inspect import signature
import os, json
from .Channel import Channel, Channels

class Operation:    
    def __init__(self, func=None, args=[], name="", enabled=True):
        self.func = func
        self.args = args
        self.name = name
        self.output = None
        self.enabled = enabled

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
            arg = arguments[arg_id]
            if param.annotation is Channel and type(arg) is list:
                batch_size = max(batch_size, len(arg))
            if param.annotation is Channel and arg == None:
                return
        
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
                if param.annotation is Channel and arg == None:
                    return
                arg_id += 1
            self.output.append(self.func(*args_tmp))
    
    def __str__(self) -> str:
        return self.name
        

class Pipeline:
    def __init__(self):
        self.operations = []
        self.functions = []
    
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
            data = json.load(f)
        self.functions = functions
        operations = {}
        for op_json in data:
            op = Operation()
            op.name = op_json["name"]
            op.enabled = op_json["enabled"]
            op.func = self.functions[op_json["function"]]
            op.args = []
            for arg in op_json["args"]:
                if type(arg) is str and len(arg) > 0 and arg[0] == '%':
                    op.args.append(operations[arg[1:]])
                else:
                    op.args.append(arg)
                operations[op.name] = op
        self.operations = list(operations.values())
    
    def save(self, filepath: str):
        operations_json = []
        for op in self.operations:
            op_json = {}
            op_json["name"] = op.name
            op_json["enabled"] = op.enabled
            op_json["function"] = op.func.__name__
            op_json["args"] = []
            for arg in op.args:
                if type(arg) is Operation:
                    op_json["args"].append("%" + arg.name)
                elif type(arg) is list:
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
    
    