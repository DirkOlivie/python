import createscripfile

def loopcreatescripfile2(gridlist, version):
#-----------------------

    for grid in gridlist :

        createscripfile.createscripfile(grid=grid,version=version)
