from pandas import Series, DataFrame
from pandas import Series, Dataframe
import pandas as pd


data = {'state': ['Ohio','Ohio','Ohio','Nevada', 'Nevada'],
        'year':  [200,2001,2002,2001,2002],
        'pop':   [1.5,1.7,3.6,2.4,2.9]]
frame = DataFrame(data)
frame
data = {'state': ['Ohio','Ohio','Ohio','Nevada', 'Nevada'],
        'year':  [200,2001,2002,2001,2002],
        'pop':   [1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data)
frame
DataFrame(data, columns=['year', 'state','pop'])
DataFrame(data, columns=['year', 'state','pop','debt'])
frame2['state']
frame2 = DataFrame(data, columns=['year', 'state','pop','debt'])
frame2
frame2.columns
frame2 = DataFrame(data, columns=['year', 'state','pop','debt'])
frame2
frame2.columns
frame2['state']
frame2.year
data = {'state': ['Ohio','Ohio','Ohio','Nevada', 'Nevada'],
        'year':  [2000,2001,2002,2001,2002],
        'pop':   [1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data)
frame
# Here is how you can build a dataframe outright
data = {'state': ['Ohio','Ohio','Ohio','Nevada', 'Nevada'],
        'year':  [2000,2001,2002,2001,2002],
        'pop':   [1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data)
frame
 
# You can specify column sequence
DataFrame(data, columns=['year', 'state','pop'])
 
# Non-existant columns show NAN
frame2 = DataFrame(data, columns=['year', 'state','pop','debt'])
frame2
frame2.columns
 
# A column can be retrieved as a Sereis either by dict-like notation or by attribute
frame2['state']
frame2.year
frame2['state']
frame2.year
frame2[3]
frame2(3)
frame2[1]
frame2['three']
frame2 = DataFrame(data, columns=['year', 'state','pop','debt'],
                         index=['one', 'two','three','four','five'])
frame2
frame2.columns
 
# A column can be retrieved as a Sereis either by dict-like notation or by attribute
frame2['state']
frame2.year
 
#rows can be retireved by position or by ix method
frame2['three']
frame2 = DataFrame(data, columns=['year', 'state','pop','debt'],
                         index=['one', 'two','three','four','five'])
frame2['three']
frame2
frame2.ix[2]
frame2.ix['three']
frame2['debt'] = 16.5
frame2
np.arrange(5.)
np.arange(5.)
frame2['debt'] = np.arange(5.)
frame2
val = Series([-1.2,-1.5,-1.7], index=['two','four','five'])
frame2['debt'] =  val
frame2
frame2['eastern'] = frame2.stat=='Ohio'
frame2
frame2['eastern'] = frame2.state=='Ohio'
frame2
del frame['eastern']
frame2
del frame2['eastern']
frame2
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000:1.5, 2001:1.7,2002:3.6}}
pop
pop.T
pop.t
frame3 = DataFrame(pop)
pop.T
frame3.T
DataFrame(pop, index=[2001,2002,2003])
frame3[:-1]
frame3[:-2]
frame3[:-0]
frame3[:]
pdata = {'Ohio':frame3['Ohio'][:-1],
         'Nevada':frame3['Nevada'][:2]}
DataFrame(pData)
DataFrame(pdata)
frame3.index.name = 'year'; frame.columns.name='state'
frame3
frame.columns.name='state'
frame3
frame3.index.name = 'year'; frame3.columns.name='state'
frame3
frame3.values
frame2.values
hist