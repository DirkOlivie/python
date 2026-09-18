import numpy as np
import extractexpinfo
import gettablevalue
import tablewrite

def tableanalyse (code,expdeflist,varlist,orientation,myformat) :
#---------------    
    ''' 
    MODIFICATIONS
	(2021-11-26) : creation
        (2023-11-07) : extension of allowed possibilities
            mean
            standard_deviation 
            error_on_mean
        (2025-03-05) : added errormatrix to be passed to tablewrite
        (2025-03-05) : added stattypelist to be passed to tablewrite

    INPUT
        code
        expdeflist : list of [..., '<expid>/<refexpid/1/-1/1990-1995-YEA/1990-1995-YEA/...', ...>
        varlist
        orientation
        myformat

    CALLS
        extractexpinfo
        gettablevalue   
        tablewrite
    '''
#
#    
    nvar=len(varlist)
    nexpid=len(expdeflist)
#
    expidAlist=[]
    expidBlist=[]
    unitslist=[]
    stattypelist=[]

#   fill table
    matrix=np.zeros((nexpid,nvar))
    errormatrix=np.zeros((nexpid,nvar))
        
    for iexpid in range(0,nexpid) :   

        info = extractexpinfo.extractexpinfo(expdef=expdeflist[iexpid]) # gives inormation whether 'mean', 'standard_deviation', 'error_on_mean'

        expidAlist.append(info["expA"])
        expidBlist.append(info["expB"])


        stattype=info["xdiff"]  # type of statistics you want to apply : 'mean', 'standard_deviation', 'error_on_mean'
        n=info["n"]             # number of experiments contributing in xdiff

#       fill the stattype list
        stattypelist.append(stattype)

        for ivar in range(0,nvar) : 

#           read datasets
            if ( n >= 1 ) :
                tmp, units = gettablevalue.gettablevalue(var=varlist[ivar], expid=info["expA"], year0=info["yrA0"], year1=info["yrA1"],season=info["seasonA"], stattype=stattype)                
                valuelist  =            tmp*info["wA"]
            if ( n >= 2 ) : # (B)
                tmp, units = gettablevalue.gettablevalue(var=varlist[ivar], expid=info["expB"], year0=info["yrB0"], year1=info["yrB1"],season=info["seasonB"], stattype=stattype)                
                valuelist = valuelist + tmp*info["wB"]
            if ( n >= 3 ) :
                tmp, units = gettablevalue.gettablevalue(var=varlist[ivar], expid=info["expC"], year0=info["yrC0"], year1=info["yrC1"],season=info["seasonC"], stattype=stattype)                
                valuelist = valuelist + tmp*info["wC"]
            if ( n >= 4 ) :
                tmp, units = gettablevalue.gettablevalue(var=varlist[ivar], expid=info["expD"], year0=info["yrD0"], year1=info["yrD1"],season=info["seasonD"], stattype=stattype)                
                valuelist = valuelist + tmp*info["wD"]         

#           fill the unitslist
            if ( iexpid == 0 ) : unitslist.append(units)

#           fill the matrix
            if   ( stattype == 'mean' \
                or stattype == 'mean+standard_deviation' \
                or stattype == 'mean+error_on_mean' ) : matrix[iexpid,ivar] = valuelist.mean()
            elif ( stattype == 'standard_deviation' ) : matrix[iexpid,ivar] = valuelist.std() 
            elif ( stattype == 'error_on_mean'      ) : matrix[iexpid,ivar] = valuelist.std() / np.sqrt(float( len(valuelist) - 1 ) )
            else : 
                print('No stattype recognized : '+stattype)
                print('--- gettablevalue ---')
                quit()

#           fill the errormatrix
            if   ( stattype == 'mean')                     : print('Nothing to do ...')
            elif ( stattype == 'mean+standard_deviation' ) : errormatrix[iexpid,ivar] = valuelist.std() 
            elif ( stattype == 'mean+error_on_mean'      ) : errormatrix[iexpid,ivar] = valuelist.std() / np.sqrt(float( len(valuelist) - 1 ) )
            elif ( stattype == 'standard_deviation' )      : print('Nothing to do ...')
            elif ( stattype == 'error_on_mean' )           : print('Nothing to do ...')  

            else : 
                print('No stattype recognized : '+stattype)
                print('--- gettablevalue ---')
                quit()
           
#            if (   info["xdiff"] == 'mean'               ) : matrix[iexpid,ivar] = tmpA * info["wA"] + tmpB * info["wB"]
#            elif ( info["xdiff"] == 'standard_deviation' ) : matrix[iexpid,ivar] = ( tmpA + tmpB ) / np.sqrt(2.)           # combine the uncertainties
#            elif ( info["xdiff"] == 'error_on_mean'      ) : matrix[iexpid,ivar] = ( tmpA + tmpB ) / np.sqrt(2.)           # combine the uncertainties
#            else :
#                   print('No xdiff recognized : '+xdiff) 
#                   print('--- tableanalyse ---')
#                   quit()
  
    print(matrix)

#   write table 
    tablewrite.tablewrite(code=code, expidAlist=expidAlist, expidBlist=expidBlist, varlist=varlist, matrix=matrix, errormatrix=errormatrix, unitslist=unitslist, stattypelist=stattypelist, orientation=orientation, myformat=myformat)
