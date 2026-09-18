import glob
import numpy as np
from netCDF4 import Dataset

import sys
#sys.path.insert(0,'/nird/home/olivie/scripts-python')
#import experimentdefinition

sys.path.insert(0,'/nird/home/olivie/scripts-python-cmip6-v2')
import getrawdirectory
import getperiodlist
import getrealm
import getvertcoordinfo
import getexpidsplit

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import calculate4dpressure
import hybnds2hy
import interp1d


def readallcmorizedfield( expid, var, year0, year1, project=None):
########################
#
    '''
    REMARK
        contains corrections for EMAC
        cl :    is in 0-1 with units "-"
                should be 0-100 with units "%"
        cl : in the filename 'cl_corrected'

    INPUT
        expid
        var
        year0
        year1

    CALLS
        readallcmorizedfield [calls recursively itself]
        getexpidsplit
#        getexpidinfo
        getvertcoordinfo
        getrawdirectory
        getrealm
        getperiodlist
        calculate4dpressure

    MODIFCICATION 
        (2025-01-28)
        (2025-05-25) 
            extension to surface layer
            extension to column burden

    '''
#
    print('+++ readallcmorizedfield +++')
    print('var      : '+var)
#
###########################
#   Ozone  partial pressure
##########################
    if ( var == 'o3_as_partpress' ) :

        data = readallcmorizedfield( expid=expid, var='o3', year0=year0, year1=year1, project=project )

        data['field'] = data['field']*data['pfull'] # partial pressure = vmr * pressure
        data['units'] = 'Pa'   
#
################################
#   Extract surface layer values
################################
    elif ( var == 'ch4_surfacelayer' \
        or var == 'o3_surfacelayer' ) :

        print('PASSING HERE ...')

#       split
        line=var.split('_')
        varorig=line[0]        

#       read original field
        origdata=readallcmorizedfield( expid=expid, var=varorig, year0=year0, year1=year1, project=project) # will include pfull
#        
        nlev=origdata['nlev']
        pfull=origdata['pfull']
        print(pfull.shape)
        if ( np.max(pfull[:,0,:,:]) >= np.max(pfull[:,nlev-1,:,:]) ) : isurface=0
        else : isurface=nlev-1
#
        data = { 'field'     : np.squeeze(origdata['field'][:,isurface,:,:]), \
                 'longitude' : origdata['longitude'], \
                 'latitude'  : origdata['latitude'], \
                 'nlon'      : origdata['nlon'], \
                 'nlat'      : origdata['nlat'], \
                 'nlev'      : 0, \
                 'units'     : origdata['units'], \
                 'yearlist'  : origdata['yearlist'], \
                 'monthlist' : origdata['monthlist'], \
                 'datelist'  : origdata['datelist'], \
                 'ntime'     : origdata['ntime']}
#
###################################
#   columnburden based on mol mol-1
###################################
    elif ( var == 'ch4_columnburden' ) : 
#
#       constants
        Rair  = 287.058
        Mwair =  28.97    # this should be Mwair !!!!!
        Nav   =   6.022e23        
#       derived var info
        if ( var == 'ch4_columnburden' ) : varorig='ch4' ; Mw=16.0406
        else :
            print('No var recognized : ', var)
            quit()

#       read original field
        OD=readallcmorizedfield( expid=expid, var=varorig, year0=year0, year1=year1, project=project) # will include pfull

#       column integration
        columnfield = np.zeros((OD['ntime'], OD['nlat'], OD['nlon']), dtype=float)

#       integration
        for ilev in range(0,OD['nlev']) :
            columnfield=columnfield + OD['field'][:,ilev,:,:] \
                                    * np.abs(OD['phalf'][:,ilev,:,:]-OD['phalf'][:,ilev+1,:,:] ) / 9.81 \
                                    * Mw / Mwair
            print('Level               : ', ilev)          
            print('Mean orig field     : ', np.mean(OD['field'][:,ilev,:,:]))
            print('Mean pressure       : ', np.mean(OD['pfull'][:,ilev,:,:])) 
            print('Mean delta pressure : ', np.mean(np.abs(OD['phalf'][:,ilev,:,:]-OD['phalf'][:,ilev+1,:,:])))


        data = { 'field'     : columnfield, \
                 'longitude' : OD['longitude'], \
                 'latitude'  : OD['latitude'], \
                 'nlon'      : OD['nlon'], \
                 'nlat'      : OD['nlat'], \
                 'nlev'      : 0, \
                 'units'     : 'kg m-2', \
                 'yearlist'  : OD['yearlist'], \
                 'monthlist' : OD['monthlist'], \
                 'datelist'  : OD['datelist'], \
                 'ntime'     : OD['ntime']}

#   columnburden based on mol/m3/s 
    elif ( var == 'ch4lossoh_columnburden' \
        or var == 'ch4losscl_columnburden' \
        or var == 'ch4losso1d_columnburden' \
        or var == 'lossch4_columnburden' ) :
#
#       constants
        Rair  = 287.058
        Mwair =  28.97    # this should be Mwair !!!!!
        Nav   =   6.022e23        
#       derived var info
        if (   var == 'ch4lossoh_columnburden'  ) : varorig='ch4lossoh'  ; Mw=16.0406 
        elif ( var == 'ch4losscl_columnburden'  ) : varorig='ch4losscl'  ; Mw=16.0406
        elif ( var == 'ch4losso1d_columnburden' ) : varorig='ch4losso1d' ; Mw=16.0406
        elif ( var == 'lossch4_columnburden'    ) : varorig='lossch4'    ; Mw=16.0406
        else :
            print('No var recognized : ', var)
            quit()

#       read original field
        OD=readallcmorizedfield( expid=expid, var=varorig, year0=year0, year1=year1, project=project) # will include pfull

#       read temperature
        T=readallcmorizedfield( expid=expid, var='ta', year0=year0, year1=year1, project=project)

        t3d=np.zeros((OD['ntime'], OD['nlev'], OD['nlat'], OD['nlon']), dtype=float)

        print('START INTERPOLATION')
        for ilon in range(0,OD['nlon']) :
            for ilat in range(0,OD['nlat']) : 
                for itime in range(OD['ntime']) :
#                   correct T-profile for 1e+19
                    t1d=T['field'][itime,:,ilat,ilon]
                    for ilev in range(T['nlev']-1,-1,-1) :
                        if ( t1d[ilev] > 1.e10 ) : t1d[ilev] = t1d[ilev+1]
#                   interpolate
                    t3d[itime,:,ilat,ilon] = interp1d.interp1d(x=T['pfull'][itime,:,ilat,ilon], \
                                                               fx=t1d[:], \
                                                               y=OD['pfull'][itime,:,ilat,ilon]) 
#       column integration
        columnfield = np.zeros((OD['ntime'], OD['nlat'], OD['nlon']), dtype=float)

#       loop over all times
        for ilev in range(0,T['nlev']) :
            print('Mean temperature    : ', np.mean(T['field'][:,ilev,:,:]))

        for ilev in range(0,OD['nlev']) :
            columnfield=columnfield + OD['field'][:,ilev,:,:] \
                                    * Rair * t3d[:,ilev,:,:] / OD['pfull'][:,ilev,:,:] \
                                    * np.abs(OD['phalf'][:,ilev,:,:]-OD['phalf'][:,ilev+1,:,:] ) / 9.81 \
                                    * Mw \
                                    * 0.001
            print('Level               : ', ilev)          
            print('Mean orig field     : ', np.mean(OD['field'][:,ilev,:,:]))
            print('Mean temperature    : ', np.mean(t3d[:,ilev,:,:]))
            print('Mean pressure       : ', np.mean(OD['pfull'][:,ilev,:,:])) 
            print('Mean delta pressure : ', np.mean(np.abs(OD['phalf'][:,ilev,:,:]-OD['phalf'][:,ilev+1,:,:])))


        data = { 'field'     : columnfield, \
                 'longitude' : OD['longitude'], \
                 'latitude'  : OD['latitude'], \
                 'nlon'      : OD['nlon'], \
                 'nlat'      : OD['nlat'], \
                 'nlev'      : 0, \
                 'units'     : 'kg m-2 s-1', \
                 'yearlist'  : OD['yearlist'], \
                 'monthlist' : OD['monthlist'], \
                 'datelist'  : OD['datelist'], \
                 'ntime'     : OD['ntime']}

#################################
#   columnburden below tropopause  SHOULD BE DEVELOPED !
#################################
    elif ( var == 'ch4_columnburden_belowtropopause' ) : 

#       split  
        line=var.split('_')
        varorig=line[0]
#
############
#   Standard
############
    else :
#
        nmonth=12
#
#       obtain the project
#        expidinfo=experimentdefinition.getexpidinfo(expid=expid)
#        project = expidinfo['project']        
#       model   = expidinfo['model']
        expidsplitinfo=getexpidsplit.getexpidsplit(expid=expid)
        model=expidsplitinfo['model']
        

        print('model (readallcmorizedfield-1) : ', model)

#       vertical coordinfon
        vinfo = getvertcoordinfo.getvertcoordinfo(model=model)
        vtype=vinfo['vtype']
        cp0=vinfo['cp0']
        cps=vinfo['cps']
        chyam=vinfo['chyam']       # nlev
        chybm=vinfo['chybm']
        chyai=vinfo['chyai']       # nlev +1  
        chybi=vinfo['chybi']
        chyabnds=vinfo['chyabnds'] # nlev x2
        chybbnds=vinfo['chybbnds']

#       directory
        directory=getrawdirectory.getrawdirectory(expid=expid,var=var,project=project,freqfile='monthly')
        print('model (readallcmorizedfield-2) : ', model)
        realm=getrealm.getrealm(var=var,freqfile='monthly',model=model)

#list of all files  
        fvar = var
        if ( model == 'DLR-EMAC' and var == 'cl' ) : fvar='cl_corrected'
 
        filelist=glob.glob(directory+'/'+fvar+'_'+realm+'_*[0-9].nc')
        filelist.sort()

# list of all periods
        periodlist=getperiodlist.getperiodlist(expid, var, project, freqfile='monthly')

# loop over all periods
        first=True

        for iperiod in range(0,periodlist['nperiod']) :

            period=periodlist['periodlist'][iperiod]
            year0file=periodlist['year0list'][iperiod]
            year1file=periodlist['year1list'][iperiod]

            if ( year0 <= year1file and year1 >= year0file ) :

# read netcdfi file
                filelist=glob.glob(directory+'/'+fvar+'_'+realm+'_*'+period+'.nc')
                nc_f=filelist[0]

                print(nc_f)
                nc_fid= Dataset(nc_f, 'r')
    
# reading actual field
                print('... before ...')
                tmpfieldlist=np.squeeze(np.array(nc_fid.variables[var][:]))
                if ( model == 'DLR-EMAC' and var == 'cl' ) :
                    tmpfieldlist=tmpfieldlist*100.

                print('... after ...')


# only for first file
                if ( first ) :   

                    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
                    lons=np.array(nc_fid.variables['lon'][:])  # longitudes

                    if ( model == 'DLR-EMAC' and var == 'cl' ) : 
                        units='%'
                    elif ( model == 'CESM2' and var == 'cl' ) :
                        units='%'
                    elif ( model == 'CESM2' and var == 'ta' ) :
                        units='K'
                    elif ( model == 'CESM2' and var == 'o3' ) :
                        units='mol mol-1'
                    elif ( model == 'CESM2' and var == 'hus' ) :
                        units='kg kg-1'
                    else : 
                        print('model : ', model)
                        print('var   : ', var)

                        units=nc_fid.variables[var].units

                    ndim=tmpfieldlist.ndim
                    nlat=len(lats)
                    nlon=len(lons)

                    dimensions = nc_fid.variables[var].dimensions   # ('MT', 'Depth', 'Y', 'X')
                    shape = nc_fid.variables[var].shape             # (1, 10, 850, 712) 

# 3d fields
                    if ( ndim == 4 ) :

# distinguish between model levels (lev as coordinate) and 19 pressure levels
                        if ( 'lev' in dimensions ) :

                            levs=np.array(nc_fid.variables['lev'][:]) # model levels 
                            nlev=len(levs)

                            # p0
                            if ( cp0   != '' ) : p0   = np.array(nc_fid.variables[cp0][:])   
                            else               : p0   = 1. 
                            # hyam / hybm
                            if ( chyam != '' ) : hyam = np.array(nc_fid.variables[chyam][:]) # hyam
                            if ( chybm != '' ) : hybm = np.array(nc_fid.variables[chybm][:]) # hybm
                            # hyai / hybi
                            if ( chyai != '' ) : hyai = np.array(nc_fid.variables[chyai][:]) # hyai
                            if ( chybi != '' ) : hybi = np.array(nc_fid.variables[chybi][:]) # hybi
                            # hyabnds / hybbnds
                            if ( chyabnds != '' ) : 
                                hyabnds = np.array(nc_fid.variables[chyabnds][:]) # hyabnds
                                hyai = hybnds2hy.hybnds2hy(hyabnds)
                            if ( chybbnds != '' ) : 
                                hybbnds = np.array(nc_fid.variables[chybbnds][:]) # hybbnds
                                hybi = hybnds2hy.hybnds2hy(hybbnds)    

                            # units_ps
                            if ( cps   != '' ) : units_ps = nc_fid.variables[cps].units      # units of surface pressure

                        elif ( 'plev' in dimensions ) :

                            levs=np.array(nc_fid.variables['plev'][:])   # 19 pressure levels
                            nlev=len(levs) 
                            print(model)
                            if ( model == 'NorESM2-LM' \
                              or model == 'CESM2' ) :
                                units_plev='Pa'
                            else : 
                                units_plev = nc_fid.variables['plev'].units  # units of 19 pressure levels

                        else :
                            print('No vertical dimension recognized')
                            quit()
#
# reading pressure field
                if ( ndim == 4 and vtype == 'hybrpress' and 'lev' in dimensions ) : tmppslist=np.squeeze(np.array(nc_fid.variables['ps'][:]))

# generating timefield
                ntime=(year1file-year0file+1)*nmonth

                tmpyearlist=np.zeros((ntime), dtype=int)
                tmpmonthlist=np.zeros((ntime), dtype=int)
                tmpdatelist=np.zeros((ntime),dtype='<U7')   # strings of max 7 characters !!!
                for itime in range(0,ntime):
                    year = year0file + itime // nmonth
                    month = itime%nmonth + 1 # module

                    tmpyearlist[itime]  = year
                    tmpmonthlist[itime] = month
        
                    cyear=str("%4.4i"% (year))
                    cmonth= str("%2.2i"% (month))

                    tmpdatelist[itime] = cyear+'-'+cmonth

                nc_fid.close # close file
#
# concatenate 
                if ( first ) :
                    fieldlist=tmpfieldlist
                    if ( ndim == 4 and vtype == 'hybrpress' and 'lev' in dimensions ) : pslist = tmppslist # ps
                    yearlist=tmpyearlist
                    monthlist=tmpmonthlist
                    datelist=tmpdatelist
                else : 
                    fieldlist=np.concatenate( (fieldlist,tmpfieldlist), axis=0 ) 
                    if ( ndim == 4 and vtype == 'hybrpress' and 'lev' in dimensions ) : pslist=np.concatenate( (pslist,tmppslist), axis=0 ) # ps
                    yearlist=np.concatenate(  (yearlist,tmpyearlist)           )
                    monthlist=np.concatenate( (monthlist,tmpmonthlist)         )
                    datelist=np.concatenate(( datelist,tmpdatelist)            )

                first = False

#   read also phalf and pfull / calculate from ps  
        ntime=len(datelist) 
        if ( ndim == 4 and ( var != 'phalf' and var != 'pfull' ) ) : 

            if ( 'lev' in dimensions ) : # model levels 

                if ( vtype == 'hybrheight' ) :                     # UKESM  
                    pfull=readallcmorizedfield( expid=expid, var='pfull',year0=year0, year1=year1, project=project)   # read directly pfull-field
                    field_pfull=pfull['field']
                    units_pfull=pfull['units']

#                   phalf=readallcmorizedfield( expid=expid, var='phalf',year0=year0, year1=year1)
                elif (vtype == 'hybrpress' ) :                    
#                    ps=readallcmorizedfield( expid=expid, var='ps',year0=year0, year1=year1, project=project)   # read directly ps-field                     

                    field_pfull=calculate4dpressure.calculate4dpressure(p0=p0,ps=pslist,hya=hyam,hyb=hybm)  # calculate pfull-field based on ps # before ps = pslist                 
                    units_pfull=units_ps

                    field_phalf=calculate4dpressure.calculate4dpressure(p0=p0,ps=pslist,hya=hyai,hyb=hybi)  # calculate pfull-field based on ps # before ps = pslist
                    units_phalf=units_ps

                else :
                    print('No vtype recognized : ', vtype)
                    quit() 

            elif ( 'plev' in dimensions ) : 
                field_pfull=np.zeros((ntime,nlev,nlat,nlon),dtype=float)
                for ilev in range(nlev) :
                    field_pfull[:,ilev,:,:] = levs[ilev]

                units_pfull=units_plev
            else : 
                print('No vertical dimension recognized')
                quit()

#   data selection between year0 and year1
        isubset = ( yearlist >= year0 ) * ( yearlist <= year1)

#       reduce extent 
        if (   ndim == 3 ) : fieldlist = fieldlist[isubset,:,:]           # fiedlist
        elif ( ndim == 4 ) : 
            fieldlist = fieldlist[isubset,:,:,:] 
            if ( vtype == 'hybrpress' and 'lev' in dimensions ) :
                field_pfull = field_pfull[isubset,:,:,:]                
                field_phalf = field_phalf[isubset,:,:,:]                
        else :  
               print('No dimension size recognized : ', ndim)
               quit()
        yearlist = yearlist[isubset]                                      # yearlist
        monthlist = monthlist[isubset]                                    # monthlist
        datelist= datelist[isubset]                                       # datelist  

#   return data               
        data = { 'field'     : fieldlist, \
                 'longitude' : lons, \
                 'latitude'  : lats, \
                 'nlon'      : nlon, \
                 'nlat'      : nlat, \
                 'nlev'      : 0, \
                 'units'     : units, \
                 'yearlist'  : yearlist, \
                 'monthlist' : monthlist, \
                 'datelist'  : datelist, \
                 'ntime'     : len(datelist)}
#   in case of 4d data
        if( ndim == 4 ) : 
            data.update({'nlev'      : nlev})

#   in case of 4d data (not 'phalf', not 'pfull')    
        if ( ndim == 4 and ( var != 'phalf'and var != 'pfull' ) ) :
            data.update({ \
#               'pfull'     : field_pfull[isubset,:,:,:], \ # isubset selection not anymore neededd
                'pfull'     : field_pfull[:,:,:,:], \
                'units_pfull' : units_pfull})
#            commented out because UKESM
#            if ( 'lev' in dimensions ) : # not to be done if plev19
#                data.update({ \
##                   'phalf'     : field_phalf[isubset,:,:,:], \ # isubset selection not anymore needed
#                    'phalf'     : field_phalf[:,:,:,:], \
#                    'units_phalf' : units_phalf})
#   
    print('--- readallcmorizedfield ---')
# 
    return data    
