import analysescatter

def loopanalysescatter2(expXlist,refXlist,expXyear0list,expXyear1list,refXyear0list,refXyear1list,seasonXlist,wXlist,varXlist,typevarXlist, \
                        expYlist,refYlist,expYyear0list,expYyear1list,refYyear0list,refYyear1list,seasonYlist,wYlist,varYlist,typevarYlist, \
                        legendlist,colorlist,linestylelist,description,code,figlayout, \
                        refX2list=None,refX3list=None,refY2list=None,refY3list=None,regressionlist=None) :
#----------------------------
#
    nexpid=len(expXlist)
    nvar=len(varXlist)
#
    if ( regressionlist == None ) : regressionlist=[1]*nexpid


    if ( ( len(expXlist) != len(refXlist) ) \
      or ( len(expXlist) != len(expXyear0list) ) \
      or ( len(expXlist) != len(expXyear1list) ) \
      or ( len(expXlist) != len(refXyear0list) ) \
      or ( len(expXlist) != len(refXyear1list) ) \
      or ( len(expXlist) != len(seasonXlist) ) \
      or ( len(expXlist) != len(expYlist) ) \
      or ( len(expXlist) != len(refYlist) ) \
      or ( len(expXlist) != len(expYyear0list) ) \
      or ( len(expXlist) != len(expYyear1list) ) \
      or ( len(expXlist) != len(refYyear0list) ) \
      or ( len(expXlist) != len(refYyear1list) ) \
      or ( len(expXlist) != len(seasonYlist) ) \
      or ( len(expXlist) != len(legendlist) ) \
      or ( len(expXlist) != len(colorlist) ) \
      or ( len(expXlist) != len(linestylelist) ) \
      or ( len(expXlist) != len(regressionlist) ) \
      or ( len(varXlist) != len(varYlist) ) \
      or ( len(typevarXlist) != len(typevarYlist) )
      or ( len(varXlist) != len(typevarXlist) ) \
      ) :
        print('+++ loopanalysescatter2 +++')  
        print('length expXlist : ', len(expXlist))
        print('length refXlist : ', len(refXlist))
        print('length expXyear0list : ', len(expXyear0list))
        print('length expXyear1list : ', len(expXyear1list))
        print('length refXyear0list : ', len(refXyear0list))
        print('length refXyear1list : ', len(refXyear1list))
        print('length seasonXlist : ', len(seasonXlist))
        print('length expYlist : ', len(expYlist))
        print('length refYlist : ', len(refYlist))
        print('length expYyear0list : ', len(expYyear0list))
        print('length expYyear1list : ', len(expYyear1list))
        print('length refYyear0list : ', len(refYyear0list))
        print('length refYyear1list : ', len(refYyear1list))
        print('length seasonYlist : ', len(seasonYlist))
        print('length legendlist : ', len(legendlist))
        print('length colorlist : ', len(colorlist))
        print('length linestylelist : ', len(linestylelist))
        print('length regressionlist : ', len(regressionlist))
        print('length varXlist : ', len(varXlist))
        print('length varYlist : ', len(varYlist))
        print('length typevarXlist : ', len(typevarXlist))
        print('length typevarYlist : ', len(typevarYlist))
        print('--- loopanalysescatter2 ---')
        quit()

    if ( refX2list != None or refX3list != None or refY2list != None or refY3list != None ) :
        if ( len(expXlist) != len(refX2list) \
          or len(expXlist) != len(refX3list) \
          or len(expYlist) != len(refY2list) \
          or len(expYlist) != len(refY3list)) :
            print('expXlist : ', len(expXlist))
            print('refX2list : ', len(refX2list))
            print('refX3list : ', len(refX3list))
            print('expYlist : ', len(expYlist))
            print('refY2list : ', len(refY2list))
            print('refY3list : ', len(refY3list))
            quit()
        if ( len(wXlist) != 4 or len(wYlist) != 4) :
            print('wXlist : '+string(len(wXlist)))
            print('wYlist : '+string(len(wYlist)))
            quit()
    else :
        if ( len(wXlist) != 2 or len(wYlist) != 2 ) :
            print('wXlist : '+string(len(wXlist)))
            print('wYlist : '+string(len(wYlist)))
            quit()
#
    if ( description == 'varcommon-typevarcommon' ) : 

        for ivar in range(0,nvar) :

            varX=varXlist[ivar]
            varY=varYlist[ivar]

            typevarX=typevarXlist[ivar]
            typevarY=typevarYlist[ivar]

#           fill list with all identical values
            tmpvarXlist = [varX] * nexpid  
            tmpvarYlist = [varY] * nexpid
            tmptypevarXlist = [typevarX] * nexpid
            tmptypevarYlist = [typevarY] * nexpid

            analysescatter.analysescatter(\
                expXlist=expXlist,refXlist=refXlist,refX2list=refX2list,refX3list=refX3list,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=tmpvarXlist,typevarXlist=tmptypevarXlist, \
                expYlist=expYlist,refYlist=refYlist,refY2list=refY2list,refY3list=refY3list,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=tmpvarYlist,typevarYlist=tmptypevarYlist, \
                legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,regressionlist=regressionlist,code=code,figlayout=figlayout)

    elif ( description == '' ) : 

        analysescatter.analysescatter(\
                expXlist=expXlist,refXlist=refXlist,refX2list=refX2list,refX3list=refX3list,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
                expYlist=expYlist,refYlist=refYlist,refY2list=refY2list,refY3list=refY3list,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
                legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,regressionlist=regressionlist,code=code,figlayout=figlayout) 
