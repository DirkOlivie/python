import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import plotmap

def analysetopography(setopofile, fvtopofile, regridweightfile, figlayoutlist, code) :
#--------------------

#   initialise new field
#    newfield = np.zeros((nlat,nlon),dtype=float)


#   read weights from regridfile
    col = readnc.readnc('col', regridweightfile) - 1 # should start at 0 !!
    row = readnc.readnc('row', regridweightfile) - 1 # should start at 0 !!
    S   = readnc.readnc('S'  , regridweightfile)

#   read ne30pg3 topograph
    setopo = readnc.readnc('PHIS',setopofile) # m2/s2

#   read fv topography
    fvtopo    = readnc.readnc('PHIS',fvtopofile)
    longitude = readnc.readnc('lon' ,fvtopofile)
    latitude  = readnc.readnc('lat' ,fvtopofile)

    nlat,nlon = fvtopo.shape


#   initialise new field
    newfield = np.zeros((nlat,nlon),dtype=float)

#   fill new field
    for i in range(0,len(S)) :
        newfield[row[i] // nlon,  row[i] % nlon] = newfield[row[i] // nlon,  row[i] % nlon] + S[i] * setopo[col[i]]

#   
    ifound = 0    
    for ilat in range(0,nlat) :
        for ilon in range(0,nlon) :
            if ( fvtopo[ilat,ilon] != 0. or newfield[ilat,ilon] != 0. ) :
                print(ifound, ilat, ilon, fvtopo[ilat,ilon], newfield[ilat,ilon])
                ifound=ifound+1

#   
    newdata = { 'field' : newfield, \
                'units' : 'm2 s-2', \
                'latitude' : latitude, \
                'longitude' : longitude }
#
    fvdata = { 'field' : fvtopo, \
                'units' : 'm2 s-2', \
                'latitude' : latitude, \
                'longitude' : longitude }



    for figlayout in figlayoutlist :
        plotmap.plotmap(expid='topo', refid='topo', wlist=[1.,0.], var='PHIS', year0=9999, year1=9999, season='CTE', expdata=newdata, refdata=newdata, figlayout=figlayout, code='se_'+code)

    for figlayout in figlayoutlist :
        plotmap.plotmap(expid='topo', refid='topo', wlist=[1.,0.], var='PHIS', year0=9999, year1=9999, season='CTE', expdata=fvdata , refdata=fvdata , figlayout=figlayout, code='fv_'+code)

    for figlayout in figlayoutlist :
        plotmap.plotmap(expid='topo', refid='topo', wlist=[1.,-1], var='PHIS', year0=9999, year1=9999, season='CTE', expdata=newdata , refdata=fvdata , figlayout=figlayout, code='se-fv_'+code)

