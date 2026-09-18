import readdistribution
import plotdistributionhistogram

def analysedistribution(expidlist, refidlist, wlist, varlist, typevarlist, timedescriptionlist, finalresolutionlist, legendlist, distributiontype, figlayoutlist, code) :
#----------------------

    '''
    INPUT
        expid
        variable
    '''

    nexpid=len(expidlist)

    a_all=[]
# read all experiments     
    for iexpid in range(0,nexpid) :

        a=readdistribution.readdistribution(expid=expidlist[iexpid], var=varlist[iexpid], typevar=typevarlist[iexpid], timedescription=timedescriptionlist[iexpid], finalresolution=finalresolutionlist[iexpid])
#
#        if ( wlist[1] != 0. ) :
#
#            c=readdistribution.readdistribution(expid=refidlist[iexpid], var=varlist[iexpid], typevar=typevarlist[iexpid], timedescription=timedescriptionlist[iexpid])
#
#            a['valuelist'] = a['valuelist'] - c['valuelist'] 

# attach the new data to the structure  
        a_all.append(a)
#
# do all the plotting   
    if ( distributiontype == 'histogram' ) : 
        for figlayout in figlayoutlist :
            plotdistributionhistogram.plotdistributionhistogram(data=a_all,legendlist=legendlist,figlayout=figlayout,code=code)
