import numpy as np

import buildoxidants

def buildoxidantsloop2(bctype, specieslist, expiddescriptionlist, time_units, calendar, version, overwrite):
#---------------------
    '''
    MODIFICATIONS
        (2026-10-19) : adding arguments : time_units and calendar

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
    buildoxidants.buildoxidants(bctype=bctype, specieslist=specieslist, expiddescriptionlist=expiddescriptionlist, time_units=time_units, calendar=calendar, version=version, overwrite=overwrite)
