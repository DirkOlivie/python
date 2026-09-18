import numpy as np
import copy

import constructseriesnoresmghg

def analyseseriesnoresmghg(directory, filename, freqtype, specieslist):
#-------------------------
    '''
    INPUT
        directory
        filename
        freqtype

    CALLED BY
        analysenoresmemissions

    CALLS
        constructseriesnoresmemissions

    '''

#=============================
#
# 1. read 3D/4D data
#-------------------
#
    D = constructseriesnoresmghg.constructseriesnoresmghg(filename=directory+'/'+filename+'.nc', freqtype=freqtype, specieslist=specieslist)

# 2. write global totals
#======================= 
#
    f=open('../info/globalseries_'+freqtype+'_'+filename+'.txt','w')

    nvar=len(D)

#   variables in alphabetical order        
    varlist = []
    for ivar in range(nvar) :
        varlist.append(D[ivar]['variable'])
#   orderedvarlist = varlist.sort() 
    orderedvarlist = sorted(varlist) 
    print(nvar)
    print(varlist)
    print(orderedvarlist)


#   write units
    f.write('UNITS='+D[0]['units'])
    f.write('\n')

#   write header line
#       
    f.write('YEAR')
#    for ivar in range(0,nvar) :         
#        f.write(' ')                 # one blanco space
#        f.write(D[ivar]['variable'])
#    f.write('\n')
    
    for var in orderedvarlist :         
        f.write(' ')                 # one blanco space
        f.write(var)
    f.write('\n')

#   loop over times
    for itime in range(D[0]['ntime']) :
#       write DATE
        if   ( freqtype == 'YEA'     ) : f.write(str("%4.4i"% D[0]['timelist'][itime]))      # 4 digits for integer year
        elif ( freqtype == 'monthly' ) : f.write(str("%07.2f"% D[0]['timelist'][itime]))  # xxxx.xx for decimal year
        else :
            print('+++ analyseseriesnoresmghg +++')
            print('No freqtype recognized : ', freqtype)
            quit()

#       write seperate values
#        for ivar in range(nvar) :
#            f.write(' '+str("%13.6e"% D[ivar]['valuelist'][itime]))

#       write seperate values
        for var in orderedvarlist :
            ivar = varlist.index(var)
            f.write(' '+str("%18.12e"% D[ivar]['valuelist'][itime]))
            f.write(' '+str("%18.12e"% D[ivar]['valuelist'][itime]))

#       end of line
        f.write('\n')

    f.close()
