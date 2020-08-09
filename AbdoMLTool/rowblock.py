#takes file path and returns an iterable (rowblock)
def rowblock(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b
##lazyrow = rowblock("C:/Users/pc/Google Drive/Personal/Work/Online/Jupyter/Git/CoronaWhy/SS.txt")
