import re
import numpy as np

def readaerocomascii(origin, activity, sector, species):
#--------------------------
    '''
    REMARK :
        1) I APPLIED A HALD DEGREE SHIFT (I hope that is correct) Is that needed
        2) original units in ascii file : kg SO2/yr

    INPUT
        origin
        activity
        sector   : 'CONT' or 'EXPL'
        species

    RETURN data structure containing

    CALLED BY
        intpvolcano

    CALLS

    MODIFICATIONS
        (2025-01-08) storeA -> storeB
        (2025-10-18) correction : last 3 volcanoes were forgotten by wrong implementation of skipping of 3 lines

    '''
    print, sector

    if (   sector == 'CONT' ) : filename='/nird/datalake/NS2345K/olivie/emissions-auxiliary/volc/continuous_volc.1x1.ascii'
    elif ( sector == 'EXPL' ) : filename='/nird/datalake/NS2345K/olivie/emissions-auxiliary/volc/explosive_volc.1x1.ascii'
    else :
        print('No sector recognized : ', sector)    
        quit()

#   initialize data structures
    nmax=300
    lonlist        = np.zeros((nmax), dtype=float)
    latlist        = np.zeros((nmax), dtype=float)
    emissionlist   = np.zeros((nmax), dtype=float)
    height_low     = np.zeros((nmax), dtype=float)
    height_high    = np.zeros((nmax), dtype=float)
    topographylist = np.zeros((nmax), dtype=float)
#
#   READ THE FILE AND PUT ALL LINES IN LIST "FIN"
#   empty list
    fin=[]

#   read first fig
    fid  = open(filename, 'r')
    for line in fid:
        fin.append(line)
    fid.close()
#
#   number of lines
    nline= len(fin)

#   skip first 3 lines
    for i in range(3,nline) :

        line=re.sub(r'\s+', ' ',fin[i]).strip()  # REPLACE : 1) sub : replace multiple blanc spaces "\s" by only one ; 2) strip : remove leading/trailing blancs
        line = line.split(' ')        

        lonlist[i-3]      = ( float(line[0]) + 0.5 + 720. ) % 360. # modulo
        latlist[i-3]      =   float(line[1]) + 0.5
        emissionlist[i-3] =   float(line[2]) * 1.e-9       # kg/yr -> Tg/yr
        height_low[i-3]   =   float(line[3])
        height_high[i-3]  =   float(line[4])

        if ( height_low[i-3] == height_high[i-3] ) :

            print('increasing height_high for lon, lat = ', lonlist[i-3], latlist[i-3])
            height_high[i-3] = height_low[i-3] + 10. # add 10 [m] 
#
    n=nline-3
#
#   DATA STRUCTURE : emissions are assumed in Tg[SO2]/yr
    data={'origin'      : origin, \
          'activity'    : activity, \
          'sector'      : sector, \
          'species'     : species, \
          'lonlist'     : lonlist[0:n], \
          'latlist'     : latlist[0:n], \
          'emistotlist' : emissionlist[0:n], \
          'height_low'  : height_low[0:n],\
          'height_high' : height_high[0:n], \
          'n'           : n }
#
    return data
