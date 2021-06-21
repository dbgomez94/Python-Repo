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
pop['CA']# etc
# Advantage of series is array-style indexing (e.g., splicing)
# pop_dict['CA':'NY'] # returns error
pop['CA':'NY'] # works
"""
Several ways to create a series from scratch
    pd.Series(data, index=index)
    Data = list, np array, scalar, dictionary (shown above)
    index = auto starting from 0 if undefined, typically an array like entity
"""
mydict = {'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3}  # dynamic type indices and values
myseries = pd.Series(mydict)  # static type indices and values


# %% The Pandas DataFrame Object
" can be built from multiple series with the same index object "
ind = ['R0', 'R1', 'R2', 'R3']
s0 = pd.Series(np.random.randint(0, 10, 4), index=ind)
s1 = pd.Series(np.random.randint(0, 10, 4), index=ind)
s2 = pd.Series(np.random.randint(0, 10, 4), index=ind)
# each series here shares the same index ind
# we'll build a dict from these with unique keys, and turn the dict into a df. The keys will default to column names
df = pd.DataFrame({'C0': s0, 'C1': s1, 'C2': s2})
# index and column attributes are both index objects!
df.index
df.columns
"""
there are many ways to construct a dataframe
pd.DataFrame(data, columns=col)
data = list of dictionaries, dictionary of series objects, 2d np array, np structured array
"""
# % The Pandas Index Object
pd.Index([2, 3, 5, 7, 11])  # index object is an immutable array / ordered set


# %% Data Selection in DataFrames
""" 
recall a df is like a dictionary of series, all sharing the same index, with column names serving as the "keys".
individual series are accessed via dictionary-style item access:
"""
df['C1']
"""
if col is nice string, can also use df.C1 (attribute style), doesn't work all the time, 
can be confused with other attributes, not recommended
"""
# dict-style item access can also be used to modify the df object (e.g., create new column)
df['C3'] = df['C0'] + df['C1'] + df['C2']  # this is implicit indexing
df.loc[:, 'C3'] = df.loc[:, 'C0'] + df.loc[:, 'C1'] + df.loc[:, 'C2']  # this is explicit (preferred)
"""
majority of indexing dfs will be in this column-wise fashion, but suppose you're interested in accessing row items?
(what if row index is same as column index?)
this is generally referred to as "array-style item access"
use iloc, loc, and ix to index as an array

two kinds:
1. implicit - uses implicit underlying indices (always 0 to n-1), but row and col names are preserved!
2. explicit - uses the explicitly designated indices (can be strings, numbers, etc.)
*** NOTE, first index is rows. "Rows before ..."
"""
ri = 2
ci = 3
rx = 'R2'
cx = 'C3'
df.iloc[ri]  # returns the row at index [r] as a pd ** Series ** with the column names now the index object
df.loc[rx]

df.iloc[:, ci]  # returns all the rows and the column at c
df.loc[:, cx]

df.iloc[ri,  ci]  # returns element at index [r, c], just like a 2d array
df.loc[rx, cx]

df.iloc[:ri, :ci]  # all up to but not including r, and all up to but not including c
df.loc[:rx, :cx]  # all up to AND including r, and all up to AND including c
"""
WARNING on splicing: explicit splicing is INCLUSIVE (whereas implicit splicing is exclusive)
"""

# %% Operating and Data in Pandas
# unary operations (one operand) preserve index and column labels
np.exp(s0)  # works on a Series
np.sin(df)  # and on a DataFrame
np.sqrt(df.loc['R0'])  # operand is a Series indexed from the DataFrame
# binary operations (two operands) will automatically align indices,
# if extra/missing indices, will return nan (can specify will arg: fill_value=##), returns sorted indices
s0 + s1  # "+" is a "wrapper" for np.add
np.add(s0, s1)  # numpy version
s0.add(s1)  # pandas version
s3 = np.add(s0, s1)
s3['R4'] = 0
s0 + s3  # returns NaN for R4 (does this work if numpy is not imported?)
np.add(s0, s1)  # returns NaN for R4
s0.add(s3, fill_value=0)  # returns 0 for R4
# index and columns are aligned and preserved in DataFrames
df + df
np.add(df, df)
df.add(df, fill_value=0)
# operating between DataFrames and Series
# first index is row, defaults to row-wise operation.
df - df.loc['R0']
df.subtract(df.loc['R0'])
df.subtract(df.loc[:, 'C0'], axis=0)  # substracts C0 column from df moving in axis 0 direction

# %% missing data
# other good functions: df.drop(), df.pop(), send a list if want multiple
df.loc['R3', 'C3'] = np.nan
df.dropna()  # drops the row with nan (will prolly use this one most)
df.dropna(axis=1)  # drops the col with nan
np.any(df.isnull())
df.loc['R3', 'C2'] = np.nan
df.loc[:, 'C2'].fillna(0)  # can specify which column to fill nans

# %% Hierarchical Indexing
# pd.MultiIndex(data, index=row_index, columns=col_index)
# lets create some toy data and create a dataframe
age = [41, 38, 24, 21]
gen = ['M', 'M', 'F', 'F']
race = ['W', 'NW', 'W', 'NW']

# option 1: dictionary of lists -- prolly the simplest in this case
midf = pd.DataFrame({'Age': age, 'Gen': gen, 'Alive': race})

# option 2: dictionary of series
s_age = pd.Series(age, name='Age')
s_gen = pd.Series(gen, name='Gen')
s_race = pd.Series(race, name='Race')
midf = pd.DataFrame({'Age': s_age, 'Gen': s_gen, 'Race': s_race})

# options 3: by zipping the list/series together
midf = pd.DataFrame(zip(s_age, s_gen, s_race), columns=[s_age.name, s_gen.name, s_race.name])

# lets multiindex on the rows, resulting df is referred to as a stacked df
# we'll use the age and gen columns
midf.index = pd.MultiIndex.from_frame(midf.loc[:, 'Gen':'Race'])  # just the last two columns
midf = midf.drop(['Gen', 'Race'], axis=1)  # drop those columns, leaving only Age
# indexing a stacked multi-index dataframe:
midf.loc['M', :]  # Dataframe
midf.loc['M', :].loc['NW', :]  # Series
midf.loc['M', :].loc['NW', :].loc['Age']  # int64
midf.loc[:, 'NW', :]  # Dataframe
# indexing an unstacked multi-index dataframe:
midf_us = midf.unstack()




