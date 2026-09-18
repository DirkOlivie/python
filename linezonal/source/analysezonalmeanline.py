import copy

import readmeanzonalmeanline
import plotzonalmeanline
import fillzonalmeanmemberstatistics

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getmemberlist


def analysezonalmeanline (expidlist, refidlist, refid2list, refid3list, wlist, wNRlist, legendlist, varlist, year0list, year1list, seasonlist, regionlist, horizontalaxis, figlayoutlist, code, colorlist, linestylelist, linewidthlist, ensembletypelist) :
#-----------------------
#
#   INPUT
#       wNRlist : weight for "noemer" in fraction
#
# MODIFICATIONS
#
#---------------------------------------------------------------------------------------
#
    print('+++ analysezonalmeanline +++')

    print(expidlist)
    print(legendlist)
    print(varlist)
    print(year0list)
    print(year1list)
    print(seasonlist)
    print(regionlist)
#
#   read all the data (loop over experiments)
    nexpid = len(expidlist)
    datalist=[]

    for iexpid in range(0,nexpid) :

#       A . SINGLE SIMULATION
        if ( ensembletypelist[iexpid] == '' ) :        

#           CHECK WHETHER HAVE TO BE READ
            doexp  = False
            doref  = False
            doref2 = False
            doref3 = False

            if ( expidlist  != None and wlist[0] != 0. and expidlist[ iexpid] != '' ) : doexp  = True
            if ( refidlist  != None and wlist[1] != 0. and refidlist[ iexpid] != '' ) : doref  = True
            if ( refid2list != None and wlist[2] != 0. and refid2list[iexpid] != '' ) : doref2 = True
            if ( refid3list != None and wlist[3] != 0. and refid3list[iexpid] != '' ) : doref3 = True
        
#           READ ALL POSSIBLE CONTRIBUTIONS
            if ( doexp  ) : expdata  = readmeanzonalmeanline.readmeanzonalmeanline(expid=expidlist[iexpid],  var=varlist[iexpid], year0=year0list[iexpid], year1=year1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid])
            if ( doref  ) : refdata  = readmeanzonalmeanline.readmeanzonalmeanline(expid=refidlist[iexpid],  var=varlist[iexpid], year0=year0list[iexpid], year1=year1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid])
            if ( doref2 ) : ref2data = readmeanzonalmeanline.readmeanzonalmeanline(expid=refid2list[iexpid], var=varlist[iexpid], year0=year0list[iexpid], year1=year1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid])
            if ( doref3 ) : ref3data = readmeanzonalmeanline.readmeanzonalmeanline(expid=refid3list[iexpid], var=varlist[iexpid], year0=year0list[iexpid], year1=year1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid])
#
#           SUM UP TELLER 
            dataTeller = copy.deepcopy(expdata)
            dataTeller['valuelist'][:] = 0.   # initialize to 0
            if ( doexp  ) : dataTeller['valuelist'] =    dataTeller['valuelist'] +  expdata[ 'valuelist'] * wlist[0]
            if ( doref  ) : dataTeller['valuelist'] =    dataTeller['valuelist'] +  refdata[ 'valuelist'] * wlist[1]
            if ( doref2 ) : dataTeller['valuelist'] =    dataTeller['valuelist'] +  ref2data['valuelist'] * wlist[2]
            if ( doref3 ) : dataTeller['valuelist'] =    dataTeller['valuelist'] +  ref3data['valuelist'] * wlist[3]
#
#           NOEMER
            if ( wNRlist != None) : 

#               CHECK WHETHER HAVE TO BE READ
                doexp  = False
                doref  = False
                doref2 = False
                doref3 = False

                if ( expidlist  != None and wNRlist[0] != 0. and expidlist[ iexpid] != '' ) : doexp  = True
                if ( refidlist  != None and wNRlist[1] != 0. and refidlist[ iexpid] != '' ) : doref  = True
                if ( refid2list != None and wNRlist[2] != 0. and refid2list[iexpid] != '' ) : doref2 = True
                if ( refid3list != None and wNRlist[3] != 0. and refid3list[iexpid] != '' ) : doref3 = True

#               SUM UP TELLER 
                dataNoemer = copy.deepcopy(dataTeller)
                dataNoemer['valuelist'][:] = 0.   # intialize to 0
                if ( doexp  ) : dataNoemer['valuelist'] =    dataNoemer['valuelist'] +  expdata[ 'valuelist'] * wNRlist[0]
                if ( doref  ) : dataNoemer['valuelist'] =    dataNoemer['valuelist'] +  refdata[ 'valuelist'] * wNRlist[1]
                if ( doref2 ) : dataNoemer['valuelist'] =    dataNoemer['valuelist'] +  ref2data['valuelist'] * wNRlist[2]
                if ( doref3 ) : dataNoemer['valuelist'] =    dataNoemer['valuelist'] +  ref3data['valuelist'] * wNRlist[3]
#
#               DO DIVISION
                dataTeller['valuelist'] = dataTeller['valuelist'] / dataNoemer['valuelist'] * 100.
                dataTeller['units'] = '%'

            datalist.append(dataTeller)
#
#       B. ensemble
        else :
#           list of all experiment members
            expmemberlist = getmemberlist.getmemberlist(expid=expidlist[iexpid])
            nexpmember=len(expmemberlist)

#           list of all reference members
            refmemberlist = getmemberlist.getmemberlist(expid=refidlist[iexpid])
            nrefmember=len(refmemberlist)

            d_all=[]

#           read all ensemblemembers
            for iexpmember in range(nexpmember) :
                for irefmember in range(nrefmember) :
                    a = readmeanzonalmeanline.readmeanzonalmeanline(expid=expmemberlist[iexpmember],  var=varlist[iexpid], year0=year0list[iexpid], year1=year1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid])
                    c = readmeanzonalmeanline.readmeanzonalmeanline(expid=refmemberlist[irefmember],  var=varlist[iexpid], year0=year0list[iexpid], year1=year1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid])
#                   if ( dorefaverage != None ) : c['valuelist'][:] = np.mean(c['valuelist'])

                    a['valuelist'] = a['valuelist'] * wlist[0] + c['valuelist'] * wlist[1]

                    d_all.append(a)    

            b =  fillzonalmeanmemberstatistics.fillzonalmeanmemberstatistics(data=d_all)

            datalist.append(b)

#   plot the zonal mean
    for figlayout in figlayoutlist :
        plotzonalmeanline.plotzonalmeanline(datalist=datalist, legendlist=legendlist, wlist=wlist, figlayout=figlayout, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist, horizontalaxis=horizontalaxis, ensembletypelist=ensembletypelist)
#
    print('--- analysezonalmeanline ---')
