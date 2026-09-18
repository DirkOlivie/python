import numpy as np
import copy

import averageperiodcmorizedfield

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getmemberlist

def averagememberaverageperiodcmorizedfield ( expid, var, year0, year1, season):
#------------------------------------------
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
    print('+++ averagememberaverageperiodcmorizedfield +++')
#
# get the selected data
    memberlist=getmemberlist.getmemberlist(expid=expid)

    nmember=len(memberlist)
#
#   SUMMING 
    for imember in range(nmember) : 

        tmp=averageperiodcmorizedfield.averageperiodcmorizedfield(expid=memberlist[imember], var=var, year0=year0, year1=year1, season=season) 

        if ( imember == 0 ) : 

            data = copy.deepcopy(tmp) # should this be a hard copy ?
            data['field'] = data['field'] / float(nmember)

            if ( data['nlev'] != 0 ) :

                data['pfull'] = data['pfull'] / float(nmember)
#               data['phalf'] = data['phalf'] / float(nmember

        else : 

            data['field'] = data['field'] + tmp['field'] / float(nmember)
 
            if ( data['nlev'] != 0 ) :

                data['pfull'] = data['pfull'] + tmp['pfull'] / float(nmember)
#               data['phalf'] = data['phalf'] + tmp['phalf'] / float(nmember)  
#
    print('--- averagememberaverageperiodcmorizedfield ---')
#
    return data
