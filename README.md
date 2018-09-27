# Pydy: Add user-defined methods to Python classes
## Pandas DataFrame example
```python
import pandas as pd
from pydy import pydy

# create a new class that inherits from pd.DataFrame
# and includes methods defined in a 'helper.py' file
PydyFrame = pydy(cls=pd.DataFrame, src='helper')

# instantiate the new class
df = PydyFrame(data=pd.read_csv('risk_factors_cervical_cancer.csv'))

# test methods added from helper file
df.say_hi()
df.say_moo()

# test method from parent class
df.head(n=1)

# confirm that df is an instance of pd.DataFrame and PydyFrame
isinstance(df, (pd.DataFrame, PydyFrame))

# confirm that PydyFrame is a subclass of pd.DataFrame
issubclass(PydyFrame, pd.DataFrame)
```