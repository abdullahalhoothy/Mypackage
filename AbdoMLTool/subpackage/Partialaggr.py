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