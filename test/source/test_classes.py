#import cfilelocation
import cfiglayin
#import cfilelocation


import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-input4mips-to-noresm/source')
import cfilelocation


#figlayout=cfiglayout.CFigLayout(xrange=[0.,300.])
figlayin=cfiglayin.CFigLayin(xrange=[0.,300.],xtype='hallo')
filelocation=cfilelocation.CFileLocation(grid_fv19='alpha',grid_fv09='beta')

#a=filelocation.my_nethod()

#print(a)

#filelocation=cfilelocation.CFileLocation(alpha='a')
