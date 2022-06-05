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