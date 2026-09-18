import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import calculate3dpressure

def convert2dpfull( psdata, tdata, var ) :
#---------------------------------------
    '''
    MODIFICATIONS
        (2024-06-10) creation

    INPUT 
        data : structure contains
        tdata : same structure as data ... (but for temperature)
        var : the variable it should become (e.g., tropoz "tropospheric ozone column")
        
    OUTPUT 

    '''

    print('+++ convert2dpfull +++')    

#   newdata will use framework from temperature
    data=tdata 

    field=calculate3dpressure.calculate3dpressure(p0=tdata['p0'],ps=psdata['field'],hyam=tdata['hyam'],hybm=tdata['hybm'])

    data['units'] = psdata['units'] # modify units
    data['field'] = field           # modify field value

#
    print('--- convert2dpfull ---')
#
    return data
