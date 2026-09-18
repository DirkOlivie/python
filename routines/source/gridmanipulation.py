import numpy as np

def lon2lonbnds (longitude) :
    '''
    PARAMETERS
    ----------
   	array with longitude of grid cell centers

    RETURNS
    -------
	array with boundaries of grid cells
    '''
    #
    nlon = len(longitude)
    # new array
    lonbnds = np.zeros( (nlon+1) )
    #
  
    lonbnds[1:nlon] = 0.5 * ( longitude[0:nlon-1] + longitude[1:nlon] ) # meaning of : is different
    # begin 
    lonbnds[0] = lonbnds[1] - ( lonbnds[2] - lonbnds[1] )
    # end       
    lonbnds[nlon] = lonbnds[nlon-1] + ( lonbnds[nlon-1] - lonbnds[nlon-2] )
  
    return lonbnds
#
#
def lat2latbnds(latitude) :
    '''
    MODIFICATIONS
	(2019-11-26) : relaxed the condition for sum(latitude) : 5.e-4 -> 5.e-3	
		due to problems with emiss_AERmon_HadGEM3-GC31-MM_piControl_r1i1p1f1_gn_233001-234912.nc : sum(latitude) = 0.00168		
	(2020-05-15) : BUG : latbnds[nlat-1] = 90. -> latbnds[nlat] = 90.

    INPUT
        latitude : 1-dim array [nlat]

    RETURN
        latbnds : 1-dim array [latbnds]
    '''
    if abs(sum(latitude)) >= 5.e-3 :
        print(str('Latitude not correct ...'))
        print(str('Sum is : '), str(sum(latitude)))
        print(str('First latitude = '), str(latitude[0]))
        print(str('Last  latitude = '), str(latitude[latitude.len-1]))
        print(str(latitude))
        quit()
    #
    nlat = len(latitude)
    latbnds =np.zeros( (nlat+1) )


    latbnds[1:nlat] = 0.5 * ( latitude[0:nlat-1] + latitude[1:nlat] )
    # begin / enid element
    latbnds[0] = latbnds[1] - ( latbnds[2] - latbnds[1] ) 
    latbnds[nlat] = latbnds[nlat-1] + ( latbnds[nlat-1] - latbnds[nlat-2] )

    if ( latitude[1] - latitude [0] ) > 0. :
        latbnds[0]    = -90.
        latbnds[nlat] =  90.    # BUG 2020-05-15 : latbnds[nlat-1] =  90.
    elif ( latitude[1] - latitude [0] ) < 0. :
        latbnds[0]    =  90.
        latbnds[nlat] = -90.
    else :
        print(latitude)
        quit()
#
    return latbnds
#
#
def getlonoverlap ( x , y ) :
    ''' 
    MODIFICATION
	(2017-04-07) Modified constraint for x1 and y1 : 0.01 -> 0.0001

    shift everything such that
    x0=0
    all angles are in [0, 360]

    '''
    x0=x[0]
    x1=x[1]

    y0=y[0]
    y1=y[1]

    x1=(x1-x0+720.) % 360.
    if x1 <= 0.0001 : x1 = 360.
    y0=(y0-x0+720 ) % 360.
    y1=(y1-x0+720.) % 360.
    if y1 <= 0.0001 : y1 = 360.
    x0=0.
#
    wy=(y1-y0+720.) % 360.
    if wy <= 0.01 : wy=360.
#
    wz=0.
    if y0 < y1 :
    # normal case
        if ( y1 >= x0 and y0 <= x1 ) :
            z0=max([x0,y0])
            z1=min([x1,y1])
            wz=abs(z1-z0)
        wz

    else : 
        wz=min([x1,y1])+max([0.,x1-y0])

    return wz
