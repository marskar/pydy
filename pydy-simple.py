from typing import Iterable


def pydy(names: Iterable[str]) -> None:

        try:
            if pd.DataFrame:
                for name in names:
                    setattr(pd.DataFrame, name, eval(name))
        except AttributeError:
            pass
        try:
            if pandas.DataFrame:
                for name in names:
                    setattr(pandas.DataFrame, name, eval(name))
        except AttributeError:
            pass
        try:
            if DataFrame:
                for name in names:
                    setattr(DataFrame, name, eval(name))
        except AttributeError:
            pass
