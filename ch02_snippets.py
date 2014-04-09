import os
import json

os.chdir('/home/brad/Desktop/pydata')
path = '../pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

# To view the firest record of the file
open(path).readline()

# to import using the json module
records =[json.loads(line) for line in open(path)]

records[0]
records[0]['tz']
print records[0]['tz']

# method for exrtacting which time zon occures the most
time_zones = [rec['tz'] for rec in records]   # this method errors b/c not all recors have 'tz'
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]

# Hard way to count up the time zones
def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

# and the alternate hard way with collections
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts    

# now we can tests our functions
counts = get_counts(time_zones)
counts['America/New_York']
counts2 = get_counts2(time_zones)
counts2['America/New_York']
len(time_zones)

# Hard way to get the top 10
def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

top_counts(counts)

#Can make the second part a little easier using the collections class
from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)

# Now onto the method using pandas
from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
frame
frame['tz'][:10]
tz_counts = frame['tz'].value_counts()
tz_counts[:10]

# clean a little to present...
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]

# we can creat a grphic using the plot method
tz_counts[:10].plot(kind='barh', rot=0)

# we can evaluate teh first toek string
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]

# Now we want to analyze what the decomp of tz is by OS

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe.a.str.contains('Windows'),'Windows','Not Windows')
operating_system[:5]

#Now we will group into columns
by_tz_os = cframe.groupby(['tz',operating_system])
by_tz_os.size()[:10]
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]
agg_counts.sort_index(by='Windows', ascending=False)[:10]

# We will use some indirect indexer to get row counts
indexer = agg_counts.sum(1).argsort()
indexer[:10]
# Then we will slice off only the last 10 rows#
count_subset = agg_counts.take(indexer)[-10:]
count_subset
# plot it
count_subset.plot(kind='barh', stacked = True)
normed_subset = count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh', stacked = True)





