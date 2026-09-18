import buildvolcaod

def buildvolcaodloop2(inputperiod, outputperiod, inputversion, outputversion, desiredheightunits, desiredextinctionunits, wvl_interpolation_type_list, var_weighting_type, overwrite):
#--------------------
#
    '''
    INPUT
        inputperiod
        outputperiod
        inputversion
        outputversion
        desiredheightunits
        desiredextinctionunits
        wvl_interpolation_type_list : 'constant' | 'blackbody'
        var_weighting_type
        overwrite : False | True
        
    CALLED BY
        loopvolc

    CALLS
        volc_internal

    '''
#
#    if ( outputperiod == '1750-2023-monthly' ) :
#       datelist=['1750-01','1750-02','1750-03','1750-04','1750-05','1750-06','1750-07','1750-08','1750-09','1750-10','1750-11','1750-12']
#        datelist=['1750-01','1750-02']
#    elif ( outputperiod == '1850-2021-meanseasonalcycle' ) :
#       datelist=['1750-01','1750-02','1750-03','1750-04','1750-05','1750-06','1750-07','1750-08','1750-09','1750-10','1750-11','1750-12']
#        datelist=['1750-01','1750-02']
#
#    else :
#        print('No peridtype recognized : ', periodtype)
#        quit() 
#
    for wvl_interpolation_type in wvl_interpolation_type_list :

        buildvolcaod.buildvolcaod(inputperiod=inputperiod, \
                                  outputperiod=outputperiod, \
                                  inputversion=inputversion, \
                                  outputversion=outputversion, \
                                  desiredheightunits=desiredheightunits, \
                                  desiredextinctionunits=desiredextinctionunits, \
                                  wvl_interpolation_type=wvl_interpolation_type, \
                                  var_weighting_type=var_weighting_type, \
                                  overwrite=overwrite)
