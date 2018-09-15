from typing import Iterable
from helper import *
import __main__


def pydy(names: Iterable[str]) -> None:

        try:
            if __main__.pd.DataFrame:
                for name in names:
                    setattr(__main__.pd.DataFrame, name, eval(name))
        except AttributeError:
            pass
        try:
            if __main__.pandas.DataFrame:
                for name in names:
                    setattr(__main__.pandas.DataFrame, name, eval(name))
        except AttributeError:
            pass
        try:
            if __main__.DataFrame:
                for name in names:
                    setattr(__main__.DataFrame, name, eval(name))
        except AttributeError:
            pass
