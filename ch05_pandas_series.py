import numpy as np
from pandas import Series, DataFrame
import pandas as pd



obj = Series([4, 7, -5, 3])
obj

obj.values
obj.index

obj2 = Series([4,7,-5,3], index=['d','b','a','c'])
obj2

obj2.index

# You can also use the index when selecting calues
obj2['a']
obj2['d']=6
obj2[['c','a','d']]

# Scaler operations will preserve the index
obj[obj2 >0 ]
obj2 * 2
np.exp(obj2)

# Can also be though of as an ordered dict
'b' in obj2
'e' in obj2

# If you have data in a python dict, you can create a Series from it by passing the dict
sdata = {'Ohio' :35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3
# When passing a dict, the index will be in dict keys sorted order

states = ['California','Ohio','Oregon','Texas']
obj4 = Series(sdata, index=states)
obj4

# A series index can be altered in place by assignement
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj

