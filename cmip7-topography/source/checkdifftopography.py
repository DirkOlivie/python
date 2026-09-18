import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc


def checkdifftopography(file0, file1) :
#----------------------

    field0=readnc.readnc('PHIS', file0)
    field1=readnc.readnc('PHIS', file1)

    print('Field0 (min, max) : ', np.min(field0), np.max(field0))
    print('Field1 (min, max) : ', np.min(field1), np.max(field1))
    print('Field0-field1 (min, max) : ', np.min(field0-field1), np.max(field0-field1))
