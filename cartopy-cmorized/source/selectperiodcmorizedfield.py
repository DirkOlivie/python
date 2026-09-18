import copy

import readallcmorizedfield
import experimentdefinition

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents

sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import getdatelist


def selectperiodcmorizedfield ( expid, var, year0, year1, season):
#----------------------------
    '''
    MODIFICATIONS

    INPUT
        expid
        var
        year0
        year1
        season

    RETURNS
        structure containing profile data

    CALLS
        getdatelist
        getvarcomponents
        readallcmorizedfield
    '''
    print('+++ readmeanglobalmeanprofile +++')
#
# get project
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    project=expidinfo['project']

# get the datelist
    datelist=getdatelist.getdatelist(year0=year0,year1=year1,season=season) # returns, e.g., [2001-03,2001-04,2001-05, 2002-03,2002-04,2002-05, ... 2005-03,2005-04,2005-05]
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
        tmp=readallcmorizedfield.readallcmorizedfield(expid=expid,var=comp,year0=year0,year1=year1,project=project) 
# add the singel component
        if ( icomp == 0 ) :
#            data=copy.deepcopy(tmp)
            data=tmp    
            data['field']=data['field']*weight
        else :
            data['field']=data['field'] + tmp['field']*weight 
# select the correct dates 
    subset=[]
    for date in datelist : 
        index = data['datelist'].tolist().index(date)  # first conversion from numpy array to list (index method only works on lists)
        subset.append(index)
#
    print('datelist : ', datelist)

    print('subset : ', subset)

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
        newdata.update({'field' : data['field'][subset,:,:]})
    else :
        newdata.update({'field'       : data['field'][subset,:,:,:], \
                        'pfull'       : data['pfull'][subset,:,:,:], \
#                        'phalf'       : data['phalf'][subset,:,:,:], \
                        'units_pfull' : data['units_pfull']})
#                        'units_phalf' : data['units_phalf']})       
#
    print('--- readmeanglobalmeanprofile ---')
#
    return newdata
