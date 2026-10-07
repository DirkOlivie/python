import numpy as np

import builde90

def builde90loop2(specieslist, resolutionlist, periodlist, version, overwrite):
#----------------
    '''
    INPUT
        specieslist
        resolutionlist
        version
        overwrite

    CALLED BY
        builde90loop

    CALLS
        builde90

    '''

    #
    for species in specieslist :
        for resolution in resolutionlist :
            for period in periodlist :

                builde90.builde90(species=species, resolution=resolution, period=period, version=version, overwrite=overwrite)
