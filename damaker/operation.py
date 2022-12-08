from collections.abc import Iterable
from dataclasses import dataclass
from inspect import Signature, signature
from typing import Any, Callable, Type

from .dmktypes import *
from .imagestack import *

__operations__ = {}

@dataclass
class OperationInput:
    index: int = -1
    name: str = 'unkown'
    type: Type = None
    value: Any = None

class Operation:
    alias: str
    category: str
    func: Callable
    signature: Signature

    hints: dict[str, Any] = {}
    settings: list[OperationInput]
    _output: list[Any] = []

    def __init__(self, *args, **hints):
        if len(args) > 0 and type(args[0]) is str and args[0] in __operations__.keys():
            self.copyFrom(__operations__[args[0]])
        self.hints |= hints

    @property
    def kwargs(self) -> dict:
        return { input.name: input.value for input in self.settings }

    @property
    def output(self) -> Any:
        if len(self._output) == 0:
            raise OperationMissingOutputException()
        return self._output[-1]

    @property
    def description(self) -> str:
        return self.func.__doc__

    @method
    def resetSettings(self):
        self.settings = []
        param_id = 0
        for name in self.signature.parameters:
            param = self.signature.parameters[name]

            input = OperationInput()
            input.index = param_id
            input.type = param.annotation
            input.name = param.name
            input.value = param.default

            self.settings.append(input)
            param_id += 1

    @method
    def set(self, **kwargs) -> bool:
        for name, value in kwargs.items():
            input = self.findInput(name)
            if input == None:
                print(f'[Warning]: Unkown input argument: {name}')
                return False
            input.value = value
            return True
        return False

    @method
    def findInput(self, name: str) -> OperationInput:
        for input in self.settings:
            if input.name == name:
                return input
        return None

    def __call__(self, func) -> Any:
        self.func = func
        self.alias = self.hints.get('alias')
        self.category = self.hints.get('category')
        self.signature = signature(self.func)
        self.resetSettings()

        ndim_hint = self.hints.get('ndim')

        if self.alias == None:
            self.alias = self.func.__name__
        if self.category == None:
            self.category = 'Plugins'

        global __operations__
        __operations__[self.alias] = self

        def damaker_operation_wrapper(ndim_hint, func, alias):
            def damaker_operation(*args, **kwargs):
                print(f'>> Running: {alias}')
                if ndim_hint != None:
                    if issubclass(type(args[0]), ImageStack):
                        input: ImageStack = args[0]
                        if (isinstance(ndim_hint, Iterable) and input.ndim not in ndim_hint) and input.ndim != ndim_hint:
                            raise DimensionCountMismatchException()

                output = func(*args, **kwargs)
                self._output.append(output)
                return output
            return damaker_operation

        return damaker_operation_wrapper(ndim_hint, self.func, self.alias)

    def execute(self) -> Any:
        return self.func(**self.kwargs)

    @method
    def copy(self) -> Self:
        copied = Operation()
        copied.resetSettings()
        return copied

    @method
    def copyFrom(self, op: Self):
        self.func = op.func
        self.alias = op.alias
        self.category = op.category
        self.signature = op.signature
        self.resetSettings()

    def __str__(self) -> str:
        return self.alias

    def __iter__(self) -> iter:
        return iter(self.settings)
