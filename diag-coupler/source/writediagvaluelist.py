import math

def writediagvaluelist(expid, component, variable, budgettype, freqtype, data):
#---------------------
    '''



    '''
    path = "/datalake/NS2345K/olivie/output/timeblocks-v2/"+expid

    cvar='diag'+variable+budgettype+component

    filename=path+'/'+cvar+'.'+expid+'.h0.globav.txt'

    f=open(filename,'w')

    regionlist=('','glob')

#   HEADING
#   variable
    f.write('VAR=')
    f.write(cvar)    #varout
    f.write('\n')
#   units
    f.write('UNIT=')
    f.write(data['units'])
    f.write('\n')
#   fileorigin
    f.write('FILEORIGIN=NorESM2output')
    f.write('\n')
#   area size
    f.write('AREA= ')
    for tmpregion in regionlist :
        c = str("%13.6e"% (4.*math.pi*6.37e6*7.37e6))
        f.write(str(c)+' ')
    f.write('\n')
#   areaunit
    f.write('AREAUNIT= m2')
    f.write('\n')
#   heading with YYYY MMM  
    f.write('YYYY= ')
    f.write('MM= ')
    for region in regionlist :
        f.write('VALUE'+region+'= ')  # write name of region
    f.write('\n')

#   write actual values
    for itime in range(data['ntime']) :

        f.write(str("%4.4i"% (data['yearlist'][itime]))+' ')
        f.write(str("%2.2i"% (data['monthlist'][itime]))+' ')

        for region in regionlist :
            f.write(str("%13.6e"% (data['valuelist'][itime]))+' ')

        f.write('\n')
        
    f.close()
