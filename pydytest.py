import pandas as pd
from pydy import pydy

df = (pydy(cls=pd.DataFrame,
           arg=pd.read_csv('risk_factors_cervical_cancer.csv'),
           src='helper.py')
    .dropna()
    .head()
 )

df.save()

np.chararray.say_hi()
np.chararray.say_moo()

pd.DataFrame.say_hi()
pandas.DataFrame.say_hi()
DataFrame.say_hi()
