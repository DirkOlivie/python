import analyseoceanmap
#
def loopanalyseoceanmap2(expidlist, refidlist, wlist, varlist, year0list, year1list, seasonlist, figlayoutlist, code):
#-----------------------
    print('+++ loopanalyseoceanmap2 +++')
    print('--- loopanalyseoceanmap2 ---') 

    if ( len(expidlist) != len(refidlist) ) : exit()
    if ( len(wlist) != 2) : exit()
    if ( len(year0list) != len(year1list) ) : exit()


    nvar=len(varlist)
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
                    analyseoceanmap.analyseoceanmap(expid=expid, refid=refid, wlist=wlist, var=var, year0=year0, year1=year1, season=season, figlayoutlist=figlayoutlist, code=code)   
