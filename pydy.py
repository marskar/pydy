from typing import Iterable
from helper import *
import __main__


def pydy(names: Iterable[str], target: str = 'pd.DataFrame') -> None:

    def add_method(name, targ=target):
        main_target = '__main__.' + targ
        try:
            if eval(main_target):
                    setattr(eval(main_target), name, eval(name))
        except AttributeError as e:
            print(e)

    any(map(add_method, names))

