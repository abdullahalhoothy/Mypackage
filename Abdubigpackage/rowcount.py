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