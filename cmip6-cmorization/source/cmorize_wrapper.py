'''
NAME


PURPOSE


'''

import cmorize
import sys


expid=sys.argv[1]
var=sys.argv[2]
version=sys.argv[3]
overwrite=sys.argv[4]

# overwrite is interpreted as string during argument reading
# should be converted to 
if ( overwrite == 'True' ) :
    overwrite=True
elif ( overwrite == 'False' ) :
    overwrite=False
else :
    print('No overwrite recognized : ', overwrite)
    quit()

print(expid)
print(var)

cmorize.cmorize(expid=expid, var=var, version=version, overwrite=overwrite) 
