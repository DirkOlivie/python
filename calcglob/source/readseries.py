import re
import numpy as np
import copy

import getmemberlist

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents
import getvartellernoemer
import getvartrend
import readsingleseries
import getbasicexpidlist
import concatenateseries
import getfinalunits
import getmonthlength

def readseriesinternal4 (expid=None, variable=None, typevar=None, freqtype=None) :
#----------------------
    '''
    METHOD
        readseries : distinguishes between dotrend == ''             + calls readseriesinternal  
                                           dotrend == 'differential' + calls readseries
                                           dotrend == 'integral'     + calls readseries
                                           dotrend == 'offset'       + calls readseries

        readseriesinternal : distinguishes between dofraction == 0   + calls readseriesinternal2 
                                                   dofraction == 1   + calls readseries 


        readseriesinternal2 : distinguishes between # components == 1 + calls readseriesinternal3
                                                    # components >  1 + calls readseries 
 
        readseriesinternal3 : loops over all members                  + calls reaseriesinternal4

        readseriesinternal4 : loops over all basic experiments        + calls readsingleseries

    AIM 
        Concatenating series

    CALLS
        getbasicexpidlist
        readsingleseries

    MODIFICATIONS
        (2022-08-31)

    '''
#   get information about contributing experiments    
    expidlist=getbasicexpidlist.getbasicexpidlist(expid)
    nexpid=len(expidlist)

    for iexpid in range(0,nexpid) :

        tmp =readsingleseries.readsingleseries(expid=expidlist[iexpid], variable=variable, typevar=typevar, freqtype=freqtype)

        if ( iexpid == 0 ) : data = tmp
        else               : data = concatenateseries.concatenateseries(D0=data, D1=tmp)

#   add overall experiment name            
    data['expid'] = expid

    return data


def readseriesinternal3 (expid=None, variable=None, typevar=None, freqtype=None) :
#----------------------
    '''
    AIM
        averaging over members

    CALLS
        getmemberlist
        readseriesinternal3

    MODIFICATIONS
        (2022-08-31)

    '''
#   get information about contributing experiments    
    memberlist=getmemberlist.getmemberlist( expid)
    nmember=len(memberlist)

    print('expid : ', expid)
    print('memberlist : ', memberlist)

    for imember in range(0,nmember) :
        member=memberlist[imember]

        tmp = readseriesinternal4(expid=member, variable=variable, typevar=typevar, freqtype=freqtype)

        if ( imember == 0 ) : 
            data = tmp
        else : 
            data['valuelist'] = data['valuelist'] + tmp['valuelist']   

#   add overall experiment name            
    data['valuelist'] = data['valuelist'] / float(nmember)

    return data


def readseriesinternal2 (expid=None, variable=None, typevar=None, freqtype=None) :
#---------------------    
    '''
    AIM
        adding over variable components

    CALLS
        getvarcomponents
        readseriesinternal2

    MODIFICATIONS
	(2021-04-05) : creation
    '''

    complist, weightlist = getvarcomponents.getvarcomponents(var=variable, expid=expid)

    ncomp = len(complist)

    if ( ncomp == 1 ) :
        weight = weightlist[0]
        comp   = complist[0]    

        data = readseriesinternal3(expid=expid, variable=comp, typevar=typevar, freqtype=freqtype)
        data['valuelist'] = data['valuelist'] * weight        

    else :

        for icomp in range(ncomp) :        
            weight = weightlist[icomp]
            comp   = complist[icomp]

#           tmp = readsingleseries.readsingleseries(expid=expid, variable=comp, typevar=typevar, freqtype=freqtype)  
            tmp = readseries(expid=expid, variable=comp, typevar=typevar, freqtype=freqtype)  

            if ( icomp== 0 ) : 

                data=tmp
                data['valuelist'] = tmp['valuelist'] * weight

            else :

                data['valuelist'] = data['valuelist'] + tmp['valuelist'] * weight 


    data['variable'] = variable
#
#
    return data


def readseriesinternal(expid=None, variable=None, typevar=None, freqtype=None) :
#---------------------    
    '''
    AIM
        Calculating fraction (teller/noemer) or just teller

    MODIFICATIONS
        (2021-04-05) : creation
        (2025-06-25) : conversion to desired units
    '''

    info = getvartellernoemer.getvartellernoemer(var=variable)
    print(info)

    if ( info['dofraction'] == 0 ) :
#       read series
        data = readseriesinternal2(expid=expid, variable=variable, typevar=typevar, freqtype=freqtype)
    elif ( info['dofraction'] == 1 ) :
#       read
        tellerdata = readseries(expid=expid, variable=info['teller'], typevar=typevar, freqtype=freqtype) # teller # readseriesinternal2 before 20260129
        noemerdata = readseries(expid=expid, variable=info['noemer'], typevar=typevar, freqtype=freqtype) # noemer # readseriesinternal2 before 20260129
#       make new series
        data=tellerdata # the whole structure
        data['valuelist'] = tellerdata['valuelist'] / noemerdata['valuelist'] * info['f']
#       correct units and name
        data['units']    = info['newunits']
        data['variable'] = variable
    else : 
        print('Dofraction is different from 0 and 1')  
        exit()
#
# CORRECTION : some fields mention C-units, but still contain K-values (problem in scripts-python-cmip6-v2/netcdf_atmospher_exp_var.py)
    if ( data['units'] == 'C' and np.mean(data['valuelist']) >= 200. ) :
        data['valuelist'] = data['valuelist'] - 273.15
#
# FINAL = DESIRED UNITS
    units, factor = getfinalunits.getfinalunits(var=data['variable'], units=data['units'])
    data['units'] = units
    data['valuelist'] = data['valuelist'] * factor
#
# FINAL CONVERSION
    if ( variable == 'CO2_columnburden_as_RF' ) :
        data['valuelist'] = 5.35 * np.log(data['valuelist'] / 284.32e-6 )
        data['units']='W m-2'
#
    return data


def readseries (expid=None, variable=None, typevar=None, freqtype=None) :
#-------------    
    '''
    AIM
        Calculating trend if needed

    MODIFICATIONS
        (2021-04-05) : creation
        (2025-06-25) : conversion to desired units
        (2025-10-16) : added possibility for integral or differential (over time)
    '''

    info = getvartrend.getvartrend(var=variable)
    print(info)


#   standard
    if ( info['dotrend'] == '' ) :
#       read 
        data = readseriesinternal(expid=expid, variable=variable, typevar=typevar, freqtype=freqtype)

#   differential
    elif ( info['dotrend'] == 'differential'  ) :
#       read
        data = readseries(expid=expid, variable=info['varorig'], typevar=typevar, freqtype=freqtype) # readseriesinternal before 20260129

        y = copy.deepcopy(data['valuelist'])
        n = data['ntime']

#       monthly trend
        data['valuelist'][1:n-1] =  ( y[2:n] - y[0:n-2] ) / 2. # double time interval
        data['valuelist'][0] = y[1] - y[0]
        data['valuelist'][n-1] = y[n-1] - y[n-2]

#       scale to annual trend
        data['valuelist'][:] = data['valuelist'][:] * 12.
        data['units'] = data['units']+' year-1'

#       name
        data['variable'] = variable

#   integral
    elif ( info['dotrend'] == 'integral' ) :
#       read
        data = readseries(expid=expid, variable=info['varorig'], typevar=typevar, freqtype=freqtype) # readseriesinternal before 20260129

        y = copy.deepcopy(data['valuelist'])
        n = data['ntime']

#       monthly trend
        data['valuelist'][0] = 0. # + 0.5 * y[0]  # to correspond better with the offset treatment
        for i in range(1,n) :
            len0 = getmonthlength.getmonthlength(month=data['monthlist'][i-1],year=0,calendar='noleap')
            len1 = getmonthlength.getmonthlength(month=data['monthlist'][i]  ,year=0,calendar='noleap')

#           data['valuelist'][i] = data['valuelist'][i-1] + 0.5 * ( y[i-1] + y[i] )
#           data['valuelist'][i] = data['valuelist'][i-1] + ( float(len0) * y[i-1] + float(len1) * y[i] ) / ( len0 + len1 ) / 12.  # before 2026-02-15
            data['valuelist'][i] = data['valuelist'][i-1] + ( float(len0) * y[i-1] + float(len1) * y[i] ) / 2. / 365.
        
#       scale to annual trend
#       data['valuelist'][:] = data['valuelist'][:] / 12.   # before 2026-02-15

        if (data['units'] == 'Tg yr-1' ) :  
            data['units'] = 'Tg'

#       name
        data['variable'] = variable

#
    elif ( info['dotrend'] == 'offset' ) :
#       read
        data = readseries(expid=expid, variable=info['varorig'], typevar=typevar, freqtype=freqtype) # readseriesinternal before 20260129
        data['valuelist'][:] = data['valuelist'][:] - data['valuelist'][0]
        data['variable'] = variable

    elif ( info['dotrend'] == 'offsetlast30yr' ) :
#       read
        data = readseries(expid=expid, variable=info['varorig'], typevar=typevar, freqtype=freqtype) # readseriesinternal before 20260129
        data['valuelist'][:] = data['valuelist'][:] - np.mean(data['valuelist'][-1-12*30:-1])
        data['variable'] = variable

    else : 
        print('Dotrend is different from 0 and 1 : ', info['dotrend'])  
        exit()
#
#   CHANGING UNITS
    if ( ( data['variable'] == 'tempocn_trend' \
        or data['variable'] == 'thetaogaocn_trend' ) and data['units'] == 'degC year-1' ) : 
        data['valuelist'] = data['valuelist'] * 100
        data['units']     = 'degC century-1'  

    return data
