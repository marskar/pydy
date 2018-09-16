import pandas
import pandas as pd
from pandas import DataFrame
import numpy as np
from pydy import pydy

pydy(add=['say_hi', 'say_moo'], cls='np.chararray')
pydy(add='say_hi', cls='pd.DataFrame')

np.chararray.say_hi()
np.chararray.say_moo()

pd.DataFrame.say_hi()
pandas.DataFrame.say_hi()
DataFrame.say_hi()
