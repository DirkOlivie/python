import analyseoceancolumnintegral
#
def loopanalyseoceancolumnintegral2(expidlist, refidlist, wlist, varlist, year0list, year1list, seasonlist, figlayoutlist, code):
#-----------------------------

    print('+++ loopanalyseoceancolumnintegral2 +++')
    print('--- loopanalyseoceancolumnintegral2 ---') 

    if ( len(year0list) != len(year1list) ) : exit()    

    nvar=len(varlist)
    nseason=len(seasonlist)
    nexpid=len(expidlist)
    nyear=len(year0list)
#   
    for iyear in list(range(0,nyear)):

        year0=year0list[iyear]
        year1=year1list[iyear]

        for iexpid in list(range(0,nexpid)):

            expid=expidlist[iexpid]
            refid=refidlist[iexpid]

            for var in varlist:
                for season in seasonlist: 
                    analyseoceancolumnintegral.analyseoceancolumnintegral(expid=expid, refid=refid, wlist=wlist, var=var, year0=year0, year1=year1, season=season, figlayoutlist=figlayoutlist, code=code)
