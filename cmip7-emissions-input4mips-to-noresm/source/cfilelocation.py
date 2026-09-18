'''
     https://docs.python.org/3/tutorial/classes.html

    AIM
        Contains filenames for 
            regridding from one grid to another
            topography
            grid itself : will be used from topograpy fiel


'''
class CFileLocation:
    def __init__(self, weights_360x720_to_ne16pg3=None, \
                       weights_360x720_to_ne30pg3=None, \
                       weights_720x1440_to_ne16pg3=None, \
                       weights_720x1440_to_ne30pg3=None, \
# 
                       topo_fv09=None, \
                       topo_fv19=None, \
                       topo_ne16pg3=None, \
                       topo_ne30pg3=None): 
#
            self.weights_360x720_to_ne16pg3  = weights_360x720_to_ne16pg3
            self.weights_360x720_to_ne30pg3  = weights_360x720_to_ne30pg3
            self.weights_720x1440_to_ne16pg3 = weights_720x1440_to_ne16pg3
            self.weights_720x1440_to_ne30pg3 = weights_720x1440_to_ne30pg3
# 
            self.topo_fv09    = topo_fv09
            self.topo_fv19    = topo_fv19
            self.topo_ne16pg3 = topo_ne16pg3
            self.topo_ne30pg3 = topo_ne30pg3

    def topofile(self, grid):
        if   ( grid == '0.9x1.25' ) : filename=self.topo_fv09 
        elif ( grid == '1.9x2.5' )  : filename=self.topo_fv19
        elif ( grid == 'ne16pg3' )  : filename=self.topo_ne16pg3
        elif ( grid == 'ne30pg3' )  : filename=self.topo_ne30pg3
        else :
            print('+++ CFileLocation +++')
            print('No grid recognized : ', grid)
            quit()

        return  filename

    def weightfile(self, gridin, gridout) :
        if   ( gridin == '360x720'  and gridout == 'ne16pg3' ) : filename=self.weights_360x720_to_ne16pg3
        elif ( gridin == '360x720'  and gridout == 'ne30pg3' ) : filename=self.weights_360x720_to_ne30pg3
        elif ( gridin == '720x1440' and gridout == 'ne16pg3' ) : filename=self.weights_720x1440_to_ne16pg3
        elif ( gridin == '720x1440' and gridout == 'ne30pg3' ) : filename=self.weights_720x1440_to_ne30pg3
        else :
            print('+++ CFileLocation +++')
            print('No gridin or gridout recognized : ', gridin, gridout)
            quit()

        return filename
