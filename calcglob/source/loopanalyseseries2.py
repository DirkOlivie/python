import analyseseries

def loopanalyseseries2(expidlist,refidlist,wlist,legendlist,shiftlist,smoothlist,variablelist,typevarlist,freqtype,description,code,figlayout,dorefaverage=None,colorlist=None, linestylelist=None, linewidthlist=None, refid2list=None, refid3list=None, ensembletypelist=None ) :
#---------------------

    print('***')
#
#   SOME CHECKS
    if ( ( len(expidlist) != len(refidlist) ) \
      or ( len(expidlist) != len(legendlist) ) \
      or ( len(expidlist) != len(shiftlist)  ) \
      or ( len(expidlist) != len(smoothlist)  ) ) : 
        print('length expidlist : ', len(expidlist))
        print('length refidlist : ', len(refidlist))
        print('length legendlist : ', len(legendlist))
        print('length shiftlist : ', len(shiftlist))
        print('length smoothlist : ', len(smoothlist))
        quit()
#
    if ( refid2list != None or refid3list != None ) :
        if ( len(expidlist) != len(refid2list) \
          or len(expidlist) != len(refid3list) ) :
            print('expidlist : '+string(len(expidlist)))
            print('refid2list : '+string(len(refid2list)))
            print('refid3list : '+string(len(refid3list)))
            quit()
        if ( len(wlist) != 4 ) :
            print('wlist : '+string(len(wlist)))
            quit()
#
    nexpid=len(expidlist)
    nvar=len(variablelist)
    ntypevar=len(typevarlist)
#
    if ( ensembletypelist == None ) : 
        ensembletypelist = ['']*nexpid

    if ( len(expidlist) != len(ensembletypelist) ) :
        print('length expidlist : ', len(expidlist))
        print('length ensembletypelist : ', len(ensembletypelist))
        quit()


    print(variablelist)   

    print('description = ', description) 

#   all experiments use same variable
    if ( description == 'varcommon' ) : 

       print('CASE 1') 
      
       for variable in variablelist :

           tmpvarlist=[''] * nexpid
           
           for iexpid in range(0,nexpid) :  
               tmpvarlist[iexpid] = variable

           analyseseries.analyseseries(expidlist=expidlist,refidlist=refidlist,refid2list=refid2list,refid3list=refid3list,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=tmpvarlist,typevarlist=typevarlist,freqtype=freqtype,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist,ensembletypelist=ensembletypelist)
#   alle experiments use same typevar (glob,NH,SH,...)
    elif ( description == 'typevarcommon' ) :  
      
       print('CASE 2')

       for typevar in typevarlist :

           tmptypevarlist=[''] * nexpid
           
           for iexpid in range(0,nexpid) :  
               tmptypevarlist[iexpid] = typevar

           analyseseries.analyseseries(expidlist=expidlist,refidlist=refidlist,refid2list=refid2list,refid3list=refid3list,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=tmptypevarlist,freqtype=freqtype,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist,ensembletypelist=ensembletypelist)

#   alle experiments use same variable and typevar
    elif ( description == 'varcommon-typevarcommon' \
        or description == 'typevarcommon-varcommon' ) :  
      
       print('CASE 3')

       for variable in variablelist : 

           for typevar in typevarlist :

               tmpvarlist=[''] * nexpid
               tmptypevarlist=[''] * nexpid 
           
               for iexpid in range(0,nexpid) :  
                   tmpvarlist[iexpid] = variable
                   tmptypevarlist[iexpid] = typevar

               analyseseries.analyseseries(expidlist=expidlist,refidlist=refidlist,refid2list=refid2list,refid3list=refid3list,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=tmpvarlist,typevarlist=tmptypevarlist,freqtype=freqtype,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist,ensembletypelist=ensembletypelist)

#   experiments can use different variables
    elif (description == '' ) :

        print('CASE 4')

        if ( nexpid != nvar ) : exit(0)
        analyseseries.analyseseries(expidlist=expidlist,refidlist=refidlist,refid2list=refid2list,refid3list=refid3list,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist,ensembletypelist=ensembletypelist)

    else :
        print('No description recognized : ' + description)
        quit() 
