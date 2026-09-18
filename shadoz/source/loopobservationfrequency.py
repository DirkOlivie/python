import loopobservationfrequency2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

'''
    MODIFICATIONS
        (2023-10-20) Adding colorlist and colorscheme

'''

def main() :
#-----------

    figlayout=cfiglayout.CFigLayout(code='standard')

#   observations
    stationlist=['ascen', \
                 'costarica', \
                 'fiji', \
                 'hanoi', \
                 'hilo', \
                 'irene', \
                 'java', \
                 'kuala', \
                 'nairobi', \
                 'natal', \
                 'paramaribo', \
                 'reunion', \
                 'samoa', \
                 'sancrist']

#   representation
    representationtypelist=['series_annual','series_monthly','seasonal_cycle'] 


    print(stationlist)

    loopobservationfrequency2.loopobservationfrequency2(stationlist=stationlist,representationtypelist=representationtypelist,figlayout=figlayout)      

if __name__ == '__main__':
    main()
