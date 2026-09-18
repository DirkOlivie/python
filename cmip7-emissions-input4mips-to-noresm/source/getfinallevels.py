import numpy as np

def getfinallevels(activity, sector, vertintp):
#--------------------------
    '''
    INPUT
        activity
        sector
        vertinp : 'nativie' : depends on the sector
                  'L21'     : up to 15 km 

    CALLED BY

    RETURNS structure containing
        altitude
        altitude_int
        nlev
        altitude_units
    '''
#
#   keep on native grid
    if ( vertintp == 'native' ) :

        if ( activity == 'air' ) :  altitude_int=np.array([0, 0.610, 1.220, 1.830, 2.440, 3.050, 3.660,  4.270,  4.880,  5.490,  6.100, \
                                                              6.710, 7.320, 7.930, 8.540, 9.150, 9.760, 10.370, 10.980, 11.590, 12.200, \
                                                             12.810,13.420,14.030,14.640,15.250]) # km

        elif ( activity == 'volc' ) :  altitude_int=np.array([ 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, \
                                                               3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75,  \
                                                               6, 6.25, 6.5, 6.75, 7, 7.25, 7.5 ]) # km

        elif ( activity == 'volcstratclim1850-2021' \
            or activity == 'volcstratclim1750-2023' ) : altitude_int=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, \
                                                                                 11,12,13,14,15,16,17,18,19,20, \
                                                                                 21,22,23,24,25,26,27,28,29,30, \
                                                                                 31,32,33,34,35,36,37,38,39,40])
       
        elif (activity == 'bb' )          : altitude_int =np.array([0.,0.1,0.5,1.,2.,3.,6.]) # km 
        
        elif ( activity == 'anthroprof' ) :
#           profemi = getvalue_commonblock(descriptor='profemi')
            profemi = 0 

#           standard case                          
            if ( profemi == 0 ) :

                if   ( sector == 'ENE' ) :  altitude_int=np.array([0.,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40]) # [km]
                elif ( sector == 'IND' ) :  altitude_int=np.array([0.,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40]) # [km]
                else :
                    print('+++ getfinallevels +++')
                    print('No sector recognized : ', sector)     
                    quit()           

#           perturbation case : all sectors can have a profile
            elif ( profemi == 1 ) :
                              
                altitude_int=np.array([0.,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40]) # [km]                            

            else :
                print('+++ getfinallevels +++')
                print('No profemi recognized : ', profemi)
                quit()

#   common defined grid (21 levels)
    elif ( vertintp == 'L21' ) :

        altitude_int = np.array([0.000, 0.126, 0.278, 0.454, 0.654, 0.879, 1.127, 1.398, 1.884, 2.579, 3.471, 4.548, 5.765, 6.946,8.,9.,10.,11.,12.,13.,14.,15.])

    else :
        print('+++ getfinallevels +++')
        print('No vertinp recognized = ', vertintp)
        quit()


    altitude_units ='km'
    nlev           = len(altitude_int) - 1
    altitude       = ( altitude_int[0:nlev] + altitude_int[1:nlev+1] ) / 2.

#   return structure
    data = { 'altitude'      : altitude, \
             'altitude_int'  : altitude_int, \
             'nlev'          : nlev, \
             'altitude_units' : altitude_units}

    return data
