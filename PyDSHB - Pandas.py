import numpy as np
import pandas as pd

# %% The Panda Series Object
data = pd.Series(np.linspace(0.25, 1, 4), index=list('ABCD')) # series
data_values = data.values     # attribute, returns: ndarray
data_index = data.index      # attribute, returns: RangeIndex
# A dictionary
pop_dict = {'CA': np.random.randint(1e6), 'TX': np.random.randint(1e6), 'NY': np.random.randint(1e6),
            'IL': np.random.randint(1e6)}
# Series from dictionary
pop = pd.Series(pop_dict)
# Item access is similar for dictionaries and Series
pop_dict['CA']
pop['CA'] # etc
# Advantage of series is array-style indexing (e.g., splicing)
# pop_dict['CA':'NY'] # returns error
pop['CA':'NY'] # works

"""
Several ways to create a series from scratch
    pd.Series(data, index=index)
    Data = list, np array, scalar, dictionary (shown above)
    index = auto starting from 0 if undefined, typically an array like entity
"""

mydict = {'A': 0, 'B': 1, 'C': 2, 'D': 3}  # dynamic type indices and values
myseries = pd.Series(mydict)  # static type indices and values

# %% The Pandas DataFrame Object

" can be built from multiple series with the same index object "
ind = list('ABCD')
s1 = pd.Series(np.random.randint(0, 100, 4), index=ind)
s2 = pd.Series(np.random.randint(0, 100, 4), index=ind)
s3 = pd.Series(np.random.randint(0, 100, 4), index=ind)
# each series here shares the same index ind
# we'll build a dict from these with unique keys, and turn the dict into a df. The keys will default to column names
df = pd.DataFrame({'S1': s1, 'S2': s2, 'S3': s3})
# index and column attributes are both index objects!
df.index
df.columns
"""
there are many ways to construct a dataframe
pd.DataFrame(data, columns=col)
data = list of dictionaries, dictionary of series objects, 2d np array, np structured array
"""

# % The Pandas Index Object
ind = pd.Index([2, 3, 5, 7, 11]) # index object is an immutable array / ordered set

# %% Data Selection in DataFrames
""" 
recall a df is like a dictionary of series, all sharing the same index, with column names serving as the "keys".
individual series are accessed via dictionary-style item access:
"""
df['S1']
"""
if col is nice string, can also use df.S1 (attribute style), doesn't work all the time, 
can be confused with other attributes, not recommended
"""
# dict-style item access can also be used to modify the df object (e.g., create new column)
df['S4'] = df['S1'] + df['S2'] + df['S3']
"""
majority of indexing dfs will be in this column-wise fashion, but suppose you're interested in accessing row items?
(what if row index is same as column index?)
this is generally referred to as "array-style item access"
use iloc, loc, and ix to index as an array
"""




# %% Operating and Data in Pandas
# Ufuncs: Index preservation
ser = pd.Series(np.random.randint(0, 10, 4))
df1 = pd.DataFrame(np.random.randint(0, 10, (3, 4)), columns=['c0', 'c1', 'c2', 'c3'], index=['r0', 'r1', 'r2'])
# Ufuncs: Index alignment
s3['E'] = np.random.randint(100)
s4 = s1 / s3  # resulting array contains the union of the indices of s1 and s3
s1.index.union(s3.index)

df2 = df1 * 2

df1['c0']['r0'] = np.nan

df1.dropna(axis='columns')

