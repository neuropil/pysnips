import numpy as np
from pandas import Series, DataFrame
import pandas as pd

obj = Series(range(3), index=['a','b','c'])
index = obj.index

index
index[1:]

# indexes are immutable and therefore can not be changed by the user.

index[1]='d'

# This is done so that index objects can be shared between structures
index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
obj2.index is index