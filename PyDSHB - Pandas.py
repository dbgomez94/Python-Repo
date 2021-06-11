import numpy as np
import pandas as pd

# %% The Panda Series Object
data = pd.Series(np.linspace(0.25, 1, 4), index=list('ABCD')) # series
data_values = data.values     # attribute, returns: ndarray
data_index = data.index      # attribute, returns: RangeIndex

mydict = {'A': 0, 'B': 1, 'C': 2, 'D': 3}  # dynamic type indices and values
seriesfromdict = pd.Series(mydict)  # static type indices and values

# %% The Pandas DataFrame Object
s1 = pd.Series(np.random.randint(0, 100, 4), index=list('ABCD'))
s2 = pd.Series(np.random.randint(0, 100, 4), index=list('ABCD'))
s3 = pd.Series(np.random.randint(0, 100, 4), index=list('ABCD'))
df = pd.DataFrame({'Series 1': s1, 'Series 2': s2, 'Series 3': s3})

# % The Pandas Index Object
ind = pd.Index([2, 3, 5, 7, 11])

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