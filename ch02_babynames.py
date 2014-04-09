import pandas as pd

os.chdir('/home/brad/Desktop/pydata-book/ch02/names/')

!head -n 10 yob1880.txt

# can be read in as csv
names1880 = pd.read_csv('yob1880.txt',names=['name','sex','births'])
names1880.groupby('sex').births.sum()

# now will use pandas concat to pull in many files at once
years = range(1880,2011)
pieces = []
columns = ['name','sex','births']
for year in years:
  path = 'yob%d.txt' % year
  frame = pd.read_csv(path, names=columns)
  frame['year'] = year
  pieces.append(frame)
#... and then we need to concat everything together
names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table('births', rows='year',cols='sex',aggfunc=sum)
total_births.tail()
total_births.plot(title='total births by sex and year')

# add a function to determine total proportion by name
def add_prop(group):
    #Integer division floors
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year','sex']).apply(add_prop)

# Need to do a sanity check to verify that all the props add to the correct number
np.allclose(names.groupby(['year','sex']).prop.sum(),1)

# Now will look for the top 1000 names
def get_top1000(group):
    return group.sort_index(by='births',ascending=False)[:1000]
grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)

# do a gender split
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births', rows='year', cols='name', aggfunc=sum)

subset = total_births[['John', 'Brad','Kim']]

subset.plot(subplots=True, figsize=(12,10), grid=False,title="Number of births per year")

# analysis to verify if the decreases are fewer parents choosing popular names.
# Will verify by checking how much proportion the top 1000 names have.
table = top1000.pivot_table('prop',rows='year',cols='sex', aggfunc=sum)
table.plot(title='Sum of the table1000.prop by year and sex',yticks=np.linspace(0,1.2,13), xticks=range(1880,2020,10))

# Now going to try to calculate the number of names in the top 50%
# Will first take a look at a boys 2010 subset
df = boys[boys.year == 2010]
prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
# looking at the top 10
prop_cumsum[:10]
prop_cumsum.searchsorted(0.5)
# but we have to add one becuase of the zero indexing
# now try again for 1900 boys
df = boys[boys.year == 1900]
in1900 = df.sort_index(by='prop', ascending=False).prop.cumsum()
in1900.searchsorted(0.5) + 1

# now we build the function and apply
def get_quantile_count(group, q=0.5):
    group = group.sort_index(by = 'prop', ascending=False)
    return group.prop.cumsum().searchsorted(q) + 1
    
diversity = top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
diversity.plot(title = 'Number of popular names in top 50%')

# last letter revolution
#extract the las letter from the name column
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births', rows=last_letters, cols=['sex','year'], aggfunc=sum)

# Quick subtable view
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
subtable.head()

# Quick way to normalize....
subtable.sum()
letter_prop = subtable / subtable.sum().astype(float)

import matplotlib.pyplot as plt
fig, axes = plt.subplots(2,1,figsize=(10,8))
letter_prop['M'].plot(kind='bar',rot=0,ax=axes[0],title='Male')
letter_prop['F'].plot(kind='bar',rot=0,ax=axes[1],title='Female')

letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d','n','y'],'M'].T
dny_ts.head()
dny_ts.plot()

# Now we will view the plots of gender changing names over time
all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').births.sum()

table = filtered.pivot_table('births', rows='year', cols='sex',aggfunc=sum)
table = table.div(table.sum(1), axis=0)
table.plot(style={'M': 'k-', 'F': 'k--'})








