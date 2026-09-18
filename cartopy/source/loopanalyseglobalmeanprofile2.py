import analyseglobalmeanprofile
#
def loopanalyseglobalmeanprofile2(expidlist, refidlist, wlist, legendlist, varlist, year0list, year1list, seasonlist, regionlist, verticalaxislist, figlayoutlist, description, code, colorlist=None,linestylelist=None, refid2list=None, refid3list=None, wNRlist=None, refyear0list=None, refyear1list=None):
#--------------------------------
#
    '''
    MODIFICATIONS
        (2022-09-07) : adding possibility for regions
        (2022-09-12) : adding description as keyword
        (2023-02-14) : adding possibility for differences : added refidlsit and wlist
        (2025-03-09) : adding possibility for fractions - addint wNRlist
        (2026-04-22) : adding possibility for refyear0list and refyear1list

    CALLS
        analyseglobalmeanprofile        

    '''
    print('+++ loopanalyseglobalmeanprofile2 +++')
#
    if ( len(expidlist) != len(refidlist) \
      or len(expidlist) != len(year0list) \
      or len(expidlist) != len(year1list) \
      or len(expidlist) != len(seasonlist) ) : 
        print('expidlist  : ', len(expidlist))
        print('refidlist  : ', len(refidlist)) 
        print('year0list  : ', len(year0list)) 
        print('year1list  : ', len(year1list)) 
        print('seasonlist : ', len(seasonlist)) 
        quit()
#
    if ( refid2list != None or refid3list != None ) :
        if ( len(expidlist) != len(refid2list) \
          or len(expidlist) != len(refid3list) ) :   
            print('expidlist  : ', len(expidlist))
            print('refid2list : ', len(refid2list))
            print('refid3list : ', len(refid3list))     
            quit()
        if ( len(wlist) != 4 ) :
            print('wlist : ', len(wlist)) 
            quit()
#
    if ( wNRlist != None ) :
        if ( len(wlist) != len(wNRlist) ) :
            print('Different lengths of weights : ')
            print('wlist   : ', len(wlist))
            print('wNRlist : ', len(wNRlist))
#
    if ( refyear0list == None and refyear1list == None ) :
        refyear0list = year0list
        refyear1list = year1list
    elif ( refyear0list == None or refyear1list == None ) :
        print('+++ loopanalyseglobalmeanprofile2 +++')
        print('refyear0list and refyear1list of different type : None and different from None')
        print('refyear0list : ', refyear0list)
        print('refyear1list : ', refyear1list)
        quit()
#
    if ( len(expidlist) != len(refyear0list) \
      or len(expidlist) != len(refyear1list) ) :
        print('expidlist  : ', len(expidlist))
        print('refidlist  : ', len(refidlist))
        print('year0list  : ', len(refyear0list))
        print('year1list  : ', len(refyear1list))
        print('seasonlist : ', len(seasonlist))
        quit()

    nexpid=len(expidlist)
    nvar=len(varlist)
    nseason=len(seasonlist)
    nyear=len(year0list)
    nregion=len(regionlist)
    nvert=len(verticalaxislist)

#
    for verticalaxis in verticalaxislist :
#
        if ( description == 'varcommon-regioncommon' \
          or description == 'regioncommon-varcommon' ) :

            for region in regionlist :

                for var in varlist :
# 
#                   fill lists
                    tmpregionlist=[]
                    tmpvarlist=[]
                    for iexpid in range(0,nexpid) :
                        tmpregionlist.append(region)  
                        tmpvarlist.append(var)
#
#                   execute
                    analyseglobalmeanprofile.analyseglobalmeanprofile(expidlist=expidlist, refidlist=refidlist, refid2list=refid2list, refid3list=refid3list, wlist=wlist, wNRlist=wNRlist, legendlist=legendlist, varlist=tmpvarlist, year0list=year0list, year1list=year1list, refyear0list=refyear0list, refyear1list=refyear1list, seasonlist=seasonlist, verticalaxis=verticalaxis, regionlist=tmpregionlist, figlayoutlist=figlayoutlist, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
        elif ( description == 'regioncommon' ) : 

            for region in regionlist : 
 
#               varlist should be used as is
                if ( nexpid != nvar ) : exit(0)

#               regionlist is filled
                tmpregionlist=[]
                for iexpid in range(0,nexpid) :
                    tmpregionlist.append(region)

#               execute
                analyseglobalmeanprofile.analyseglobalmeanprofile(expidlist=expidlist, refidlist=refidlist, refid2list=refid2list, refid3list=refid3list,wlist=wlist, wNRlist=wNRlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, refyear0list=refyear0list, refyear1list=refyear1list, seasonlist=seasonlist, verticalaxis=verticalaxis, regionlist=tmpregionlist, figlayoutlist=figlayoutlist, code=code, colorlist=colorlist, linestylelist=linestylelist)

        elif ( description == 'varcommon' ) : 

            for var in varlist : 
 
#               regionlist should be used as is
                if ( nexpid != nregion ) : exit(0)

#               varlist is filled
                tmpvarlist=[]
                for iexpid in range(0,nexpid) :
                    tmpvarlist.append(var)

#               execute
                analyseglobalmeanprofile.analyseglobalmeanprofile(expidlist=expidlist, refidlist=refidlist, refid2list=refid2list, refid3list=refid3list,wlist=wlist, wNRlist=wNRlist, legendlist=legendlist, varlist=tmpvarlist, year0list=year0list, year1list=year1list, refyear0list=refyear0list, refyear1list=refyear1list, seasonlist=seasonlist, verticalaxis=verticalaxis, regionlist=regionlist, figlayoutlist=figlayoutlist, code=code, colorlist=colorlist, linestylelist=linestylelist)

#
        elif ( description == '' ) : 

#           regionlist should be used as is
            if ( nexpid != nregion ) : exit(0)

#           varlist should be used as is
            if ( nexpid != nvar ) : exit(0)

#           execute
            analyseglobalmeanprofile.analyseglobalmeanprofile(expidlist=expidlist, refidlist=refidlist, refid2list=refid2list, refid3list=refid3list,wlist=wlist, wNRlist=wNRlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, refyear0list=refyear0list, refyear1list=refyear1list, seasonlist=seasonlist, verticalaxis=verticalaxis, regionlist=regionlist, figlayoutlist=figlayoutlist, code=code, colorlist=colorlist, linestylelist=linestylelist)

#
    print('--- loopanalyseglobalmeanprofile2 ---')        
