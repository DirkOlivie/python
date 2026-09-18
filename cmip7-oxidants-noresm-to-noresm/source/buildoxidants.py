import os
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc

import getoxidantcomponents
import readmeanfieldoxidants

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc
import daysince

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

#
def buildoxidants(bctype, specieslist, expiddescriptionlist, version, overwrite):
#-------------
    '''
    REMARK

    AIM 

    INPUT
        bctype      : 'oxidants' (type of
        specieslist : 'vmro3'
        expiddescriptionlist : 
        version
        overwrite : True | False

    CALLED BY
	    buildoxidantsloop2

    CALLS
	    readnc
 	    daysince
   ''' 
#
    camversion = 'cam'
    h0version  = 'h0'
#
    calendar   = 'noleap'
    time_units = 'days since 1850-01-01'

    if   ( time_units == 'days since 0000-01-01' ) : refdate=     101
    elif ( time_units == 'days since 1750-01-01' ) : refdate=17500101
    elif ( time_units == 'days since 1850-01-01' ) : refdate=18500101
    else :
        print('+++ buildoxidants +++')
        print('No time_units recognized : ', time_units)
        quit()
#
    if ( bctype != 'oxidants' \
     and bctype != 'ozone' \
     and bctype != 'emish2o' ) :
        print('+++  +++')
        print('No bctype (boundary condition type) recognized : ', bctype)
        quit()

    nspecies = len(specieslist)
#
#   I. PERIOD
#------------
#   period -> yearlist
    nyear=len(expiddescriptionlist)
    yearlist=np.zeros(nyear, dtype=int)
    for iyear in range(0,nyear) :
        yearlist[iyear] = int(expiddescriptionlist[iyear]['year'])
#
#
#   II. READ FROM 
#-----------------
    expidinfo = experimentdefinition.getexpidinfo(expid=expiddescriptionlist[0]['expid'])    # taken the [0]th experiment   
    filename  = expidinfo['subdir']+'/'+expidinfo['cdir']+'/atm/hist/'+expidinfo['cexpid']+'.'+camversion+'.'+h0version+'.'+str("%4.4i"% (expidinfo['year1']))+'-01.nc' # take JAN of last year

#   fixed fields/variables
    latitude  = readnc.readnc('lat' ,filename)
    longitude = readnc.readnc('lon' ,filename)
    level     = readnc.readnc('lev' ,filename)
    levbnds   = readnc.readnc('ilev',filename)
    p0        = readnc.readnc('P0'  ,filename)
    hyam      = readnc.readnc('hyam',filename)
    hybm      = readnc.readnc('hybm',filename)
    hyai      = readnc.readnc('hyai',filename)
    hybi      = readnc.readnc('hybi',filename)

#   dimensions
    nlat = len(latitude)
    nlon = len(longitude)
    nlev = len(level)

    if ( nlat == 96 and nlon == 144 ) : resolution='1.9x2.5'
    else :
        print('+++ buildoxidants +++')
        print('No resolution recognized with nlat and nlon : ', nlat, nlon)
        quit()

#   III. TIME
#------------
    nmonth=12

    nyear = len(yearlist)
    year0 = yearlist[0]       # first element
    year1 = yearlist[-1]      # last element 
  
    date    = np.zeros(nyear*nmonth,dtype=int)  # integer  
    datesec = np.zeros(nyear*nmonth,dtype=int)  # integer

    for iyear in range(0,nyear) :
        year=yearlist[iyear]
        date[   iyear*nmonth:(iyear+1)*nmonth] = [116, 215, 316, 416, 516, 616, 716, 816, 916, 1016, 1116, 1216] + 10000 * year
        datesec[iyear*nmonth:(iyear+1)*nmonth] = [43200,0,43200,0,43200,0,43200,43200,0,43200,0,43200]
#
#   IV. NEW FILE
#----------------
    cyear0=str("%4.4i"% year0)
    cyear1=str("%2.2i"% year1)

#   cperiod
    if ( year0 == year1 ) :
        cperiod=cyear0              # one single year
    else :
        cperiod=cyear0+'-'+cyear1   # multiple years

#   FILENAME
    fshort=bctype+'_'+cperiod+'_'+resolution+'_'+version+'.nc'

##############
#   New file #
##############

#   create new directory
    outdir='/scratch/olivie/code/python/cmip7-oxidants-noresm-to-noresm/data/output/'+version
    if  not os.path.isdir(outdir) : os.makedirs(outdir)

#   create new NetCDF file
    fn = outdir+'/'+fshort
#
#   no overwriting
    if ( os.path.isfile(fn) and ( overwrite == False) ) : return

    print('File exists : ', os.path.isfile(fn))
    print('Overwrite : ', overwrite)
    print('Type : ', type(overwrite))

    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

######################
#   CreateDimensions #
######################
#
#   horizontal
    londimid = ds.createDimension('lon', nlon)
    latdimid = ds.createDimension('lat', nlat)

#   vertical
    levdimid  = ds.createDimension('lev' , nlev  )
    ilevdimid = ds.createDimension('ilev', nlev+1)

#   time
    timedimid = ds.createDimension('time', None)

######################
#   Define variables #
######################
# 
#   horizontal
    latid  = ds.createVariable('lat' , 'f4', ('lat',))
    lonid  = ds.createVariable('lon' , 'f4', ('lon',))

#   vertical
    levid  = ds.createVariable('lev' , 'f4', ('lev' ,))
    ilevid = ds.createVariable('ilev', 'f4', ('ilev',))

    p0id   = ds.createVariable('P0'  ,'f4')
    hyamid = ds.createVariable('hyam','f4', ('lev',))
    hybmid = ds.createVariable('hybm','f4', ('lev',))
    hyaiid = ds.createVariable('hyai','f4', ('ilev',))
    hybiid = ds.createVariable('hybi','f4', ('ilev',))

    psid   = ds.createVariable('PS','f4', ('time', 'lat', 'lon',), fill_value=1.e+20)

#   time
    timeid = ds.createVariable('time', 'f4', ('time',))
#
#   name of emissions will be name of sector
    speciesidlist=[]
    for species in specieslist :

        speciesidlist.append(ds.createVariable(species,'f4', ('time', 'lev', 'lat', 'lon',), fill_value=1.e+20))
# 
#   date
    dateid    = ds.createVariable('date'   , 'i4', ('time',))
    datesecid = ds.createVariable('datesec', 'i4', ('time',))
#
################
#   ATTRIBUTES #
################
#   latitude
    latid.long_name     = readattributenc.readattributenc('lat',filename,'long_name')
    latid.units         = readattributenc.readattributenc('lat',filename,'units')

#   longitude
    lonid.long_name     = readattributenc.readattributenc('lon',filename,'long_name')
    lonid.units         = readattributenc.readattributenc('lon',filename,'units')

#   altitude
    levid.positive      = readattributenc.readattributenc('lev',filename,'positive') 
    levid.long_name     = readattributenc.readattributenc('lev',filename,'long_name')
    levid.standard_name = readattributenc.readattributenc('lev',filename,'standard_name')
    levid.formula_terms = readattributenc.readattributenc('lev',filename,'formula_terms')
    levid.units         = readattributenc.readattributenc('lev',filename,'units')

#   altitude half levels
    ilevid.positive      = readattributenc.readattributenc('ilev',filename,'positive') 
    ilevid.long_name     = readattributenc.readattributenc('ilev',filename,'long_name')
    ilevid.standard_name = readattributenc.readattributenc('ilev',filename,'standard_name')
    ilevid.formula_terms = readattributenc.readattributenc('ilev',filename,'formula_terms')
    ilevid.units         = readattributenc.readattributenc('ilev',filename,'units')

#   P0
    p0id.long_name = readattributenc.readattributenc('P0',filename,'long_name')
    p0id.units     = readattributenc.readattributenc('P0',filename,'units')

#   hybrid coefficients
    hyamid.long_name = readattributenc.readattributenc('hyam',filename,'long_name')
    hybmid.long_name = readattributenc.readattributenc('hybm',filename,'long_name')

    hyaiid.long_name = readattributenc.readattributenc('hyai',filename,'long_name')
    hybiid.long_name = readattributenc.readattributenc('hybi',filename,'long_name')

#   species   
    for ispecies in range(0,nspecies) :         
        complist, weightlist = getoxidantcomponents.getoxidantcomponents(species=specieslist[ispecies])

        speciesidlist[ispecies].units     = readattributenc.readattributenc(complist[0], filename, 'units') # take units from first contributing component
        speciesidlist[ispecies].long_name = specieslist[ispecies]
        
#   PS (surface pressure field)    
    psid.long_name = readattributenc.readattributenc('PS',filename,'long_name')
    psid.units     = readattributenc.readattributenc('PS',filename,'units')
#
#   time 
    timeid.bounds        = "time_bnds"
    timeid.units         = time_units
    timeid.calendar      = calendar
    timeid.axis          = "T"
    timeid.long_name     = "time"
    timeid.standard_name = "time"

#   date
    dateid.long_name = 'current date as 8 digit integer (YYYYMMDD)'
    dateid.calendar  = 'noleap'

#   datesec
    datesecid.long_name = 'seconds of current date'
    datesecid.units     = 's'
#
#   global data   
#    ds.dataorigin = 'To be filled ...'

##################
#   WRITE FIELDS #
##################
#
#   FIXED FIELDS / VARIABLES
    latid[0:nlat] = latitude[ 0:nlat]
    lonid[0:nlon] = longitude[0:nlon]

    levid[ 0:nlev  ] = level[  0:nlev  ]
    ilevid[0:nlev+1] = levbnds[0:nlev+1]

    hyamid[0:nlev] = readnc.readnc('hyam', filename)
    hybmid[0:nlev] = readnc.readnc('hybm', filename)

    hyaiid[0:nlev+1] = readnc.readnc('hyai', filename)
    hybiid[0:nlev+1] = readnc.readnc('hybi', filename)

    p0id[:] = p0
#
#   
    print('yearlist      : ', yearlist)
    
    nmonth=12

    dataorigin=''

    for iyear in range(0,nyear) :

        expid  = expiddescriptionlist[iyear]['expid']
        period = expiddescriptionlist[iyear]['period']

        dataorigin=dataorigin + ' year:'            + str("%4.4i"% (expiddescriptionlist[iyear]['year'])) \
                              + ' experiment:'      +               expiddescriptionlist[iyear]['expid']  \
                              + ' averagingperiod:' +               expiddescriptionlist[iyear]['period'] \
                              + '\n'

        for imonth in range(0,nmonth) :

            itime=imonth + iyear*nmonth
#   
#           oxidants
            for ispecies in range(0,nspecies) :

                print(yearlist[iyear], imonth+1, specieslist[ispecies])

                F = readmeanfieldoxidants.readmeanfieldoxidants(species=specieslist[ispecies], expid=expid, period=period, month=imonth+1)
                
                speciesidlist[ispecies][itime,0:nlev,0:nlat,0:nlon] = F['field'][0:nlev,0:nlat,0:nlon]

#           surface pressure
            F = readmeanfieldoxidants.readmeanfieldoxidants(species='PS', expid=expid, period=period, month=imonth+1)
            psid[itime,0:nlat,0:nlon] = F['field'][0:nlat,0:nlon]

#
            dateid[itime] = date[itime]
            datesecid[itime] = datesec[itime]            
            timeid[itime] = daysince.daysince(refdate=refdate,enddate=date[itime], calendar=calendar) + float(datesec[itime]) / 86400.
   
#   global attribute
    ds.dataorigin = dataorigin
 
    ds.close()

