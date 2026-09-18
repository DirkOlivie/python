import analysezonalseries
#
def loopanalysezonalseries2(expidlist, refidlist, wlist, varlist, typevarlist, year0, year1, refyear0, refyear1, freqtypelist, seasonlist, dorefyearaverage, description, code, figlayoutlist):
#--------------------------
    '''
    INPUT
        ...
        year0
        year1
        ...

    CALLS
        analysezonalseries
    '''


    print('+++ loopanalysezonalseries2 +++')
    print('--- loopanalysezonalseries2 ---') 

    if ( len(expidlist) != len(refidlist) ) : 
        print('+++ loopanalysezonalseries2 +++')
        print('len(expidlist) : ', len(expidlist))
        print('len(refidlist) : ', len(refidlist))
        quit()

    if ( len(wlist) != 2) : 
        print('+++ loopanalysezonalseries2 +++')
        print('len(wlist) should be 2 but is : ', len(wlist))
        quit()

    nexpid=len(expidlist)
#   
    for iexpid in list(range(0,nexpid)):

        expid=expidlist[iexpid]
        refid=refidlist[iexpid]

        for var in varlist :
            for typevar in typevarlist :
                for freqtype in freqtypelist : 
                    for season in seasonlist : 
                        analysezonalseries.analysezonalseries(expid=expid, refid=refid, wlist=wlist, var=var, typevar=typevar, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, freqtype=freqtype, season=season, dorefyearaverage=dorefyearaverage, description=description, code=code, figlayoutlist=figlayoutlist)   
