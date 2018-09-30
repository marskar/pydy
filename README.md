# The `scattr` Python package

The `scattr` package has one function, `scattr`,
which creates a
**S**ub**C**lass with **ATTR**ibutes defined
in a user-defined helper script (`.py` files).

Subclasses are classes derived from pre-existing classes.

Attributes can be methods, classes, and variables,
but the `scattr` function only adds
callable objects(methods and classes), not variables.

The `scattr` function takes 
- a class object and
- the name of a helper script
and returns a subclass called `SubClassAttributes`
that contains the methods and classes
defined in the helper script.

Essentially, this is an easy way to
add user-defined functions and classes to classes.

Class variables, method and classes
can be added to pre-existing classes dynamically:
```python
import pandas as pd
import math
# add pi to a pandas DataFrame
pd.DataFrame.pi = math.pi
```

The `scattr` package provides a cleaner way to 
add new attributes, because
1. it creates a new subclass,
instead of modifying the original class, and
2. automatically adds all of the methods and classes
defined in a separate helper script,
rather than dynamically add each one after
defining everything in a single script or importing
functions and classes from a module.

## Pandas DataFrame example
```python
import pandas as pd
from scattr import scattr

# create a new class that inherits from pd.DataFrame
# and includes methods defined in a 'helper.py' file
ScattrFrame = scattr(cls=pd.DataFrame, src='helper')

# instantiate the new class
df = ScattrFrame(data=pd.read_csv('risk_factors_cervical_cancer.csv'))

# test methods added from helper file
df.say_hi()

# test CowClass added from helper file
df.CowClass.say_moo()

# test method from parent class
df.head(n=1)

# confirm that df is an instance of pd.DataFrame and PydyFrame
isinstance(df, (pd.DataFrame, ScattrFrame))

# confirm that ScattrFrame is a subclass of pd.DataFrame
issubclass(ScattrFrame, pd.DataFrame)
```