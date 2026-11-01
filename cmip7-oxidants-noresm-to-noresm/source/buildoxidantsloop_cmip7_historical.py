import buildoxidantsloop2


def main():
#---------------------------------
    '''
    CALLS
        buildoxidantsloop2

    REMARK :

    '''

#   II. historical
#---------------------------
#   version='version20260903'
#   version='version20260912'
    version='version20261021'

#   1. oxidants
    time_units='days since 1750-01-01'
    calendar='noleap'

    bctype='oxidants' ; specieslist=['O3','OH','NO3','HO2','HALONS']
    expiddescriptionlist = [ { 'year' : 1849, 'expid' : 'NF1850norbc_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 1850, 'expid' : 'NF1850norbc_tropstratchem_f19_f19_t02_20260829'          , 'period' : '0021-0030'} , \
                             { 'year' : 1860, 'expid' : 'NF1850norbc_1860climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1870, 'expid' : 'NF1850norbc_1870climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1880, 'expid' : 'NF1850norbc_1880climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1890, 'expid' : 'NF1850norbc_1890climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1900, 'expid' : 'NF1850norbc_1900climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1910, 'expid' : 'NF1850norbc_1910climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1920, 'expid' : 'NF1850norbc_1920climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1930, 'expid' : 'NF1850norbc_1930climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1940, 'expid' : 'NF1850norbc_1940climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1950, 'expid' : 'NF1850norbc_1950climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1960, 'expid' : 'NF1850norbc_1960climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1970, 'expid' : 'NF1850norbc_1970climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1980, 'expid' : 'NF1850norbc_1980climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 1990, 'expid' : 'NF1850norbc_1990climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 2000, 'expid' : 'NF1850norbc_2000climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 2010, 'expid' : 'NF1850norbc_2010climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 2020, 'expid' : 'NF1850norbc_2020climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 2023, 'expid' : 'NF1850norbc_2023climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 2025, 'expid' : 'NF1850norbc_2023climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'} , \
                             { 'year' : 2026, 'expid' : 'NF1850norbc_2023climo_tropstratchem_f19_f19_t02_20260829', 'period' : '0021-0030'}   \
                           ]
#
#   overwrite=False
    overwrite=True
#
    buildoxidantsloop2.buildoxidantsloop2(bctype=bctype, specieslist=specieslist, expiddescriptionlist=expiddescriptionlist, time_units=time_units, calendar=calendar, version=version, overwrite=overwrite)


if __name__ == '__main__':
    main()
