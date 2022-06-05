#################################################
# Partialaggr
#################################################
# Importing libraries
import pandas as pd

# Method defination
def stringgroup(col_substring, df, skipint=0):
    # Getting all columns
    cols = [col for col in df.columns[skipint:] if col_substring in col]
    # Deep Copying to a new dataframe
    newdf = df.copy()
    # Dropping columns that are not required
    newdf.drop(df.columns[skipint:], axis=1, inplace=True)
    # List for storing the result
    result = []
    # Looping through the original dataframe
    for idx, row in df.iterrows():
        sum = 0
        # Looping through the selected columns
        for col in cols:
            try:
                # Generating the sum of all columns
                sum += int(row[col])
            except:
                if str(row[col]) != 'nan':
                    # In case of abnormal values.
                    print("Invalid column data in row " + str(idx) + " of type: " + type(row[col]).__name__)
        # Appending the result
        result.append(sum)

    # Adding a new column to new dataframe to store results
    newdf['result'] = result
    return newdf


if __name__ == '__main__':
    # Sample data
    data = [(2000,1,5,6,8,9), (2000,2,3,5,4,6)]
    df = pd.DataFrame(data, columns=['year', 'month', 'soccer goals', 'soccer assist', 'soccer points', 'basketball goals'])
    ndf = stringgroup('socc', df, 2)
    print(ndf)


#################################################
# rowblock
#################################################
#takes file path and returns an iterable (rowblock)
def rowblock(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b
##lazyrow = rowblock("C:/Users/pc/Google Drive/Personal/Work/Online/Jupyter/Git/CoronaWhy/SS.txt")



#################################################
# rowcount
#################################################
#takes file path and returns an iterable (rowblock)
def rowblock(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b
##lazyrow = rowblock("C:/Users/pc/Google Drive/Personal/Work/Online/Jupyter/Git/CoronaWhy/SS.txt")


#takes file path and counts rows (countrows)
def rowcount(files, size=65536):
    with open(files, "r",encoding="utf-8",errors='ignore') as f:
        #print (sum(bl.count("\n") for bl in rowblock(f)))
        totalrow=sum(bl.count("\n") for bl in rowblock(f))
    return totalrow

    #use case 
    # rowCount("C:/Users/pc/Google Drive/Personal/Work/Online/Jupyter/Git/CoronaWhy/SS.txt")


#################################################
# droppercent
#################################################
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


#################################################
# batchsplit
#################################################
#takes in big file (bigSplit)
def batchsplit(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]        
# return a lazy iterator. These are objects that you can loop over like a list. 
# use case below

#lazygen = batchsplit.batchsplit(dictionary, 10)
#next(lazygen)
#next(lazygen)

#################################################
# loaddf
#################################################
# Importing the library
import pandas as pd
# The function which takes input a list of paths and output the list of dataframes
def dflists(paths):
    dflist = []
    # Loop through the list of paths
    for path in paths:
        # Read or raise exception if cannot read
        try:
            df = pd.read_csv(path)
            # Append to a dataframe list which can later be accessed by dflist[1] for first dataframe.
            dflist.append(df)
        except Exception as e:
            # Outputting the error message.
            print("Unable to read CSV with path: " + str(path))
            print("Error: " + str(e))
    # Return the dataframe list
    return dflist

