from importlib import import_module
import pickle


def pydy(cls, arg=None, src: str = 'helper'):

    class Pydy(cls):
        def save(self, filename='pydy.pickle'):
            with open(filename, 'wb') as f:
                # Pickle Pydy class using the highest protocol available.
                pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    mod = import_module(src)
    internals = mod.__dict__.items()
    method_names = [name for name, val in internals if callable(val)]

    # change this loop to map call?
    for name in method_names:
        met = getattr(mod, name)
        setattr(Pydy, name, met)

    if arg is not None:
        return Pydy(arg)
    else:
        return Pydy
