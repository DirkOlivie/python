import numpy as np


def getemissionprofile(activity, sector):
#---------------------
    '''
    MODIFCATIONS
	    (2019-06-30) added sector 'FORE' and 'GRAS' (from scenarios)
		    SHOULD BE IMPROVED !!!!
	    (2021-02-23) perturbations for emissionMIP passed via commonblock

    CALLED BY

    CALLS
    '''
#---------------------------------------------------------------------------------------------
#
#   biomass burning
    if ( activity == 'bb' ) :

        altitude_int=[0.,0.1,0.5,1.,2.,3.,6.] # [km]

        if (   sector == 'AGRI' ) : profileweight = [100.,0.,0.,0.,0.,0.]
        elif ( sector == 'PEAT' ) : profileweight = [100.,0.,0.,0.,0.,0.] # assumed the same as AGRI

        elif ( sector == 'SAVA' ) : profileweight = [20.,40.,40.,0.,0.,0.]
        elif ( sector == 'DEFO' ) : profileweight = [20.,40.,40.,0.,0.,0.]

        elif ( sector == 'TEMF' ) : profileweight = [20.,20.,20.,40.,0.,0.]

        elif ( sector == 'BORF' ) : profileweight = [10.,10.,20.,20.,40.,0.]
#
#       new for scenarios [SHOULD BE IMPROVED]
        elif ( sector == 'FORE' ) :  profileweight = [20.,20.,20.,40.,0.,0.] # same as 'TEMF'
        elif ( sector == 'GRAS' ) :  profileweight = [20.,40.,40.,0.,0.,0.]  # same as 'SAVA'

        else :
            print('No sector recognized : ', sector)
            quit() 
            
#   anthropogenic  
    elif ( activity == 'anthroprof' ) :

        altitude_int = [0.,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40] # [km]

#       profemi = getvalue_commonblock(descriptor='profemi')
        profemi = 0

#    standard case
        if ( profemi == 0 ) :

            if (   sector == 'ENE' ) : profileweight = [0.,0.,0.,1.,1.,1.,1.,0.]
            elif ( sector == 'IND' ) : profileweight = [0.,0.,0.,1.,1.,1.,1.,0.]
            else :
                print('No sector recognized : ', sector)
                quit()

        elif ( profemi == 1 ) :

            if (   sector == 'AGR' ) : profileweight =[0.,0.,0.,0.,1.,1.,1.,1.] # 200-400 m
            elif ( sector == 'ENE' ) : profileweight =[0.,0.,0.,0.,1.,1.,1.,1.]
            elif ( sector == 'IND' ) : profileweight =[0.,0.,0.,0.,1.,1.,1.,1.]
            elif ( sector == 'TRA' ) : profileweight =[0.,0.,0.,0.,1.,1.,1.,1.]
            elif ( sector == 'DOM' ) : profileweight =[0.,0.,0.,0.,1.,1.,1.,1.]
            elif ( sector == 'SOL' ) : profileweight =[0.,0.,0.,0.,1.,1.,1.,1.]
            elif ( sector == 'WST' ) : profileweight =[0.,0.,0.,0.,1.,1.,1.,1.]
            elif ( sector == 'SHP' ) : profileweight =[0.,0.,1.,1.,1.,1.,0.,0.] # 100-300 m
            else :
                print('+++ getemissionprofile +++')
                print('No sector recognized : ', sector)
                quit()

        else :
            print('+++ getemissionprofile +++')
            print('No profemi recognized (should be 0 or 1) = ', profemi)
            quit()

    else :
        print('+++ getemissionprofile +++')
        print('No activity recognized : ', activity)
        quit()        

#   check
    if ( len(profileweight) != ( len(altitude_int) - 1 ) ) :
        print('+++ getemissionprofile +++')
        print('Length of profileweight and altitude_int not compatible : ')
        print('profileweight : ', len(profileweight))
        print('altitude_int  : ', len(altitude_int) - 1 )
        quit()

#   conversion to numpy array
    altitude_int=np.array(altitude_int)
    profileweight=np.array(profileweight)        

#   
    nlev=len(altitude_int) - 1
    altitude = ( altitude_int[0:nlev]+ altitude_int[1:nlev+1] ) / 2.
    altitude_units= 'km'

#   normalizing the weights
    profileweight=profileweight/np.sum(profileweight) # normalizing to 1
  
#   check
    if ( len(profileweight) != len(altitude) ) :
        print('+++ getemissionprofile +++')
        print('Length of profileweight and altitude not compatible : ')
        print('profileweight : ', len(profileweight))
        print('altitude      : ', len(altitude))
        quit()

#   altitude        
    data = {'altitude'       : altitude, \
            'altitude_int'   : altitude_int, \
            'altitude_units' : 'km', \
            'profileweight'  : profileweight,  \
            'nlev'           : nlev }
#
    return data



  




