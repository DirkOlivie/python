import numpy as np
import os
from netCDF4 import Dataset

import experimentdefinition
import calculatesinglefield_sad_cesm2
import calculatesinglefield_sad_noresm2
import calculatesinglefield_conc_from_mmr
import calculatesinglefield_conc_from_vmr
import calculatesinglefield_vmr_from_layermass
import calculatesinglefield_vmr_from_mmr
import calculatesinglefield_partpress_from_vmr

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getbasicexpidname

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getgridtype


def readsingleh0field( expid, var, date):
#--------------------
    '''
    REMARK
        tempeatures [K] -> converted to [] : NOT ANYMORE
        conversion : molecules cm-3 -> mol mol-1

    MODIFCICATION 
        (2022-07-11) : no conversion of temperature from [K] to [C]
        (2023-10-20) : introduced possibility for basic experimentname
        (2024-10-02) : introduced possibility to read clim files when 12 months in one file (defined by clmh0)

        (2026-09-07) : possibility of irregular grid
                       added lat,lon to be extracted during cdo commands

    '''







    print('+++ readsingleh0field +++')
    print('date : '+date)
    print('var  : '+var)
    print('--- readsingleh0field ---')
#
#   basic experiment name    
    basicexpid=getbasicexpidname.getbasicexpidname(expid=expid, date=date)
    
#   date -> year and month
    line=date.split('-')    # split yyyy-mm
    yyyy  =     line[0]            # string  
    year  = int(line[0])
    month = int(line[1])      # integer

#   SOME SPECIAL VARIABLES
    if ( var == 'sad_cesm2_dry_a1' \
      or var == 'sad_cesm2_dry_a2' \
      or var == 'sad_cesm2_dry_a3' \
      or var == 'sad_cesm2_dry_a4' \
      or var == 'sad_cesm2_wet_a1' \
      or var == 'sad_cesm2_wet_a2' \
      or var == 'sad_cesm2_wet_a3' \
      or var == 'sad_cesm2_wet_a4' ) : 
         
        data = calculatesinglefield_sad_cesm2.calculatesinglefield_sad_cesm2( expid=basicexpid, var=var, date=date)
#   SOME SPECIAL VARIABLES        
    elif ( var == 'sad_noresm2_dry_m01' \
        or var == 'sad_noresm2_dry_m02' \
        or var == 'sad_noresm2_dry_m04' \
        or var == 'sad_noresm2_dry_m05' \
        or var == 'sad_noresm2_dry_m06' \
        or var == 'sad_noresm2_dry_m07' \
        or var == 'sad_noresm2_dry_m08' \
        or var == 'sad_noresm2_dry_m09' \
        or var == 'sad_noresm2_dry_m10' \
        or var == 'sad_noresm2_dry_m12' \
        or var == 'sad_noresm2_dry_m14' ) :

        data = calculatesinglefield_sad_noresm2.calculatesinglefield_sad_noresm2( expid=basicexpid, var=var, date=date)
#   SOME SPECIAL VARIABLES        
    elif ( var == 'num_a1_as_concentration' \
        or var == 'num_a2_as_concentration' \
        or var == 'num_a3_as_concentration' \
        or var == 'num_a4_as_concentration' \
        \
        or var == 'mmr_BC_as_concentration' \
        or var == 'mmr_OM_as_concentration' \
        or var == 'mmr_SULFATE_as_concentration' \
        or var == 'mmr_DUST_as_concentration' \
        or var == 'mmr_SALT_as_concentration' ) :
        data = calculatesinglefield_conc_from_mmr.calculatesinglefield_conc_from_mmr( expid=basicexpid, var=var, date=date)
#   SOME SPECIAL VARIABLES        
    elif ( var == 'CHBR3_as_concentration' \
        or var == 'SO2_as_concentration'   \
        or var == 'H2SO4_as_concentration' ) :
        data = calculatesinglefield_conc_from_vmr.calculatesinglefield_conc_from_vmr( expid=basicexpid, var=var, date=date)
#   SOME SPECIAL VARIABLES
    elif ( var == 'm_CO2_c_as_vmr' \
        or var == 'm_CH4_c_as_vmr' \
        or var == 'm_N2O_c_as_vmr' \
        or var == 'm_CFC11_c_as_vmr' \
        or var == 'm_CFC11STAR_c_as_vmr' \
        or var == 'm_CFC12_c_as_vmr' \
        or var == 'm_O3_c_as_vmr' \
        or var == 'm_ozone_c_as_vmr' \
          \
        or var == 'm_CO2_c_as_vmr_drytest' \
        or var == 'm_CH4_c_as_vmr_drytest' \
        or var == 'm_N2O_c_as_vmr_drytest' \
        or var == 'm_CFC11_c_as_vmr_drytest' \
        or var == 'm_CFC11STAR_c_as_vmr_drytest' \
        or var == 'm_CFC12_c_as_vmr_drytest' \
        or var == 'm_O3_c_as_vmr_drytest ' \
        or var == 'm_ozone_c_as_vmr_drytest' ) : 
        data = calculatesinglefield_vmr_from_layermass.calculatesinglefield_vmr_from_layermass( expid=basicexpid, var=var, date=date)
#   SOME SPECIAL VARIABLES
    elif ( var == 'O3_as_partpress' \
        or var == 'ozone_as_partpress' \
        or var == 'ozone_extclim_as_partpress' \
        or var == 'm_O3_c_as_vmr_as_partpress' \
        or var == 'm_ozone_c_as_vmr_as_partpress' \
        or var == 'SO2_as_partpress' \
        or var == 'H2SO4_as_partpress' ) :
        data = calculatesinglefield_partpress_from_vmr.calculatesinglefield_partpress_from_vmr( expid=basicexpid, var=var, date=date)
#   TROPOSPHERIC COLUMN
    elif ( var == 'O3_as_tropcolumn' \
        or var == 'O3_as_stratcolumn' \
        or var == 'O3_as_totalcolumn' ) :
        data = calculatesinglefield_column.calculatesinglefield_column( expid=basicexpid, var=var, date=date)
#   SCALING NEEDED
    elif ( var == 'CO2_as_vmr' \
        or var == 'CH4_as_vmr' \
        or var == 'N2O_as_vmr' ) :
        data = calculatesinglefield_vmr_from_mmr.calculatesinglefield_vmr_from_mmr(expid=basicexpid, var=var, date=date)
#   STANDARD VARIABLES
    else :
#       experiment info
        expidinfo=experimentdefinition.getexpidinfo(expid=basicexpid)
        subdir=expidinfo['subdir']
        cexpid=expidinfo['cexpid'] # experiment you read (can be different from experiment you write)
        model=expidinfo['model']
        clmh0=expidinfo['clmh0']

#       h0 / h0a / h0i in filename
        if ( model == 'NorESM1' or model == 'NorESM2' or model == 'CESM2' ) :
            h0version='h0'
        elif ( model == 'NorESM2.5' or model == 'CESM2.5' ) :
            h0version='h0a'

#       clm or cam data
        if ( var == 'FSNO' \
          or var == 'MEG_isoprene' \
          or var == 'NPP' \
          or var == 'SOILWATER_10CM' \
          or var == 'TSA' \
          or var == 'TLAI'\
          or var == 'FCH4' ) :
            realm='lnd'
            modelversion='clm2'
        else :
            realm='atm'
            modelversion='cam'
    
#       NEW METHOD
        if ( 1 == 1 ) :

#           original filename
            cvar=str(var)
            if ( realm == 'lnd' and ( clmh0 == 'annual' or ( clmh0 == 'monthlyuntil1700' and year >= 1701 ) ) ) :
                shortfilename=cexpid+'.'+modelversion+'.'+h0version+'.'+yyyy+'-02-01-00000.nc'
            else :
                shortfilename=cexpid+'.'+modelversion+'.'+h0version+'.'+date+'.nc'  

#           original file       
            nc_f_orig=subdir+'/'+cexpid+'/'+realm+'/hist/'+shortfilename 

#           temporary directory
            dir='/scratch/olivie/tmp-hist/'+cexpid
            if ( not os.path.isdir(dir) ) : os.mkdir(dir)

            dir_var = dir+'/'+cvar
            dir_t   = dir+'/'+'T'
            dir_ps  = dir+'/'+'PS'

#           create new directories
            if ( not os.path.isdir(dir_var) ) : os.mkdir(dir_var)
            if ( not os.path.isdir(dir_t)   ) : os.mkdir(dir_t)
            if ( not os.path.isdir(dir_ps)  ) : os.mkdir(dir_ps)

#           temporary files
            nc_f_var = dir_var+'/'+cvar+'.'+shortfilename 
            nc_f_t   = dir_t  +'/'+'T' +'.'+shortfilename
            nc_f_ps  = dir_ps +'/'+'PS'+'.'+shortfilename

#
            print('nc_f_var : ', nc_f_var)
            print('nc_f_t   : ', nc_f_t)
            print('nc_f_ps  : ', nc_f_ps)

#            if ( not os.path.isfile(nc_f_var) ) : os.system('cdo select,name='+cvar                    +' '+nc_f_orig+' '+nc_f_var)
#            if ( not os.path.isfile(nc_f_t  ) ) : os.system('cdo select,name='+'T,hyam,hybm,hyai,hybi' +' '+nc_f_orig+' '+nc_f_t  )
#            if ( not os.path.isfile(nc_f_ps ) ) : os.system('cdo select,name='+'PS'+' +select,name=P0' +' '+nc_f_orig+' '+nc_f_ps )
#           2026-09-07 : added lat,lon,area
            if ( model == 'NorESM1' or model == 'NorESM2' or model == 'CESM2' ) :
                extralist_3d_latlon = 'hyam,hybm,hyai,hybi,time,time_bnds,lat,lon'
                extralist_2d_latlon =                  'P0,time,time_bnds,lat,lon'
            elif ( model == 'NorESM2.5' or model == 'CESM2.5' ) :
                extralist_3d_latlon = 'hyam,hybm,hyai,hybi,time,lat,lon'
                extralist_2d_latlon =                     'time,lat,lon'

            extralist_3d_irregular = extralist_3d_latlon + ',area'
            extralist_2d_irregular = extralist_2d_latlon + ',area'

#
            if ( not os.path.isfile(nc_f_var ) ) : 
                gridtype=getgridtype.getgridtype(filename=nc_f_orig)
                if   ( gridtype == 'latlon'    ) : extralist_3d = extralist_3d_latlon
                elif ( gridtype == 'irregular' ) : extralist_3d = extralist_3d_irregular
                else : print('+++ readsingleh0field +++') ; print('No gridtype recognized : ', gridtype), quit()  
                os.system('ncrcat -v '+cvar+','+extralist_3d+' '+nc_f_orig+' -O '+nc_f_var)
            if ( not os.path.isfile(nc_f_t   ) ) : 
                gridtype=getgridtype.getgridtype(filename=nc_f_orig)
                if   ( gridtype == 'latlon'    ) : extralist_3d = extralist_3d_latlon
                elif ( gridtype == 'irregular' ) : extralist_3d = extralist_3d_irregular
                else : print('+++ readsingleh0field +++') ; print('No gridtype recognized : ', gridtype), quit()
                os.system('ncrcat -v T,'       +extralist_3d+' '+nc_f_orig+' -O '+nc_f_t)
            if ( not os.path.isfile(nc_f_ps  ) ) : 
                gridtype=getgridtype.getgridtype(filename=nc_f_orig)
                if   ( gridtype == 'latlon'    ) : extralist_2d = extralist_2d_latlon
                elif ( gridtype == 'irregular' ) : extralist_2d = extralist_2d_irregular
                else : print('+++ readsingleh0field +++') ; print('No gridtype recognized : ', gridtype), quit()
                os.system('ncrcat -v PS,'      +extralist_2d+' '+nc_f_orig+' -O '+nc_f_ps)

#           read from variable file
            nc_fid= Dataset(nc_f_var, 'r')

            lats=np.array(nc_fid.variables['lat'][:])  # latitudes
            lons=np.array(nc_fid.variables['lon'][:])  # longitudes
            field=np.squeeze(np.array(nc_fid.variables[var][:]))
            if ( realm == 'lnd' and ( clmh0 == 'annual' or ( clmh0 == 'monthlyuntil1700' and year >= 1701 ) ) ) :
                field=field[month-1,:,:]
            units=nc_fid.variables[var].units

# 
#           gridtype       
            dimlist=nc_fid.dimensions.keys()
            if   ( 'ncol' in dimlist ) : gridtype='irregular' ; area = 6370e+3 * 6370e+3 * np.squeeze(np.array(nc_fid.variables['area'][:])) # area [sums up to 4*pi] ; areawt [sums up to 1]
            else                       : gridtype='latlon'    ; area = areafraction.areafraction(latitude=lats, longitude=lons, outputtype='area', region='global')


            ndim=field.ndim
            nlat=len(lats)
            nlon=len(lons)

            nc_fid.close # close variable file
#
#           vertical information
            if ( ( ndim==3 and gridtype == 'latlon') \
              or ( ndim==2 and gridtype == 'irregular' ) ) :

#               read from PS file
                nc_fid= Dataset(nc_f_ps, 'r') # open the PS file

                ps=np.squeeze(np.array(nc_fid.variables['PS'][:])) # surface pressure

                if ( model == 'NorESM2.5' or model == 'CESM2.5' ) :
                    print('p0 is not read (probably not in file)')
                    p0=100000.
                    units_p0='Pa'
                else :
                    p0=np.array(nc_fid.variables['P0'][:]) # reference pressure 
                    units_p0=nc_fid.variables['P0'].units

                units_ps=nc_fid.variables['PS'].units

                nc_fid.close # close ps file

#               read from T file
                nc_fid= Dataset(nc_f_t, 'r') # open the T file
                hyam=np.array(nc_fid.variables['hyam'][:]) # hyam
                hybm=np.array(nc_fid.variables['hybm'][:]) # hybm
                hyai=np.array(nc_fid.variables['hyai'][:]) # hyam
                hybi=np.array(nc_fid.variables['hybi'][:]) # hybm
                ta=np.squeeze(np.array(nc_fid.variables['T'][:]))

                nlev = len(hyam)

                nc_fid.close # close T file

#       OLD METHOD
        if ( 0 == 1 ) :

#           read netcdf file
            if ( realm == 'lnd' and ( clmh0 == 'annual' or ( clmh0 == 'monthlyuntil1700' and year >= 1701 ) ) ) :
                nc_f=subdir+'/'+cexpid+'/'+realm+'/hist/'+cexpid+'.'+modelversion+'.'+h0version+'.'+yyyy+'-02-01-00000.nc'
            else :
                nc_f=subdir+'/'+cexpid+'/'+realm+'/hist/'+cexpid+'.'+modelversion+'.'+h0version+'.'+date+'.nc'
            print(nc_f)

#           open file
            nc_fid= Dataset(nc_f, 'r')
    
            lats=np.array(nc_fid.variables['lat'][:])  # latitudes
            lons=np.array(nc_fid.variables['lon'][:])  # longitudes
            field=np.squeeze(np.array(nc_fid.variables[var][:]))
            if ( realm == 'lnd' and ( clmh0 == 'annual' or ( clmh0 == 'monthlyuntil1700' and year >= 1701 ) ) ) :
                field=field[month-1,:,:]
            units=nc_fid.variables[var].units
            ndim=field.ndim
            nlat=len(lats)
            nlon=len(lons)
    
            if ( ndim==3 ) : 
    
                ps=np.squeeze(np.array(nc_fid.variables['PS'][:])) # surface pressure
                hyam=np.array(nc_fid.variables['hyam'][:]) # hyam
                hybm=np.array(nc_fid.variables['hybm'][:]) # hybm
                hyai=np.array(nc_fid.variables['hyai'][:]) # hyam
                hybi=np.array(nc_fid.variables['hybi'][:]) # hybm
                ta=np.squeeze(np.array(nc_fid.variables['T'][:]))
   

                if ( model == 'NorESM2.5' or model == 'CESM2.5' ) :
                    print('p0 is not read (probably not in file)')
                    p0=100000.
                    units_p0='Pa' 
                else :
                    p0=np.array(nc_fid.variables['P0'][:]) # reference pressure 
                    units_p0=nc_fid.variables['P0'].units
    
                units_ps=nc_fid.variables['PS'].units
    
                nlev = len(hyam)
    
#           close the file
            nc_fid.close
#
#       put undefined values (over ocean) to 0 for land model
        if ( realm == 'lnd' ) : field=np.where(field > 1.e+30, 0., field)
    
#       conversion temperature : K -> C : REMOVED (2022-07-11)
#       if ( units == 'K') : 
#           units='C'
#           field = field - 273.16 
    
#       lacking units for OH_bef, OH_aft, NO3_bef, NO3_aft
        if ( ( var == 'OH_bef' \
            or var == 'OH_aft' \
            or var == 'NO3_bef' \
            or var == 'NO3_aft' )  
           and units == 'unit' ) : units = 'molecules cm-3'
#
#       lacking units for N_AER (assumed to be #/cm3)
        if ( var == 'N_AER' and units == 'unitless' ) :         
           units='m-3'
           field=field*1.e6         

#       conversion molecules cm-3 -> mol mol-1
        if ( units == 'molecules cm-3' ) :       
    
            Rair = 287.058  #
            Mwair = 0.02897 # kg mol-1
            Nav = 6.022e23  # molecules mol-1
    
            for ilev in range(nlev) : 
   

                if ( grid == 'latlon' ) :   
                    pressure = hyam[ilev] * p0 + hybm[ilev] * ps[:,:] # mid-level pressure
                    density  = pressure / Rair / ta[ilev,:,:]  * 1. / Mwair    *    Nav          * 1.e-6       
#                   density [air molecules/cm3] :  [kg/m3]               * [mol/kg]      * [molecules/mol] * [m3/cm3] 
    
                    field[ilev,:,:] = field[ilev,:,:] / density[:,:]  # mixing ratio [mol/mol] : [molecules/cm3] / [molecules/cm3]
           
                elif ( grid == 'irregular' ) :   
                    pressure = hyam[ilev] * p0 + hybm[ilev] * ps[:] # mid-level pressure
                    density  = pressure / Rair / ta[ilev,:]  * 1. / Mwair    *    Nav          * 1.e-6       
#                   density [air molecules/cm3] :  [kg/m3]               * [mol/kg]      * [molecules/mol] * [m3/cm3] 
    
                    field[ilev,:] = field[ilev,:] / density[:]  # mixing ratio [mol/mol] : [molecules/cm3] / [molecules/cm3]
           
            units='mol mol-1'

#       data            
        data = { 'field'     : field, \
                 'longitude' : lons, \
                 'latitude'  : lats, \
                 'nlon'      : nlon, \
                 'nlat'      : nlat, \
                 'units'     : units, \
                 'gridtype'  : gridtype, \
                 'area'      : area, \
                 'area_units': 'm2'}  
    
        if ( ( ndim == 3 and gridtype == 'latlon' ) \
          or ( ndim == 2 and gridtype == 'irregular' ) ) :
            data.update({   
                 'p0'        : p0, \
                 'ps'        : ps, \
                 'hyai'      : hyai, \
                 'hybi'      : hybi, \
                 'hyam'      : hyam, \
                 'hybm'      : hybm, \
                 'units_ps'  : units_ps, \
                 'units_p0'  : units_p0, \
                 'nlev'      : nlev})
#   
    print('--- readsingleh0field ---')
# 
    return data    
