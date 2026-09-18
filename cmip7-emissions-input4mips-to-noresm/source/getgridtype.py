def getgridtype(resolution):
#--------------
    '''
    INPUT
        resolution

    RETURN
        gridtype            

    MODIFICATIONS
        (2025-10-18) creation

    '''
    if   ( resolution == '0.9x1.25') : gridtype = 'latlon'
    elif ( resolution == '1.9x2.5' ) : gridtype = 'latlon'
    elif ( resolution == 'ne30pg3' ) : gridtype = 'irregular'
    elif ( resolution == 'ne16pg3' ) : gridtype = 'irregular'
    else :
        print('+++ getgridtype +++')
        print('No resolution recognized : ', resolution)
        quit()

    return gridtype
