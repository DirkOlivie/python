import numpy as np
import math
import re

def readseriesnoresmemissions(file, freqtype):
#----------------------------
    '''
    INPUT
        file

    RETURN 
        structure containing time series

    '''
#
    if ( freqtype != 'YEA' ) :
        print('+++ readseriesnoresmemissions +++')
        print('Only YEA frequency available : ', freqtype)
        quit()
#
    Rearth=6370e3
    Aearth=4.*math.pi*Rearth*Rearth
#
    if   ( '_BC_AX_'  in file ) : species = 'BC_AX'
    elif ( '_BC_N_'   in file ) : species = 'BC_N'
    elif ( '_BC_NI_'  in file ) : species = 'BC_NI'
    elif ( '_OM_NI_'  in file ) : species = 'OM_NI'
    elif ( '_SO2_'    in file ) : species = 'SO2'
    elif ( '_SO4_PR_' in file ) : species = 'SO4_PR'
    else :
        print('+++ generateseriesnoresmemissions +++')
        print('No species recognized in file : ', file)
        quit()

    dir='/nird/home/olivie/code/python/cmip7-emissions-noresm/info'
    filename=dir+'/'+file+'.txt'
    f=open(filename)

    timelist=[]
    valuelist=[]

    for line in f:
#   print(repr(line))

        if ( 'UNITS=' in line ) : # units
            line=line.split("=")
            units=line[1].strip()    
        elif ( 'YEAR' in line ) :   
            line=line.strip()          # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            contentlist=line.split(" ")
            iyear=contentlist.index('YEAR')
            ivalue=contentlist.index('TOTAL')
        else :
            line=line.strip()       # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            content=line.split(" ")

            timelist.append(int(content[iyear]))
            valuelist.append(float(content[ivalue]))
#
    f.close()
#
#   CONVERT TO NUMPY ARRAY
    valuelist = np.array(valuelist,dtype=float)
    timelist = np.array(timelist,dtype=int)


#   SOME ADDITIONAL STATISTICS
    ntime=len(valuelist)
    Ex   = np.mean(valuelist)
    Exx  = np.mean(valuelist*valuelist)
    sigma = np.sqrt(Exx-Ex*Ex)
    error = sigma/np.sqrt(float(ntime))
#
    outdata = { 'expid'    : file, \
                'variable' : species, \
                'units'    : units, \
                'freqtype' : 'YEA', \
                'area'     : Aearth, \
                'areaglob' : Aearth, \
                'timelist'  : timelist, \
                'valuelist' : valuelist, \
                'ntime' : len(valuelist), \
#                additional statistics                  
                'Ex'    : Ex, \
                'Exx'   : Exx, \
                'sigma' : sigma, \
                'error' : error}
#
    return outdata















