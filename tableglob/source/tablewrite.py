import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import expidlist2expidshortlist


def tablewrite(code, expidAlist, expidBlist, varlist, matrix, errormatrix, unitslist, stattypelist, orientation, myformat) :
#--------------
    '''
    myformat = "{0:.3f}", "{0:.5e}"

    MODIFICATIONS
        (2025-03-05) : added errormatrix

    INPUT
        code
        expidAlist
        expidBlist
        varlist
        matrix
        unitslist
        stattypelist
        orientatlion : 'y(exp)-x(var)' | 'y(var)-x(exp)'


    '''

#    print('BEFORE')
#    print(expidAlist)
    expidAlist = expidlist2expidshortlist.expidlist2expidshortlist(expidAlist)    
    expidBlist = expidlist2expidshortlist.expidlist2expidshortlist(expidBlist)    
#    print('AFTER')
#    print(expidBlist)

    nexpid=len(expidAlist)
    nvar=len(varlist)


    filename='../info/output/'+code+'.txt'

    print(myformat)


    f=open(filename,'w')

    if ( orientation == 'y(exp)-x(var)') : 

#       list of variable names        
        f.write("{:122s}".format(''))                       # 122 blanco spaces 
        for var in varlist:
            print(var)
            f.write("{:20s}".format(var))                   # 20 spaces for variable name
            f.write(' ')                                    # 1 blanco space 
        f.write('\n')
 
#       list of units
        f.write("{:122s}".format(''))                       # 122 blanco spaces 
        for units in unitslist:
            print(units)
            f.write("{:20s}".format(units))                 # 20 spaces for units
            f.write(' ')                                    # 1 blanco space 
        f.write('\n')
 
#
        for iexpid in range(0,nexpid) :
            expA=expidAlist[iexpid]
            expB=expidBlist[iexpid]

            f.write("{:60s}".format(expA[:60]))             # 60 spaces for experiment name    
            f.write(' ')                                    # 1 blanco space
            f.write("{:60s}".format(expB[:60]))             # 60 spaces for experiment name 
            f.write(' ')                                    # 1 blanco space

            for ivar in range(0,nvar) :
                c=myformat.format(matrix[iexpid,ivar])
                d=myformat.format(errormatrix[iexpid,ivar])

                if ( stattypelist[iexpid] == 'mean' \
                  or stattypelist[iexpid] == 'standard_deviation' \
                  or stattypelist[iexpid] == 'error_on_mean' ) : 
                    f.write("{:20s}".format(c))                  # 20 spaces for numerical value
                    f.write(' ')                                 # 1 blanco space
                elif ( stattypelist[iexpid] == 'mean+standard_deviation' \
                    or stattypelist[iexpid] == 'mean+error_on_mean' ) :
                    f.write("{:9s}".format(c))                  # 20 spaces for numerical value
                    f.write('+-')
                    f.write("{:9s}".format(d))                  # 20 spaces for numerical value
                    f.write(' ')
      
            f.write('\n')

    elif ( orientation == 'y(var)-x(exp)') : 

        f.write("{:42s}".format(''))                        # 21 blanco spaces 
        for expid in expidAlist:
            print(expid)
            f.write("{:20s}".format(expid[:20]))                 # 20 spaces for variable name
            f.write(' ')                                    # 1 blanco space 

        f.write('\n')

        f.write("{:42s}".format('')) 
        for expid in expidBlist:
            print(expid)
            f.write("{:20s}".format(expid[:20]))                 # 20 spaces for variable name
            f.write(' ')                                    # 1 blanco space 

        f.write('\n')
 

        for ivar in range(0,nvar) :
            var=varlist[ivar]

            f.write("{:20s}".format(var[:20]))             # 20 spaces for variable name    
            f.write(' ')                                    # 1 blanco space

            units=unitslist[ivar]

            f.write("{:20s}".format(units[:20]))             # 20 spaces for variable name    
            f.write(' ')                                    # 1 blanco space

            test="{0:.5e}"
            print(test)
            print(myformat) 

            for iexpid in range(0,nexpid) :
                c=myformat.format(matrix[iexpid,ivar])
                d=myformat.format(errormatrix[iexpid,ivar])

                if ( stattypelist[iexpid] == 'mean' \
                  or stattypelist[iexpid] == 'standard_deviation' \
                  or stattypelist[iexpid] == 'error_on_mean' ) :
                    f.write("{:20s}".format(c))                  # 20 spaces for numerical value
                    f.write(' ')                                 # 1 blanco space
                elif ( stattypelist[iexpid] == 'mean+standard_deviation' \
                    or stattypelist[iexpid] == 'mean+error_on_mean' ) :
                    f.write("{:9s}".format(c))                  # 20 spaces for numerical value
                    f.write('+-')
                    f.write("{:9s}".format(d))                  # 20 spaces for numerical value
                    f.write(' ')
 
            f.write('\n')

    f.close()
