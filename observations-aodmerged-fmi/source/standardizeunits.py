def standardizeunits(data):
#-------------------
    '''
    AIM
        replacing the model mask (1 everywhere) by the mask from toe observations


    INPUT
        data (already read data from model, and interpolated to observation grid)
        var
        year0
        year1
 
    RETURN
        structure containing 
            var
            field[nlon x nlat x ntime]
               
    CALLS
        readobsmodelperiod
    '''
#---------------------------------------------------------
#
# read observational data
    print('+++ standardizeunits +++')
#
    if ( var == 'toc' ) : 
       if ( data['units'

    else :
        print('No var recognized : '+var)
        quit()
#
# impose observational mask to the model data
    data['mask']=obsdata['mask']
#
    return data
