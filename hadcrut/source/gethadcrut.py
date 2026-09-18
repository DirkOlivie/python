import numpy as np

def gethadcrut ():
#-----------------

    filename='/nird/home/olivie/code/python/hadcrut/info/input/HadCRUT.5.0.2.0.analysis.summary_series.global.annual.csv'

    f=open(filename)

    yearlist  = []
    valuelist = []
    minlist   = []
    maxlist   = []

    for line in f:

        line=line.strip()     # remove blanks and end-of-line (\n) symbols
        line=line.split(",")

        print(line)

        if ( 'Time' == line[0] ) :  

            ipos_year  = line.index('Time')
            ipos_value = line.index('Anomaly (deg C)')
            ipos_min   = line.index('Lower confidence limit (2.5%)')
            ipos_max   = line.index('Upper confidence limit (97.5%)')  # including end of line symbol
            heading_ok=True 

        elif ( heading_ok ) : 
             
            yearlist.append( float(line[ipos_year]))     # float : to convert from string to real 
            valuelist.append(float(line[ipos_value]))
            minlist.append(  float(line[ipos_min ]))
            maxlist.append(  float(line[ipos_max ]))   

        else : 
            print('Something went wrong during reading HadCrut data')
            quit()

    f.close()

#   create a dictionary
    data={''
          'units'     : 'deg_C', \
          'yearlist'  : np.array(yearlist), \
          'valuelist' : np.array(valuelist), \
          'minlist'   : np.array(minlist), \
          'maxlist'   : np.array(maxlist), \
          'ntime'     : len(yearlist)}

    return data
