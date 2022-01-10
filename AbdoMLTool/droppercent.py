# drop rows with a lot of missing data
# Importing required Libraries
import pandas as pd
import math
# Drop Percent Function which drops rows/columns based on  accepted percentage missing values, default axis is 0 (rows).
# for example : x,y = droppercent(certif,20, axis=1) will return a table in y where the only columns left are one that are atleast 20% filled, 
# setting threshold to 100 keeps only columns that have no NAN values
def droppercent(df, threshold, axis=0):
    # Checking types for variable df.
    if isinstance(df, pd.DataFrame):
        pass
    else:
        print("First parameter should be a Pandas DataFrame.")
        return
    # Checking types for variable threshold.
    if isinstance(threshold, int):
        pass
    else:
        print("Second parameter should be a Integer for Percentage.")
        return
    # Checking types for variable axis.0=row, 1=column
    if isinstance(axis, int) and (axis == 0 or axis == 1):
        pass
    else:
        print("Third parameter should be 0 for rows or 1 for columns for axis.")
        return
    # Getting the original index
    origindex = df.index.values.tolist()
    # Calculating threshold - here threshold is (Drop rows/columns with less than 2(example threshold) Non-nan values)
    if axis == 1:
      a=0
    if axis ==0:
      a=1
    threshold = math.ceil((df.shape[a]) * ( (threshold / 100)))
    print('require atleast this many non-NA= '+str(threshold)+'\n')
    # Dropping based on threshold and axis.
    df=df.dropna(axis=axis, thresh=threshold)
    # Getting the new index
    newindex = df.index.values.tolist()
    # Using list comprehension to get values not in new index
    droppedindex = list(set(origindex).difference(newindex))
    # Returning output
    return [droppedindex, df]
