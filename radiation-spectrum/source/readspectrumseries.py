import readspectrumseries_cdr

def readspectrumseries(var, origin, wvlresolution, freqtype):
#---------------------
#
    '''
    INPUT
        var
        origin
        wvlresolution
        year0
        year1
    '''
#
    if ( var == 'TSI' and origin == 'ClimateDataRecord' ) : data = readspectrumseries_cdr.readspectrumseries_cdr(var=var, wvlresolution=wvlresolution, freqtype=freqtype)
    else :
        print('+++ readspectrumseries +++')
        print('No var or origin recognized : ', var, origin)
        quit()
#
    return data
