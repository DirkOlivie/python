import numpy as np

import buildoxidants

def buildoxidantsloop2(bctype, specieslist, expiddescriptionlist, version, overwrite):
#---------------------
    '''
    INPUT
        specieslist
        periodexpiddescriptionlist
        version
        overwrite

    CALLED BY
        buildoxidantsloop

    CALLS
        buildozone

    '''

    #
    buildoxidants.buildoxidants(bctype=bctype, specieslist=specieslist, expiddescriptionlist=expiddescriptionlist, version=version, overwrite=overwrite)
