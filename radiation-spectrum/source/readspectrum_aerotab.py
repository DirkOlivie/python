import readfile_aerotab


def readspectrum_aerotab(var):
#-------------------
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
    if   ( var == 'SSI' ) : data = readfile_aerotab.readfile_aerotab(var=var)
    else :
        print('+++ generatespectrum_aerotab +++')
        print('No var or origin recognized : ', var, origin)
        quit()
#
    return data
