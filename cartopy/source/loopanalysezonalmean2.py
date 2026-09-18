import analysezonalmean
#
def loopanalysezonalmean2(expidlist, refidlist, wlist, varlist, year0, year1, seasonlist, figlayoutlist, code, refyear0=None, refyear1=None):
#
    print('+++ loopanalysezonalmean2 +++')
    print('--- loopanalysezonalmean2 ---') 

    if ( len(expidlist) != len(refidlist) ) :
        print('expidlist (#) : '+string(len(expidlist)))
        print('refidlist (#) : '+string(len(refidlist)))
        exit()
    if ( len(wlist) != 2) : 
        print('wlist (#) : '+string(len(wlist)))        
        exit()

    nexpid=len(expidlist)
#   
    for iexpid in list(range(0,nexpid)):

        expid=expidlist[iexpid]
        refid=refidlist[iexpid]

        for var in varlist:
            for season in seasonlist: 
                analysezonalmean.analysezonalmean(expid=expid, refid=refid, wlist=wlist, var=var, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, season=season, figlayoutlist=figlayoutlist, code=code)   
