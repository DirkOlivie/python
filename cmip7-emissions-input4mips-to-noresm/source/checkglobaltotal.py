import numpy as np

import getgridtype

#import sys
#sys.path.insert(0,'/nird/home/olivie/scripts-python')
#import areafraction

#sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-volc/source')
#import readareatopography

def  checkglobaltotal(D):
#--------------------------
    '''
    REMARK
        assumes 365.25 days per year

    CALLED BY

    CALLS
	    areafraction
        readtopography (also to obtain the area)

    MODIFICATIONS
        (2025-10-28) adding resolution as an input argument

    '''
#----------------------------------------
#
    if ( D['dim'] == '3d' ) :
        nlev=len(D['levbnds'])-1

    ntime=D['ntime']
#
    gridtype=getgridtype.getgridtype(resolution=D['resolution'])
#   area
#    if (   gridtype == 'latlon' )    : area = areafraction.areafraction(longitude=D['longitude'], latitude=D['latitude'], outputtype='area')
#    elif ( gridtype == 'irregular' ) : area = readareatopography.readareatopography(grid=D['resolution'], variable='area')
#    else : print('+++ checkglobaltotal +++') ; print('No gridtype recognized') ; quit()
    area=D['area']

    
#
#   units : fmass and ftime factor
    if ( D['units'] == 'kg m-2 s-1' or D['units'] == 'kg m-3 s-1' ) : 
        ftime=86400.*365.25  # s-1 -> yr-1
        fmass=1.e-9          # kg  -> Tg
    else : 
        print('No units recoginzed : ', D['units'])
        quit()
#
#   hfactor    
    if ( D['dim'] == '2d' ) : 
        hfactor = 1.
    elif ( D['dim'] == '3d' ) :  
        if (   D['lev_units'] == 'km' ) : hfactor=1000.
        elif ( D['lev_units'] == 'm'  ) : hfactor=1.
        else : print('+++ checkglobaltotal +++') ; print('No levunits recognized : '), D['levunits'] ; quit()
#
#   global total
    if ( D['dim'] == '2d' ) :
        if   ( gridtype == 'latlon'    ) : globtotal = np.sum(area*D['field'][:,:,:]) / float(ntime)      
        elif ( gridtype == 'irregular' ) : globtotal = np.sum(area*D['field'][:,:  ]) / float(ntime)
        else : print('+++ checkglobaltotal +++') ; print('No gridtype recognized') ; quit()

    elif ( D['dim'] == '3d' ) :    
        globtotal = 0.
        for ilev in range(0,nlev) :
            if   ( gridtype   == 'latlon'  ) : globtotal = globtotal + np.sum(area*D['field'][:,ilev,:,:]) * ( D['levbnds'][ilev+1] - D['levbnds'][ilev] ) / float(ntime)      
            elif ( gridtype == 'irregular' ) : globtotal = globtotal + np.sum(area*D['field'][:,ilev,:  ]) * ( D['levbnds'][ilev+1] - D['levbnds'][ilev] ) / float(ntime)
            else : print('+++ checkglobaltotal +++') ; print('No gridtype recognized') ; quit()
#
    globtotal = globtotal * ftime * fmass * hfactor
#
    print('Globaltotal [Tg/yr] - '+D['activity']+' - '+D['sector']+' - '+D['species']+' : ', globtotal)
#
    return globtotal
