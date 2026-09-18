import analysedistribution
#
def loopanalysedistribution2(expidlist, refidlist, wlist, varlist, typevarlist, timedescriptionlist, finalresolutionlist, legendlist, distributiontype, figlayoutlist, code):
#---------------------------    
#
    print('+++ loopanalysedistribution2 +++')
    print('--- loopanalysedistribution2 ---') 

    if ( len(expidlist) != len(refidlist) \
      or len(expidlist) != len(varlist) \
      or len(expidlist) != len(typevarlist) \
      or len(expidlist) != len(timedescriptionlist) \
      or len(expidlist) != len(legendlist) \
      or len(wlist)     != 2 ) : 
        print('expidlist           : ', len(expidlist))
        print('refidlist           : ', len(refidlist))
        print('varlist             : ', len(varlist))
        print('typevarlist         : ', len(typevarlist))
        print('timedescriptionlist : ', len(timedescriptionlist))
        print('legendlist          : ', len(legendlist))        
        exit()
#   
    analysedistribution.analysedistribution(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, timedescriptionlist=timedescriptionlist, finalresolutionlist=finalresolutionlist, legendlist=legendlist, distributiontype=distributiontype, figlayoutlist=figlayoutlist, code=code)   
