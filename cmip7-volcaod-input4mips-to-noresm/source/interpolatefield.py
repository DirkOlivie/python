import numpy as np
import time

import getwavelengthweight

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/radiation-spectrum/source')
import readspectrum



def interpolatefield(origdata, wavelength_bnds, wavelength_units, wvl_interpolation_type, wvl_group_type):
#-------------------
    '''
    AIM
        Intepolate from origincal wavelength_bnds (in origdata) to final wavelength_bnds

        In case of 'blackbody' : T=5777 [Seinfeld and Pandis, 2006] or T = 255 [aerotab.f]


    REMARK
        as new wavelength intervals are given as [lower, upper] and no central wavelength
        I calculate central wavelength as the mean

    INPUT
        origdata              : origdata structure on original wavelength   
            [ntime, nheight, nlat, nwvl]
        wavelenght_bnds        : NEW wavelength bounds
        wavelength_units       : units in which NEW wavelengths are given
        wvl_interpolation_type : 'constant' | 'blackbody' | 'ssicdr'
        wvl_group              : 'SW' | 'LW'

    RETURN
        structure

    REMARK
        possibly extend wavelength limits !!!!

    CALLS
        readspectrum
        getwavelengthweight

    '''
#   CHECK THAT ORIGINAL DATA and NEW WAVELENGTH DEFINITION have same wavelength
#   UNITS
    if ( origdata['wavelength_units'] != wavelength_units ) :
        print('+++ interpolatefield  +++')
        print('Different wavelength units : ')
        print('original CMIP7 data : ', origdata['wavelength_units'])
        print('new wavelenths : ', wavelength_units)
        quit()

#   OBTAIN HIGH FREQUENCY SPECTRUM IN SAME WVL UNITS AS GIVEN DATA    
    if   ( wvl_group_type == 'SW' ) : temperature = 5777. ; wvl0= 100. ; wvl1=  20000. ; dwvl= 1. ; limit_wvl_units='nm' # [K] [Seinfield and Pandis, 2006, Figure 4.2]
    elif ( wvl_group_type == 'LW' ) : temperature =  255. ; wvl0=1000. ; wvl1=1000000. ; dwvl=50. ; limit_wvl_units='nm' # [K] [AeroTab, specbands.f] 
    else : 
        print('+++ interpolatefield  +++')
        print('No wvl_group_type recognized : ', wvl_group_type)
        quit()

#   MAKE UNITS OF wvl0/wvl1/dwvl EQUAL TO 
    if   ( origdata['wavelength_units'] == limit_wvl_units ) : 
        factor=1
    elif ( ( origdata['wavelength_units'] == 'um' ) and ( limit_wvl_units=='nm' ) ) : 
        factor=0.001
        limit_wvl_units='um'
    else : 
        print('+++ interpolatefield  +++')
        print('No wvl_group_type recognized : ', wvl_group_type)
        quit()

    wvl0 = wvl0 * factor
    wvl1 = wvl1 * factor
    dwvl = dwvl * factor

#   OBTAIN SPECTRUM
    if   ( wvl_interpolation_type == 'constant'  ) : spectrum = None
    elif ( wvl_interpolation_type == 'blackbody' ) : spectrum = readspectrum.readspectrum(var='BBI', origin='SP2006'           , wvlresolution=None      , wvl0=wvl0, wvl1=wvl1, dwvl=dwvl, year0=None, year1=None, temperature=temperature, prefactor=None, desired_wvl_units=origdata['wavelength_units']) 
    elif ( wvl_interpolation_type == 'ssicdr' )    : spectrum = readspectrum.readspectrum(var='SSI', origin='ClimateDataRecord', wvlresolution='standard', wvl0=None, wvl1=None, dwvl=None, year0=1850, year1=2021, temperature=None       , prefactor=None, desired_wvl_units=origdata['wavelength_units'])
    else :
        print('+++ interpolatefield  +++')
        print('No wvl_group_type recognized : ', wvl_group_type)
        quit()
       
    print('Original wavelength bounds       : ', origdata['wavelength_bnds'], origdata['wavelength_units'])    
    print('Final    wavelength bounds       : ', wavelength_bnds, wavelength_units)
    if ( spectrum != None ) : print('High resolution spectrium bounds : ', spectrum['wavelength_bnds'], spectrum['wavelength_units'])         

    time.sleep(3)

#   MINIMUM WAVELENGTH
    if ( origdata['wavelength_bnds'][0] > wavelength_bnds[0] ) :
        print('Smallest wavelength of original CMIP7 data too large: ', origdata['wavelength_bnds'][0], wavelength_bnds[0])
        origdata['wavelength_bnds'][0] = wavelength_bnds[0]
        time.sleep(3)

#   MAXIMUM WAVELENGTH
    if ( origdata['wavelength_bnds'][-1] < wavelength_bnds[-1] ) :
        print('Largest wavelength of original CMIP7 data too small : ', origdata['wavelength_bnds'][-1], wavelength_bnds[-1])
        origdata['wavelength_bnds'][-1] = wavelength_bnds[-1]
        time.sleep(3)

#   DIMENSIONS IN ORIGINAL DATA
    ntime   =     origdata['ntime']    
    nheight = len(origdata['height'])
    nlat    = len(origdata['latitude'] )
    nwvl0   = len(origdata['wavelength'])   

#
#   NEW DIMENSION
    nwvl2=len(wavelength_bnds)-1
 
#   SHAPE
#   exptected shape : ntime, nlat, nheight, nwavelenth
    if ( origdata['field'].shape != (ntime, nheight, nlat, nwvl0) ) :
        print('No correct shape')
        quit()
#
#   NEW FIELD
    newfield=np.zeros((ntime, nheight, nlat, nwvl2),dtype=float)

#
#   WAVELENGTH WEIGHTS
    weight = getwavelengthweight.getwavelengthweight(wvl_bnds0=origdata['wavelength_bnds'], wvl_bnds2=wavelength_bnds, spectrum=spectrum)

#
#   write some output to file
    asciifilename='/nird/home/olivie/code/python/cmip7-volcaod-input4mips-to-noresm/info/output/'+wvl_group_type+'_'+wvl_interpolation_type+'.txt'
    f=open(asciifilename,'w')
    for iwvl2 in range(nwvl2) :          # original wavelength
        for iwvl0 in range (nwvl0) :    # final wavelength
                if ( weight[iwvl2,iwvl0] != 0. ) :
                    f.write('iwvl2, iwvl0, weight : ')
                    f.write(str("%2.2i"% (iwvl2)))
                    f.write(' ')
                    f.write(str("%2.2i"% (iwvl0)))
                    f.write(' ')
                    f.write(str("%13.6e"% (weight[iwvl2,iwvl0])))
                    f.write('\n')


#   WRITE SOME OUTPUT
    print('WAVELENGHT WEIGHTS')
    for iwvl2 in range(nwvl2) :          # original wavelength
        print('iwvl2, sum of weight : ', iwvl2, np.sum(weight[iwvl2,:]))
 
#   APPLY INTERPOLATION WEIGHT
    for iwvl0 in range(nwvl0) :          # original wavelength
        for iwvl2 in range (nwvl2) :    # final wavelength
            newfield[:,:,:,iwvl2] =  newfield[:,:,:,iwvl2] + origdata['field'][:,:,:,iwvl0] * weight[iwvl2,iwvl0]

#   CREATE CENTRAL WAVELENGTH (based on wl0list and wl1list)
    wavelength    = np.zeros(nwvl2, dtype=float)
    wavelength[:] = 0.5 * ( wavelength_bnds[0:nwvl2]+wavelength_bnds[1:nwvl2+1] )

#   NEW DATA STRUCTUR
    newdata = {'var'   : origdata['var'], \
               'field' : newfield, \
               'units' : origdata['units'], \
#
               'latitude'       : origdata['latitude'], \
               'latitude_bnds'  : origdata['latitude_bnds'], \
               'latitude_units' : origdata['latitude_units'], \
#
               'height'       : origdata['height'], \
               'height_bnds'  : origdata['height_bnds'], \
               'height_units' : origdata['height_units'], \
#
               'wavelength'       : wavelength, \
               'wavelength_bnds'  : wavelength_bnds, \
               'wavelength_units' : origdata['wavelength_units'], \
#
               'yearlist'  : origdata['yearlist'], \
               'monthlist' : origdata['monthlist'], \
               'daylist'   : origdata['daylist'], \
               'decimalyearlist' : origdata['decimalyearlist'], \
               'ntime' : ntime}

#
#   RETURN
    return newdata
