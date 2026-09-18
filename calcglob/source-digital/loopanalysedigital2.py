import analysedigital

def loopanalysedigital2(expidlist,refidlist,wlist,xlist,expyear0list,expyear1list,expseasonlist,refyear0list,refyear1list,refseasonlist,legendlist,varlist,typevar,description,code) :
#---------------------

    if ( ( len(expidlist) != len(refidlist) ) \
      or ( len(expidlist) != len(xlist) ) \
      or ( len(expidlist) != len(expyear0list) ) \
      or ( len(expidlist) != len(expyear1list) ) \
      or ( len(expidlist) != len(expseasonlist) ) \
      or ( len(expidlist) != len(refyear0list) ) \
      or ( len(expidlist) != len(refyear1list) ) \
      or ( len(expidlist) != len(refseasonlist) ) \
      or ( len(expidlist) != len(legendlist) ) ) : 
        print('length expidlist : ', len(expidlist))
        print('length refidlist : ', len(refidlist))
        print('length xlist : ', len(xlist))
        print('length expyear0list : ', len(expyear0list))
        print('length expyear1list : ', len(expyear1list))
        print('length expseasonlist : ', len(expseasonlist))
        print('length refyear0list : ', len(refyear0list))
        print('length refyear1list : ', len(refyear1list))
        print('length refseasonlist : ', len(refseasonlist))
        print('length legendlist : ', len(legendlist))
        quit()

    nexpid=len(expidlist)
    nplot=len(varlist)

    print(varlist)   


    for iplot in range(0,nplot) :


        print('--- STARTING ---')

        tmplist=varlist[iplot]

        print(tmplist)

        analysedigital.analysedigital(expidlist=expidlist,refidlist=refidlist,wlist=wlist,xlist=xlist,expyear0list=expyear0list,expyear1list=expyear1list,expseasonlist=expseasonlist,refyear0list=refyear0list,refyear1list=refyear1list,refseasonlist=refseasonlist,legendlist=legendlist,varlist=tmplist,typevar=typevar,code=code)


##   all experiments use same var
#    if ( description == 'varcommon' ) :  
#       
#       for var in varlist :
#
#           tmplist=[''] * nexpid
#           
#           for iexpid in range(0,nexpid) :  
#               tmplist[iexpid] = var
#
#           print(varlist)  
#           print(tmplist)  
#
#           analysedigital.analysedigital(expidlist=expidlist,refidlist=refidlist,wlist=wlist,expyear0list=expyear0list,expyear1list=expyear1list,expseasonlist=expseasonlist,refyear0list=refyear0list,refyear1list=refyear1list,refseasonlist=refseasonlist,legendlist=legendlist,varlist=tmplist,typevar=typevar,code=code)
#
##   experiments can use different vars
#    elif (description == '' ) :
#        if ( nexpid != nvar ) : exit(0)
#        analysedigital.analysedigital(expidlist=expidlist,refidlist=refidlist,wlist=wlist,expyear0list=expyear0list,expyear1list=expyear1list,expseasonlist=expseasonlist,refyear0list=refyear0list,refyear1list=refyear1list,refseasonlist=refseasonlist,legendlist=legendlist,varlist=varlist,typevar=typevar,code=code)
