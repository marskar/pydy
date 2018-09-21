from typing import Optional, Type
from importlib import import_module


def pydy(cls: str = None,
         arg: str = None,
         src: str = None) -> Optional[Type]:

    if cls is not None:
        class Pydy(cls):
            # add pickle method here to give option to save the class
            pass

    if src.endswith('.py'):
        src = src[:-3]
    mod = import_module(src)
    internals = mod.__dict__.items()
    method_names = [name for name, val in internals if callable(val)]

    for name in method_names:
        setattr(Pydy, name, eval(name))

    instance = Pydy(eval(arg))

    return instance
