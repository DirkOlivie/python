import analysemap
#
def loopanalysemap2(expidlist, refidlist, wlist, varlist, year0list, year1list, seasonlist, figlayoutlist, code, description='', refyear0list=None, refyear1list=None):
#------------------
    print('+++ loopanalysemap2 +++')
    print('--- loopanalysemap2 ---') 
#
    if ( len(expidlist) != len(refidlist) ) : exit()
    if ( len(wlist) != 2) : exit()
    if ( len(year0list) != len(year1list) ) : exit()
#
    if ( refyear0list == None ) : refyear0list = year0list
    if ( refyear1list == None ) : refyear1list = year1list



#   nvar=len(varlist)
    nexpid=len(expidlist)
    nyear=len(year0list)
#
    if ( description == 'yearcommon-varcommon'
      or description == 'varcommon-yearcommon' ) :
   
        for iyear in list(range(0,nyear)):

            year0=year0list[iyear]
            year1=year1list[iyear]

            refyear0=refyear0list[iyear]
            refyear1=refyear1list[iyear]

            for iexpid in list(range(0,nexpid)):

                expid=expidlist[iexpid]
                refid=refidlist[iexpid] 

                for var in varlist:
                    for season in seasonlist: 
                        analysemap.analysemap(expid=expid, refid=refid, wlist=wlist, var=var, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, season=season, figlayoutlist=figlayoutlist, code=code)   

    elif ( description == 'yearcommon' ) :
   
        if ( len(varlist) != len(expidlist) ) : exit()

        for iyear in list(range(0,nyear)):

            year0=year0list[iyear]
            year1=year1list[iyear]

            refyear0=refyear0list[iyear]
            refyear1=refyear1list[iyear]


            for iexpid in list(range(0,nexpid)):

                expid=expidlist[iexpid]
                refid=refidlist[iexpid] 
                var=varlist[iexpid]  

                for season in seasonlist: 
                    analysemap.analysemap(expid=expid, refid=refid, wlist=wlist, var=var, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, season=season, figlayoutlist=figlayoutlist, code=code)

    
    elif ( description == 'varcommon' ) :
   
        if ( len(year0list) != len(expidlist) ) : exit()  

        for iexpid in list(range(0,nexpid)):

            year0=year0list[iexpid]
            year1=year1list[iexpid]

            refyear0=refyear0list[iexpid]
            refyear1=refyear1list[iexpid]

            expid=expidlist[iexpid]
            refid=refidlist[iexpid] 

            for var in varlist:
                for season in seasonlist: 
                    analysemap.analysemap(expid=expid, refid=refid, wlist=wlist, var=var, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, season=season, figlayoutlist=figlayoutlist, code=code)  
 
    elif ( description == '' ) :
   
        if ( len(year0list) != len(expidlist) ) : exit()  
        if ( len(varlist)   != len(expidlist) ) : exit()  

        for iexpid in list(range(0,nexpid)):

            year0=year0list[iexpid]
            year1=year1list[iexpid]
            
            refyear0=refyear0list[iexpid]
            refyear1=refyear1list[iexpid]

            expid=expidlist[iexpid]
            refid=refidlist[iexpid] 
            var=varlist[iexpid]

            for season in seasonlist: 
                analysemap.analysemap(expid=expid, refid=refid, wlist=wlist, var=var, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, season=season, figlayoutlist=figlayoutlist, code=code)   
