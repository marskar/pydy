import pandas as pd
from pydy import pydy

PydyFrame = pydy(cls=pd.DataFrame, src='helper')

df = PydyFrame(data=pd.read_csv('risk_factors_cervical_cancer.csv'))

df.say_hi()
df.say_moo()
df.unused()

df.save()
df.say_hi()
