import getdatelist
import readsingleglobalmeanprofile

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents

def readmeanglobalmeanprofile_cmorized ( expid, var, year0, year1, season, region, verticalaxis):
#-------------------------------------
    '''
    MODIFICATIONS

    INPUT
        expid
        var
        year0
        year1
        season
        region
        verticalaxis : 'pressure' | 'height'

    RETURNS
        structure containing profile data

    CALLS
        getdatelist
        getvarcomponents
        readsingleglobalmeanprofile
    '''
    print('+++ readmeanglobalmeanprofile +++')
#
# get the datelist
    datelist=getdatelist.getdatelist(year0=year0,year1=year1,season=season)
    ndate=len(datelist)
#
# get the componentlist
    complist, weightlist = getvarcomponents.getvarcomponents(var=var)
    ncomp=len(complist)
#
# read all the components
    for icomp in range(0,ncomp) :
        comp=complist[icomp]
        weight=weightlist[icomp]
# read single component      
        tmp=readallcmorizedfield(expid=expid,var=comp) 
# add the singel component
        if ( icomp == 0 ) :
            data=copy.deepcopy(tmp)
            data['field']=data['field']*weight
        else :
            data['field']=data['field'] + tmp['field']*weight 
# select the correct dates 
    subset=[]
    for date in datelist : 
        index = data['datelist'].index(date)
        subset.append(index)
#
# newdata            
    newdata = { 'longitude' : data['longitude'], \
             'latitude'  : data['latitude'], \
             'nlon'      : data['nlon'], \
             'nlat'      : data['nlat'], \
             'nlev'      : data['nlev'], \
             'units'     : data['units'], \
             'yearlist'  : data['yearlist'][subset], \
             'monthlist' : data['monthlist'][subset], \
             'datelist'  : data['datelist'][subset], \
             'ntime'     : len(subset)}
#   in case of 4d data
    if( data['nlev'] == 0 ) :
        newdata.update({'field' : data['field'][subset,:,:])
    else :
        newdata.update({'field' : data['field'][subset,:,:,:])
             'pfull'     : data['pfull'][subset,:,:,:], \
             'phalf'     : data['phalf'][subset,:,:,:], \
             'units_pfull' : pfull['units'],\
             'units_phalf' : phalf['units']}       
#
    print('--- readmeanglobalmeanprofile ---')
#
    return newdata
