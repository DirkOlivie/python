import plotobservationfrequency

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

'''
    MODIFICATIONS
        (2023-10-20) Adding colorlist and colorscheme

'''

def loopobservationfrequency2(stationlist,representationtypelist,figlayout) :
#--------------------------------

#   loop over representationtype
    for representationtype in representationtypelist :    

        plotobservationfrequency.plotobservationfrequency(stationlist=stationlist,representationtype=representationtype,figlayout=figlayout)      

if __name__ == '__main__':
    main()
