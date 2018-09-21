import pandas as pd
from pydy import pydy

# create new class
PydyFrame = pydy(cls=pd.DataFrame, src='helper')

# instantiate it
df = PydyFrame(data=pd.read_csv('risk_factors_cervical_cancer.csv'))

# test out methods added from helper file
df.say_hi()
df.say_moo()
