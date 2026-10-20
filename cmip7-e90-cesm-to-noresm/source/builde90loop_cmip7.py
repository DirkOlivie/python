import builde90loop2


def main():
#---------------------------------
    '''
    CALLS
        builde90loop2

    REMARK :

    '''

    

#   I. piControl climatology
#---------------------------
#   version='version20260903'
    version='version20261002'

#   0.9x1.25
#-----------
    specieslist    = ['E90', \
                      'C2H4','C2H6','C3H6','C3H8','CO','NH3','NO']
    resolutionlist = ['0.9x1.25']
#   periodlist     = ['histclimo']
    periodlist     = ['scenario']
#
    overwrite=False
#   overwrite=True
#
    builde90loop2.builde90loop2(specieslist=specieslist, resolutionlist=resolutionlist, periodlist=periodlist, version=version, overwrite=overwrite)
#
#   1.9x2.5
#----------
    specieslist    = ['C2H4','C2H6','C3H6','C3H8','CO','NH3','NO']
    resolutionlist = ['1.9x2.5']
#   periodlist     = ['histclimo']
    periodlist     = ['scenario']
#
    overwrite=False
#   overwrite=True
#
    builde90loop2.builde90loop2(specieslist=specieslist, resolutionlist=resolutionlist, periodlist=periodlist, version=version, overwrite=overwrite)

if __name__ == '__main__':
    main()
