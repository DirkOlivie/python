import analysezonalmeanline
#
def loopanalysezonalmeanline2(expidlist, refidlist, wlist, legendlist, varlist, year0list, year1list, seasonlist, regionlist, horizontalaxislist, figlayoutlist, description, code, refid2list=None, refid3list=None, colorlist=None,linestylelist=None,linewidthlist=None, wNRlist=None, ensembletypelist=None):
#----------------------------
#
    '''
    MODIFICATIONS
        (2025-05-20) : creation

    CALLS
        analysezonalmeanline

    '''
    print('+++ loopanalysezonalmeanline2 +++')
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
    nexpid=len(expidlist)
#
    if ( ensembletypelist == None ) :
        ensembletypelist = ['']*nexpid

    if ( len(expidlist) != len(ensembletypelist) ) :
        print('length expidlist : ', len(expidlist))
        print('length ensembletypelist : ', len(ensembletypelist))
        quit()

    nvar=len(varlist)
    nseason=len(seasonlist)
    nyear=len(year0list)
    nregion=len(regionlist)
    nvert=len(horizontalaxislist)





#
    print('A')
#
    for horizontalaxis in horizontalaxislist :

        print('B')

        for region in regionlist :

            print('C') 

            if ( description == 'varcommon' ) :

                for var in varlist :
# 
                    tmpregionlist=[]
                    tmpvarlist=[]
                    for iexpid in range(0,nexpid) :
                        tmpregionlist.append(region)  
                        tmpvarlist.append(var)
#
                    analysezonalmeanline.analysezonalmeanline(expidlist=expidlist, refidlist=refidlist, refid2list=refid2list, refid3list=refid3list, wlist=wlist, wNRlist=wNRlist, legendlist=legendlist, varlist=tmpvarlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, horizontalaxis=horizontalaxis, regionlist=tmpregionlist, figlayoutlist=figlayoutlist, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist, ensembletypelist=ensembletypelist)
#
            elif ( description == '' ) : 
 
                if ( nexpid != nvar ) : exit(0)

                tmpregionlist=[]
                for iexpid in range(0,nexpid) :
                    tmpregionlist.append(region)

                analysezonalmeanline.analysezonalmeanline(expidlist=expidlist, refidlist=refidlist, refid2list=refid2list, refid3list=refid3list, wlist=wlist, wNRlist=wNRlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, horizontalaxis=horizontalaxis, regionlist=tmpregionlist, figlayoutlist=figlayoutlist, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist, ensembletypelist=ensembletypelist)

#
    print('--- loopanalysezonalmeanline2 ---')        
