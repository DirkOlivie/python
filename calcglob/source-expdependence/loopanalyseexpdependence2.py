import analyseexpdependence

def loopanalyseexpdependence2(expidlist,refidlist, \
                              expyear0list,expyear1list,refyear0list,refyear1list,seasonlist, \
                              wlist, \
                              varlist,typevarlist,legendlist,colorlist,linestylelist, \
                              xvaluelist, xtitle, xunits, \
                              description,code,figlayout) :
#----------------------------

    print('***')
#
#   SOME CHECKS ON EXPERIMENTS
    if ( ( len(expidlist) != len(refidlist) ) \
      or ( len(expidlist) != len(expyear0list) ) \
      or ( len(expidlist) != len(expyear1list)  ) \
      or ( len(expidlist) != len(refyear0list) ) \
      or ( len(expidlist) != len(refyear1list)  ) \
      or ( len(expidlist) != len(xvaluelist)  ) ) : 
        print('length expidlist    : ', len(expidlist))
        print('length refidlist    : ', len(refidlist))
        print('length expyear0list : ', len(expyear0list))
        print('length expyear1list : ', len(expyear1list))
        print('length refyear0list : ', len(refyear0list))
        print('length refyear1list : ', len(refyear1list))
        print('length xvaluelist   : ', len(xvaluelist))
        quit()
#
#   SOME CHECKS ON VARIABLES
#    if ( ( len(varlist) != len(typevarlist) ) \
#      or ( len(varlist) != len(legendlist) ) \
#      or ( len(varlist) != len(colorlist) ) \
#      or ( len(varlist) != len(linestylelist) ) ) :
#        print('length varlist      : ', len(varlist))
#        print('length typevarlist  : ', len(typevarlist))
#        print('length legendlist   : ', len(legendlist))
#        print('length colorlist    : ', len(colorlist))
#        print('length linestyllist : ', len(linestylelist))
#
    nvar = len(varlist)
    ntypevar = len(typevarlist)

    print('description = ', description) 

   
    if ( description == 'typevarcommon' ) :

        for typevar in typevarlist :
            tmpvarlist=varlist
            tmptypevarlist=[''] * nvar

            for ivar in range(0,nvar) :
                   tmptypevarlist[ivar] = typevar

            analyseexpdependence.analyseexpdependence(\
                   expidlist=expidlist,refidlist=refidlist, \
                   expyear0list=expyear0list,expyear1list=expyear1list,refyear0list=refyear0list,refyear1list=refyear1list,seasonlist=seasonlist, \
                   wlist=wlist, \
                   varlist=tmpvarlist,typevarlist=tmptypevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
                   xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
                   description=description,code=code,figlayout=figlayout)


    elif ( description == 'varcommon-typevarcommon' \
        or description == 'typevarcommon-varcommon' ) :

        for var in varlist :

           for typevar in typevarlist :

               tmpvarlist=[var]
               tmptypevarlist=[typevar]

               analyseexpdependence.analyseexpdependence(\
                   expidlist=expidlist,refidlist=refidlist, \
                   expyear0list=expyear0list,expyear1list=expyear1list,refyear0list=refyear0list,refyear1list=refyear1list,seasonlist=seasonlist, \
                   wlist=wlist, \
                   varlist=tmpvarlist,typevarlist=tmptypevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
                   xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
                   description=description,code=code,figlayout=figlayout)

    elif ( description == '' ) :

        analyseexpdependence.analyseexpdependence(\
            expidlist=expidlist,refidlist=refidlist, \
            expyear0list=expyear0list,expyear1list=expyear1list,refyear0list=refyear0list,refyear1list=refyear1list,seasonlist=seasonlist, \
            wlist=wlist, \
            varlist=varlist,typevarlist=typevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
            xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
            description=description,code=code,figlayout=figlayout)






