# Mypackage
This is a python package that contains some modules useful when dealing with data pre-processing


droppercent:  Drop Percent Function which drops rows/columns based on  accepted percentage missing values, default axis is 0 (rows).

loaddf :  takes input a list of paths and output the list of dataframes

PartialAggr: like pandas' groupby but aggregates columns based on partial string match 

Batchsplit: splits data pefore loading to csv, requires "iterable" as input

rowblock: takes file path and returns an iterable (rowblock)

rowcount: takes file path and counts rows (countrows)

remove_outliers: removes outliers from all numeric columns 


