import analysescatterseries

def loopanalysescatterseries2(expXlist,refXlist,expXyear0list,expXyear1list,refXyear0list,refXyear1list,seasonXlist,wXlist,varXlist,typevarXlist, \
                              expYlist,refYlist,expYyear0list,expYyear1list,refYyear0list,refYyear1list,seasonYlist,wYlist,varYlist,typevarYlist, \
                              legendlist,colorlist,dolinearregressionlist,description,code) :
#----------------------------

    if ( ( len(expXlist) != len(refXlist) ) \
      or ( len(expXlist) != len(expXyear0list) ) \
      or ( len(expXlist) != len(expXyear1list) ) \
      or ( len(expXlist) != len(refXyear0list) ) \
      or ( len(expXlist) != len(refXyear1list) ) \
      or ( len(expXlist) != len(seasonXlist) ) \
      or ( len(wXlist)   != 2                   ) \
      or ( len(expXlist) != len(expYlist) ) \
      or ( len(expXlist) != len(refYlist) ) \
      or ( len(expXlist) != len(expYyear0list) ) \
      or ( len(expXlist) != len(expYyear1list) ) \
      or ( len(expXlist) != len(refYyear0list) ) \
      or ( len(expXlist) != len(refYyear1list) ) \
      or ( len(expXlist) != len(seasonYlist) ) \
      or ( len(wYlist)   != 2 ) \
      or ( len(expXlist) != len(legendlist) ) \
      or ( len(expXlist) != len(colorlist) ) \
      or ( len(expXlist) != len(dolinearregressionlist) ) \
      or ( len(varXlist) != len(varYlist) ) \
      or ( len(typevarXlist) != len(typevarYlist) )
      or ( len(varXlist) != len(typevarXlist) ) \
      ) : 
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
        print('length dolinearregressionlist : ', len(dolinearregressionlist))
        print('length varXlist : ', len(varXlist))
        print('length varYlist : ', len(varYlist))
        print('length typevarXlist : ', len(typevarXlist))
        print('length typevarYlist : ', len(typevarYlist))
        quit()

    nvar=len(varXlist)

    for ivar in range(0,nvar) :

        varX=varXlist[ivar]
        varY=varYlist[ivar]

        typevarX=typevarXlist[ivar]
        typevarY=typevarYlist[ivar]


        analysescatterseries.analysescatterseries(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varX=varX,typevarX=typevarX, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varY=varY,typevarY=typevarY, \
        legendlist=legendlist,colorlist=colorlist,dolinearregressionlist=dolinearregressionlist, \
        description=description,code=code)
        
