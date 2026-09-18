from netCDF4 import Dataset

def getgridtype(filename):
#--------------
    '''
    AIM
        distnguish between SE and FV cam grids based on dimensions in file

    INPUT
        filename

    RETURN
        gridtype : 'latlon' | 'irregular'

    '''

    nc_fid= Dataset(filename, 'r')
    dimlist=nc_fid.dimensions.keys()
    nc_fid.close
    if   ( 'ncol' in dimlist                       ) : gridtype = 'irregular'
    elif ( 'lat'  in dimlist and 'lon' in dimlist ) : gridtype = 'latlon'
    else :
        print('+++ getgridtype +++')
        print('No gridtype recognized in file : ', filename)
        quit()

    return gridtype     
