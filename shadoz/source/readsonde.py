import numpy as np


def readsonde (sonde):
#---------------------
    '''
    MODIFICATIONA
        (2024-02-19) creation

    INPUT
        sonde : costarica_20120608T17_SHADOZV06.dat

    '''
#
#   extract station from sonde
    line=sonde.split('_')
    station=line[0]
#
#   
    filename='/projects/NS9560K/users/olivie/observations/shadoz/v20240209/'+station+'/'+sonde

    print(filename)

    f=open(filename,'r')

    readingdata=0 # will be put to one, once the last lie of header has been read

#    data=[]
    
    nvarmax=20
    nptmax=15000

    data=np.zeros([nvarmax,nptmax])

    ipt=0

    for line in f : 

        if ( 'Latitude (deg)' in line) : 
            line=line.split(':')
            latitude=float(line[-1])  
        elif ( 'Longitude (deg)' in line) : 
            line=line.split(':')
            longitude=float(line[-1])  
        elif ( ( 'Time' in line ) and ( 'Press' in line ) and ( 'GeopAlt' in line ) ) :            
            varlist=line.split()                   # no seperator argument : does not see leading/trailing blancs, multiple blancs count as one           
        elif ( ( 'sec' in line ) and ( 'hPa' in line ) and ( 'km' in line ) ) :        
            unitlist=line.split()
            readingdata=1
        elif (readingdata == 1) :  
            line=line.split()             
            line=[float(i) for i in line] # convert string to float
            
            n=len(line)
            for i in range(0,n) :
                if ( line[i] == 9000. ) :  
                    line[i]=float('nan')
            
 #           data.append(line) 
            data[0:n,ipt] = np.array(line)
            ipt=ipt+1

#   keep only section of matrix
    data=data[0:n,0:ipt]

    sondedata={'sonde'     : sonde, \
               'latitude'  : latitude, \
               'longitude' : longitude, \
               'varlist'   : varlist, \
               'unitlist'  : unitlist, \
               'data'      : data}   
#           
    return sondedata
