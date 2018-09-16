from typing import Iterable
from method import *
import __main__


def pydy(add: Iterable[str], cls: str = 'pd.DataFrame') -> None:

    def add_method(name, target=cls):
        main_target = '__main__.' + target
        try:
            if eval(main_target):
                    setattr(eval(main_target), name, eval(name))
        except AttributeError as e:
            print(e)

    if type(add) == str:
        add_method(add)
    elif type(add) in (list, tuple):
        any(map(add_method, add))
    else:
        print(f'The add argument was {type(names)}. '
              'It can only be a list/tuple of strings or a string')
