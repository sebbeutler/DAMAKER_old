
from processing import *
from utils import *

# TODO: take **kwargs into account

class Operation:    
    def __init__(self, func, args):
        self.func = func
        self.args = args
        self.output = None

    def run(self):
        arguments = [] 
        
        for arg in self.args:
            if type(arg) is Operation:
                arguments.append(arg.output)
            elif type(arg) is list:
                arg_as_list = []
                for i in range(len(arg)):
                    if type(arg[i]) is Operation:
                        arg_as_list.append(arg[i].output)
                    else:
                        arg_as_list.append(arg[i])                
                arguments.append(arg_as_list)
            else:
                arguments.append(arg)                
        
        self.output = self.func(*arguments)
        

class Pipeline:
    def __init__(self):
        self.operations = []
    
    def add(self, func, *args):
        op = Operation(func, args)
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
    
    