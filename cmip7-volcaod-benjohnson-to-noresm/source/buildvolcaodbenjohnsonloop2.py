import buildvolcaodbenjohnson

def buildvolcaodbenjohnsonloop2(periodlist, inputversion, outputversion, desiredheightunits, desiredextinctionunits, intpmethodlist, overwrite):
#------------------------------
#
    '''
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
    for period in periodlist :
        for intpmethod in intpmethodlist :

            buildvolcaodbenjohnson.buildvolcaodbenjohnson(period=period, \
                                                          inputversion=inputversion, \
                                                          outputversion=outputversion, \
                                                          desiredheightunits=desiredheightunits, \
                                                          desiredextinctionunits=desiredextinctionunits, \
                                                          intpmethod=intpmethod, \
                                                          overwrite=overwrite)
