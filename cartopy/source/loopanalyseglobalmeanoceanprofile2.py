import analyseglobalmeanoceanprofile
#
def loopanalyseglobalmeanoceanprofile2(expidlist, refidlist, wlist, legendlist, varlist, expyear0list, expyear1list, refyear0list, refyear1list, seasonlist, regionlist, verticalaxislist, figlayoutlist, description, code, colorlist=None,linestylelist=None, refid2list=None, refid3list=None):
#--------------------------------
#
    '''
    MODIFICATIONS
        (2022-09-07) : adding possibility for regions
        (2022-09-12) : adding description as keyword
        (2023-02-14) : adding possibility for differences : added refidlsit and wlist

    '''
    print('+++ loopanalyseglobalmeanprofile2 +++')
#
    if ( len(expidlist) != len(refidlist) \
      or len(expidlist) != len(expyear0list) \
      or len(expidlist) != len(expyear1list) \
      or len(expidlist) != len(refyear0list) \
      or len(expidlist) != len(refyear1list) \
      or len(expidlist) != len(seasonlist) ) : 
        print('expidlist  : ', len(expidlist))
        print('refidlist  : ', len(refidlist)) 
        print('year0list  : ', len(expyear0list)) 
        print('year1list  : ', len(expyear1list)) 
        print('year0list  : ', len(refyear0list)) 
        print('year1list  : ', len(refyear1list)) 
        print('seasonlist : ', len(seasonlist)) 
        quit()
#
    nexpid=len(expidlist)
    nvar=len(varlist)
    nseason=len(seasonlist)
    nregion=len(regionlist)
    nvert=len(verticalaxislist)

#
    for verticalaxis in verticalaxislist :

        for region in regionlist :

            if ( description == 'varcommon' ) :

                for var in varlist :
# 
                    tmpregionlist=[]
                    tmpvarlist=[]
                    for iexpid in range(0,nexpid) :
                        tmpregionlist.append(region)  
                        tmpvarlist.append(var)
#
                    analyseglobalmeanoceanprofile.analyseglobalmeanoceanprofile(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=tmpvarlist, expyear0list=expyear0list, expyear1list=expyear1list, refyear0list=refyear0list, refyear1list=refyear1list, seasonlist=seasonlist, verticalaxis=verticalaxis, regionlist=tmpregionlist, figlayoutlist=figlayoutlist, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
            elif ( description == '' ) : 
 
                if ( nexpid != nvar ) : exit(0)

                tmpregionlist=[]
                for iexpid in range(0,nexpid) :
                    tmpregionlist.append(region)

                analyseglobalmeanoceanprofile.analyseglobalmeanoceanprofile(expidlist=expidlist, refidlist=refidlist, refid2list=refid2list, refid3list=refid3list,wlist=wlist, legendlist=legendlist, varlist=varlist, expyear0list=expyear0list, expyear1list=expyear1list, refyear0list=refyear0list, refyear1list=refyear1list, seasonlist=seasonlist, verticalaxis=verticalaxis, regionlist=tmpregionlist, figlayoutlist=figlayoutlist, code=code, colorlist=colorlist, linestylelist=linestylelist)

#
    print('--- loopanalyseglobalmeanprofile2 ---')        
