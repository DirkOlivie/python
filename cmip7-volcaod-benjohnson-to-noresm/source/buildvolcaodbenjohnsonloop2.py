import buildvolcaodbenjohnson

def buildvolcaodbenjohnsonloop2(inputversion,origindescriptionlist, outputversion, hybridperiod, desiredheightunits, desiredextinctionunits, intpmethodlist, overwrite):
#------------------------------
#
    '''
    MODIFICATIONS
        (2026-10-30)
            inputarguments modified : periodlist (removed), inputversion (removed), descriptionlist (new)
            loop over perilodlist removed


    INPUT
        period
        inputversion
        outputversion
        desiredheightunits
        desiredextinctionunits
        intpmethodlist
        overwrite : False | True
        
    CALLED BY
        loopvolc

    CALLS
        volc_internal

    '''
#   
    for intpmethod in intpmethodlist :

        buildvolcaodbenjohnson.buildvolcaodbenjohnson(inputversion=inputversion, \
                                                      origindescriptionlist=origindescriptionlist, \
                                                      outputversion=outputversion, \
                                                      hybridperiod=hybridperiod, \
                                                      desiredheightunits=desiredheightunits, \
                                                      desiredextinctionunits=desiredextinctionunits, \
                                                      intpmethod=intpmethod, \
                                                      overwrite=overwrite)
