import buildoxidantsloop2


def main():
#---------------------------------
    '''
    CALLS
        buildoxidantsloop2

    REMARK :

    '''

#   I. piControl climatology
#---------------------------
#   version='version20260903'
    version='version20260912'

    time_units='days since 1850-01-01'
    calendar='noleap'

#   1. oxidants
    bctype='oxidants' ; specieslist=['O3','OH','NO3','HO2','HALONS']
    expiddescriptionlist = [ { 'year' : 1850, 'expid' : 'NF1850norbc_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'}]
#
#   overwrite=False
    overwrite=True
#
    buildoxidantsloop2.buildoxidantsloop2(bctype=bctype, specieslist=specieslist, expiddescriptionlist=expiddescriptionlist, time_units=time_units, calendar=calendar, version=version, overwrite=overwrite)

#   2. ch4 -> h2o
    bctype='emish2o' ; specieslist=['H2O_EMIS']
    expiddescriptionlist = [ { 'year' : 1850, 'expid' : 'NF1850norbc_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'}]
#
#   overwrite=False
    overwrite=True
#
#    buildoxidantsloop2.buildoxidantsloop2(bctype=bctype, specieslist=specieslist, expiddescriptionlist=expiddescriptionlist, time_units=time_units, calendar=calendar, version=version, overwrite=overwrite)

#   3. ozone
    bctype='ozone' ; specieslist=['O3']
    expiddescriptionlist = [ { 'year' : 1850, 'expid' : 'NF1850norbc_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'}]
#
#   overwrite=False
    overwrite=True
#
#    buildoxidantsloop2.buildoxidantsloop2(bctype=bctype, specieslist=specieslist, expiddescriptionlist=expiddescriptionlist, time_units=time_units, calendar=calendar, version=version, overwrite=overwrite)

if __name__ == '__main__':
    main()
