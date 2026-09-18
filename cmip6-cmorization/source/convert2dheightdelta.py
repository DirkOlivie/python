import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import calculate3dheightdelta

def convert2dheightdelta( psdata, tdata, var ) :
#---------------------------------------
    '''
    MODIFICATIONS
        (2024-06-10) creation

    INPUT 
        data : structure contains
        tdata : same structure as data ... (but for temperature)
        var : the variable it should become (e.g., tropoz "tropospheric ozone column")
        
    OUTPUT structure containing

    '''

    print('+++ convert2dheightdelta +++')    

#   newdata will use framework from temperature
    data=tdata 

    field=calculate3dheightdelta.calculate3dheightdelta(p0=tdata['p0'],ps=psdata['field'],t=tdata['field'],hyam=tdata['hyam'],hybm=tdata['hybm'],hyai=tdata['hyai'],hybi=tdata['hybi'])

    data['var']   = 'layer thickness'  
    data['field'][:,:,:] = field[:,:,:]
    data['units'] = 'm'
#
    print('--- convert2dheightdelta ---')
#
    return data
