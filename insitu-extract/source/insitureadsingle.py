import numpy as np
import sys

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import getdatelist

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import lon2lonbnds
import lat2latbnds
import xlon2ilon
import xlat2ilat
import readnc
import readattributenc

def insitureadsingle(expid, variable, xlon, xlat):
#-------------------

# get experiment info
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    chem=expidinfo['chem']
    year0=expidinfo['year0']
    year1=expidinfo['year1']
    subdir=expidinfo['subdir']
    cexpid=expidinfo['cexpid']
    model=expidinfo['model']

#   cam / cam2 in filename
    if ( model == 'NorESM1' ) :
        camversion='cam2'
    elif ( model == 'NorESM2' or model == 'CESM2' or model == 'NorESM2.5' or model == 'CESM2.5' ) :
        camversion='cam'

#   h0 / h0a / h0i in filename
    if ( model == 'NorESM1' or model == 'NorESM2' or model == 'CESM2' ) :
        h0version='h0'
    elif ( model == 'NorESM2.5' or model == 'CESM2.5' ) :
        h0version='h0a'

#   general info from first file
    yyyy = str("%4.4i"% (year1))
    filename=subdir+'/'+cexpid+'/atm/hist/'+cexpid+'.'+camversion+'.'+h0version+'.'+yyyy+'-01.nc'

# read longitude and latitude
    longitude=readnc.readnc('lon', filename)   
    latitude=readnc.readnc('lat', filename)
# read units
    units=readattributenc.readattributenc(variable,filename,'units')
#
#   lonbnds and latbnds
    lonbnds=lon2lonbnds.lon2lonbnds(longitude=longitude)
    latbnds=lat2latbnds.lat2latbnds(latitude=latitude)
#    
#   ilon and ilat
    ilon=xlon2ilon.xlon2ilon(lonbnds=lonbnds, xlon=xlon)
    ilat=xlat2ilat.xlat2ilat(latbnds=latbnds, xlat=xlat)
#
#   UNITS
    units=readattributenc.readattributenc(variable,filename,'units')

#   LOOP OVER ALL DATES
    datelist=getdatelist.getdatelist(year0=year0, year1=year1, season='YEA')

    yearlist=[]
    monthlist=[]
    valuelist=[]

    for date in datelist : 
#
        print('date : ', date)

#       split yyyy-mm into 
        line=date.split('-')
        yyyy=line[0]
        mm=line[1]
        filename=subdir+'/'+cexpid+'/atm/hist/'+cexpid+'.'+camversion+'.'+h0version+'.'+yyyy+'-'+mm+'.nc'

        field=np.squeeze(np.array(readnc.readnc(variable,filename)))
        value=field[ilat,ilon]

        year=int(line[0])  # year
        month=int(line[1]) # month

        yearlist.append(year)
        monthlist.append(month)
        valuelist.append(value)

    

#
# create a dictionary
    data={'expid'    : expid, \
          'variable' : variable, \
          'units'    : units, \
#          'fileorigin' : fileorigin, \
#          'area'     : float(arealist[iregion-2]), \
#          'areaglob' : float(arealist[iregionglob-2]), \
#          'areaunits': areaunits, \
          'yearlist' : np.array(yearlist,dtype=int), \
          'monthlist': np.array(monthlist,dtype=int), \
          'timelist' : np.array(yearlist)*1. + ( np.array(monthlist)*1. - 0.5 ) / 12., \
          'valuelist': np.array(valuelist), \
          'ntime'    : len(datelist)}
#
    print(data['units'])
#
    return data
