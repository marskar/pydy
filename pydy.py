from importlib import import_module
import pickle
import os.path

if os.path.isfile('helper.py'):
    from helper import *


def pydy(cls, arg=None, src=None):

    class Pydy:#(cls):
        def save(self, filename='pydy.pickle'):
            with open(filename, 'wb') as f:
                # Pickle Pydy class using the highest protocol available.
                pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    if arg is not None:
        instance = Pydy(arg)
    else:
        instance = Pydy

    if src is not None:
        if src.endswith('.py'):
            src = src[:-3]
        mod = import_module(src)
        internals = mod.__dict__.items()
        method_names = [name for name, val in internals if callable(val)]

        for name in method_names:
            instance.name = name
    return instance
