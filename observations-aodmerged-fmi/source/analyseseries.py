import getseries
import plotseriestoc
import getseasonalcycle
import plotseasonalcycle
import getannualseries

def analyseseries(expidlist, refidlist, xdiff, regionlist, varlist, year0, year1, code, plottypelist, colorlist, linestylelist, legendlist, dolegendlist, figlayout):
#----------------------
    '''
    CALLED BY
        loopanalyseseries2

    CALLS
        getseries
        plotseries
        getseasonalcycle
        plotseasonalcycle
    '''
#----------------------------------------------------------------------

    print('+++ analyseseries +++')
#
    nexpid=len(expidlist)
#   1. read all the data

    data=[] 

    for iexpid in range(0,nexpid) :
        expid=expidlist[iexpid]
        refid=refidlist[iexpid]
        region=regionlist[iexpid]
        var=varlist[iexpid]
      
        tmp=getseries.getseries(expid=expid, refid=refid, xdiff=xdiff, region=region, var=var, year0=year0, year1=year1)

        data.append(tmp)

#
#   2. plot the data [timeseries/seasonal cycle]
    for plottype in plottypelist: 

        if ( plottype == 'timeseries' ) :
#           variable plotting          
            plotseriestoc.plotseriestoc(expidlist=expidlist, xdiff=xdiff, vartype='var', code=code, data=data, \
                    colorlist=colorlist, linestylelist=linestylelist, legendlist=legendlist, dolegendlist=dolegendlist, figlayout=figlayout)
#           mask plotting    
            plotseriestoc.plotseriestoc(expidlist=expidlist, xdiff=xdiff, vartype='mask', code=code, data=data, \
                    colorlist=colorlist, linestylelist=linestylelist, legendlist=legendlist, dolegendlist=dolegendlist, figlayout=figlayout)

        elif ( plottype == 'timeseries-season' ) :

            seasonlist=['DJF','MAM','JJA','SON','YEA']

            for season in seasonlist:

                seasondata=[]

#               calculate all seasonal cycles           
                for iexpid in range(0,nexpid):
                    tmp=getannualseries.getannualseries(data=data[iexpid], season=season)

                    seasondata.append(tmp)            

#               variable plotting          
                plotseriestoc.plotseriestoc(expidlist=expidlist, xdiff=xdiff, vartype='var', code=code+'_'+season, data=seasondata, \
                    colorlist=colorlist, linestylelist=linestylelist, legendlist=legendlist, dolegendlist=dolegendlist, figlayout=figlayout)
#               mask plotting    
                plotseriestoc.plotseriestoc(expidlist=expidlist, xdiff=xdiff, vartype='mask', code=code+'_'+season, data=seasondata, \
                    colorlist=colorlist, linestylelist=linestylelist, legendlist=legendlist, dolegendlist=dolegendlist, figlayout=figlayout)
 

        elif ( plottype == 'seasonalcycle' ) :

            vartypelist=['var-unweighted','var-weighted','weight']
            for vartype in vartypelist :

                cycledata=[]

#               calculate all seasonal cycles           
                for iexpid in range(0,nexpid):
                    tmp=getseasonalcycle.getseasonalcycle(data=data[iexpid], vartype=vartype)

                    cycledata.append(tmp)            

#               plot seasonal cycle
                plotseasonalcycle.plotseasonalcycle(expidlist=expidlist, xdiff=xdiff, vartype=vartype, code=code, data=cycledata, \
                    colorlist=colorlist, linestylelist=linestylelist, legendlist=legendlist, dolegendlist=dolegendlist, figlayout=figlayout)

