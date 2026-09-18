import numpy as np
import copy

import constructseriesnoresmemissions

def analyseseriesnoresmemissions(directory, filename, freqtype):
#-------------------------------
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
    D, P = constructseriesnoresmemissions.constructseriesnoresmemissions(filename=directory+'/'+filename+'.nc', freqtype='YEA')

# 2. write global totals
#======================= 
#
    f=open('../info/globalseries_'+freqtype+'_'+filename+'.txt','w')

    nvar=len(D)

#   write units
    f.write('UNITS='+D[0]['units'])
    f.write('\n')

#   write header line
    f.write('YEAR')
    for ivar in range(0,nvar) :         
        f.write(' ')                 # one blanco space
        f.write(D[ivar]['variable'])
    f.write(' ')
    f.write(' TOTAL')
    f.write('\n')

#   loop over times
    for itime in range(D[0]['ntime']) :
#       write DATE
        f.write(str("%4.4i"% D[ivar]['timelist'][itime]))

#       write seperate values
        for ivar in range(nvar) :
            f.write(' '+str("%13.6e"% D[ivar]['valuelist'][itime]))

#       write TOTAL
        totvalue = 0.
        for ivar in range(nvar) :
            totvalue = totvalue + D[ivar]['valuelist'][itime]
        f.write(' '+str("%13.6e"% totvalue ) )

#       end of line
        f.write('\n')

    f.close()
# 
# 3. write global profile
#========================
#
    proftypelist=['globalprofile', 'globalnormalizedprofile']

    if ( P[0] != None ) :

        for proftype in proftypelist : 

            if   ( proftype == 'globalprofile'           ) : 
                TMP = P
            elif ( proftype == 'globalnormalizedprofile' ) : 
                TMP = copy.deepcopy(P)
                for ivar in range(nvar) :
                    TMP[ivar]['valuelist'][:] = P[ivar]['valuelist'][:] / ( np.max(P[ivar]['valuelist'][:]) + 1.e-40 )
                    TMP[ivar]['units'] = '1'
            else :
                print('+++ analysenoresmemissions +++')
                print('No proftype recognized : ', proftype)
                quit()

            f=open('../info/'+proftype+'_'+freqtype+'_'+filename+'.txt','w')

            nvar=len(TMP)

#           write units
            f.write('UNITS='+TMP[0]['units'])
            f.write('\n')

#           write units
            f.write('HEIGHTUNITS='+TMP[0]['altitude_units'])
            f.write('\n')

#           write header line
            f.write('LEVEL')
            f.write(' ')
            f.write('HEIGHTBOT')
            f.write(' ')
            f.write('HEIGHTMID')
            f.write(' ')
            f.write('HEIGHTTOP')
            for ivar in range(0,nvar) :
                f.write(' ')                 # one blanco space
                f.write(TMP[ivar]['variable'])
            f.write(' ')
            f.write(' TOTAL')
            f.write('\n')

            for ilev in range(len(TMP[0]['altitude'])) :
#               write DATE
                f.write(    str("%2i"% ilev))                             # LEVEL
                f.write(' '+str("%13.6e"% TMP[0]['altitude_int'][ilev]))    # HEIGHTBOT
                f.write(' '+str("%13.6e"% TMP[0]['altitude'][ilev]))        # HEIGHTMID
                f.write(' '+str("%13.6e"% TMP[0]['altitude_int'][ilev+1]))  # HEIGHTTOP

#               write seperate values
                for ivar in range(nvar) :
                    f.write(' '+str("%13.6e"% TMP[ivar]['valuelist'][ilev])) # seperate value

#               write TOTAL
                totvalue = 0.
                for ivar in range(nvar) :
                    totvalue = totvalue + TMP[ivar]['valuelist'][ilev]   # sum over all sectors
                f.write(' '+str("%13.6e"% totvalue ) )

                f.write('\n')

            f.close()




