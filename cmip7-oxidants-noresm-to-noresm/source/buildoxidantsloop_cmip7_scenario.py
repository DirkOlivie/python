import buildoxidantsloop2


def main():
#---------------------------------
    '''
    CALLS
        buildoxidantsloop2

    REMARK :

    '''

#   III. scenario
#---------------------------
    version='version20261021'

#   1. oxidants
    time_units='days since 1750-01-01'
    calendar='noleap'

    bctype='oxidants' ; specieslist=['O3','OH','NO3','HO2','HALONS']

#   overwrite=False
    overwrite=True
        
#   scenariolist=['scen-h']
    scenariolist=['scen-vl']

    for scenario in scenariolist :

        expiddescriptionlist = [ \
                             { 'year' : 2021, 'expid' : 'NF1850norbc_2022'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2022, 'expid' : 'NF1850norbc_2022'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2025, 'expid' : 'NF1850norbc_2025'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2030, 'expid' : 'NF1850norbc_2030'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2040, 'expid' : 'NF1850norbc_2040'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2050, 'expid' : 'NF1850norbc_2050'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2060, 'expid' : 'NF1850norbc_2060'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2070, 'expid' : 'NF1850norbc_2070'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2080, 'expid' : 'NF1850norbc_2080'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2090, 'expid' : 'NF1850norbc_2090'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2100, 'expid' : 'NF1850norbc_2100'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 2101, 'expid' : 'NF1850norbc_2100'+scenario+'_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'}
                           ]
#
        buildoxidantsloop2.buildoxidantsloop2(bctype=bctype, specieslist=specieslist, expiddescriptionlist=expiddescriptionlist, scenario=scenario, time_units=time_units, calendar=calendar, version=version, overwrite=overwrite)


if __name__ == '__main__':
    main()
