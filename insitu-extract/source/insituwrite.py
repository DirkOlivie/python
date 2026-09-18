def insituwrite(D, location) :
#----------------------
#
    expid=D['expid']
    variable=D['variable']
    units=D['units']
    ntime=D['ntime']
#    
    filename='/nird/home/olivie/output/insitu-extraction/'+variable+'_'+location+'_'+expid+'.txt'
    f=open(filename,'w')
#   writing to file 
    f.write('VAR=')   ; f.write(variable) ; f.write('\n')
    f.write('UNITS=')   ; f.write(units) ; f.write('\n')
    f.write('EXPID=') ; f.write(expid)    ; f.write('\n')
    f.write('LOCATION=') ; f.write(location)    ; f.write('\n')
    for itime in range(ntime) :
            f.write(str("%4.4i"% D['yearlist'][itime]))
            f.write(' ')
            f.write(str("%2.2i"% D['monthlist'][itime]))
            f.write(' ')
            f.write(str("%13.6e"% D['valuelist'][itime]))
            f.write('\n')

    f.close()

