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

