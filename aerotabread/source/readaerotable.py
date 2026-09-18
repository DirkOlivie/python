import numpy as np
import re

def readaerotable (version, shortfilename) :
#-------------------------
    '''
    MODIFICATIONS
        (2022-07-04) : creation
    '''

    print('+++ readaerotable +++')

    filename='/scratch/olivie/noresm-inputdata/noresm-only/atm/cam/camoslo/'+version+'/'+shortfilename

#   ALL X-DIMENSIONS OF THE TABLE 
    ndimmax=7                            # max. possible number of dimensions    
    nxmax=16                             # max. size of a dimension
    xvaluelist=np.zeros([ndimmax,nxmax]) # create empty array

#   waveband number dependency : always present in file, but not explicitly mentioned in heading
    dimnamelist=['iband']                # dimnamelist will be list containing all dimension names, starting with wavelength; array will be incremented when other dimensions are read
    dimsizelist=[14]                     # dimsizelist will be list containg length of dimensions , starting with wavelength; array will be incremented when other dimensions are read
    xvaluelist[0,0:14] = np.arange(0,14) # will contain discrete x-values for each dimension, starting with wavelength
    ndim=1
#
    addingdimension=False
    addingdimensionNext=False
    readingdata=False
    readingdataNext=False

    f=open(filename)  # open AeroTab file
    
    for line in f : 
#       
#        print('1',addingdimension,addingdimensionNext)

        if ( addingdimensionNext == True ) : 
            addingdimension = True
            addingdimensionNext = False

        if ( readingdataNext == True ) : 
            readingdata = True
            readingdataNext = False

#        print('2',addingdimension,addingdimensionNext) 


        if ( 'X-CHECK ' in line and ' =' in line ) :
           print('Trying do detect X-CHECK xxxx =')
           line = line.strip()     # remove leading and trailing blanks
           print('Removing leading and trailing blanks')
           line=re.sub(' +', ' ', line) # reduce to only one blank
           line=line.split(" ")    # split

           if ( line[1] in ['catot','fac','faq','fbc','fombg','relh'] ) :
               print('Recognized new dimension : '+line[1])
               dimnamelist.append(line[1])
               addingdimensionNext=True

#        print('3',addingdimension,addingdimensionNext)
           
        if ( addingdimension == True ) :   # line like 0.0000E+00 0.2000E+00 0.4000E+00 0.6000E+00 0.8000E+00 0.1000E+01
#           print(line)  
           line = line.strip()     # remove leading and trailing blanks 
           line=re.sub(' +', ' ', line) # reduce to only one blank
           line = line.split(' ')
           dimsizelist.append(len(line))
           for i in np.arange(0,len(line)) : 
              xvaluelist[ndim,i] = float(line[i])
           addingdimension=False
           ndim=ndim+1

#       read one line just before actual data
        if ( 'X-CHECK LUT: table values to be used for look-ups and interpolations in CAM5-Oslo:' in line ) :
           readingdataNext = True
           print('ndim : ', ndim)
           print('dimsizelist : ', dimsizelist)
            
#          dimensionality of arrays to be read : counterlist will indicate which element of array is being read
           if (ndim==5) : counterlist=[0,0,0,0,0]
           if (ndim==6) : counterlist=[0,0,0,0,0,0]

#          prepare arrays to be filled
           omega=np.zeros(dimsizelist)
           gass=np.zeros(dimsizelist)
           bext=np.zeros(dimsizelist)
           kext=np.zeros(dimsizelist)

#       read lines with actual data
        if ( readingdata == True ) : 
           line = line.strip()     # remove leading and trailing blanks 
           line=re.sub('\s+', ' ', line)  # reduce to only one blank 
           line=line.split(' ')    # split, based on blanks           
#           print(counterlist) 

           omega[counterlist[0],counterlist[1],counterlist[2],counterlist[3],counterlist[4]] = line[1+ndim]
           gass[counterlist[0],counterlist[1],counterlist[2],counterlist[3],counterlist[4]] = line[1+ndim+1]
           bext[counterlist[0],counterlist[1],counterlist[2],counterlist[3],counterlist[4]] = line[1+ndim+2]
           kext[counterlist[0],counterlist[1],counterlist[2],counterlist[3],counterlist[4]] = line[1+ndim+3]
#
#          increase current dimension in counterlist + possibly increase other dimensions
           counterlist[0] = counterlist[0] + 1  # waveband is most fast varying

           if ( counterlist[0] == 14 ) :
               counterlist[0] = 0
               counterlist[ndim-1] = counterlist[ndim-1] + 1

               for idim in np.flip(np.arange(0,ndim-1))+1 : # inverse order of non-wavelength dimensions  
                   if ( counterlist[idim] == dimsizelist[idim] ) : 
                       counterlist[idim] = 0                       # current dimension : set to 0    
                       counterlist[idim-1] = counterlist[idim-1] +1 # earlier dimemsion : increase by 1

#   close file
    f.close() 

#    print(omega.shape)
    print(omega[0,0,0,0,0])
    print(omega[dimsizelist[0]-1,dimsizelist[1]-1,dimsizelist[2]-1,dimsizelist[3]-1,dimsizelist[4]-1])
    print(omega[dimsizelist[0]-1,0,0,dimsizelist[3]-1,dimsizelist[4]-1])

    print('SHAPE')
    print(omega.shape)

    data = { 'bext' : bext, \
             'units' : 'km-1', \
             'dimnamelist' : dimnamelist, \
             'dimsizelist' : dimsizelist, \
             'xvaluelist'  : xvaluelist[0:ndim,:], \
             'ndim'        : ndim }
           
    print('--- readaerotable ---')

    return data
