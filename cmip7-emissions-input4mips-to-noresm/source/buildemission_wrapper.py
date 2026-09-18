'''
NAME


PURPOSE


'''
import cfilelocation
import buildemission
import sys

# arguments 
period=sys.argv[1]
species=sys.argv[2]
activity=sys.argv[3]
sectorliststring=sys.argv[4]
vertdist=sys.argv[5]
resolution=sys.argv[6]
vertintp=sys.argv[7]
version=sys.argv[8]
noresmversion=sys.argv[9]
scenario=sys.argv[10]
i4mpdownload_anthro=sys.argv[11]
i4mpdownload_bb=sys.argv[12]
overwrite=sys.argv[13]

weights_360x720_to_ne16pg3=sys.argv[14]
weights_360x720_to_ne30pg3=sys.argv[15]
weights_720x1440_to_ne16pg3=sys.argv[16]
weights_720x1440_to_ne30pg3=sys.argv[17]
topo_fv09=sys.argv[18]
topo_fv19=sys.argv[19]
topo_ne16pg3=sys.argv[20]
topo_ne30pg3=sys.argv[21]

# information on grid
filelocation=cfilelocation.CFileLocation( weights_360x720_to_ne16pg3  = weights_360x720_to_ne16pg3, \
                                              weights_360x720_to_ne30pg3  = weights_360x720_to_ne30pg3, \
                                              weights_720x1440_to_ne16pg3 = weights_720x1440_to_ne16pg3, \
                                              weights_720x1440_to_ne30pg3 = weights_720x1440_to_ne30pg3, \
# 
                                              topo_fv09    = topo_fv09, \
                                              topo_fv19    = topo_fv19, \
                                              topo_ne16pg3 = topo_ne16pg3, \
                                              topo_ne30pg3 = topo_ne30pg3)

# overwrite is interpreted as string during argument reading
# should be converted to 
if (   overwrite == 'True' )  : overwrite=True
elif ( overwrite == 'False' ) : overwrite=False
else :
    print('No overwrite recognized : ', overwrite)
    quit()

buildemission.buildemission(vertdist=vertdist,resolution=resolution,vertintp=vertintp, activity=activity,sectorliststring=sectorliststring,species=species,period=period, version=version, noresmversion=noresmversion, scenario=scenario, i4mpdownload_anthro=i4mpdownload_anthro, i4mpdownload_bb=i4mpdownload_bb, filelocation=filelocation, overwrite=overwrite)
