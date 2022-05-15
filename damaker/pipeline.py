# TODO: take **kwargs into account
from inspect import signature

from .Channel import Channel, Channels

class Operation:    
    def __init__(self, func=None, args=[], name=""):
        self.func = func
        self.args = args
        self.name = name
        self.output = None

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
                batch_size = len(arg)
                break
        
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
                    args_tmp[arg_id] = arguments[arg_id][i]
            self.output.append(self.func(*args_tmp))
    
    def __str__(self) -> str:
        return self.name
        

class Pipeline:
    def __init__(self):
        self.operations = []
    
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
    
    