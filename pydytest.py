import pandas
import pandas as pd
from pandas import DataFrame
from pydy import pydy

def say_hi():
    print("Hi!")

say_hi() # this should work

pydy(['say_hi']) # this will remove functions from global namespace

say_hi() # this will not work

pd.DataFrame.say_hi() # this should work
pandas.DataFrame.say_hi() # this should work
DataFrame.say_hi() # this should work
