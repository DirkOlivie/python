import readobsmodelperiod

def modifymask(data, var, year0, year1):
#-------------
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
    print('+++ modifymask +++')
#
    if ( var == 'od550aer' ) : obsdata=readobsmodelperiod.readobsmodelperiod(expid='aodmergedfmi' , year0=year0, year1=year1, var=var)
    elif ( var == 'toc'     ) : obsdata=readobsmodelperiod.readobsmodelperiod(expid='toccopernicus', year0=year0, year1=year1, var=var)
    else :
        print('No var recognized : '+var)
        quit()
#
# impose observational mask to the model data
    data['mask']=obsdata['mask']
#
    return data
