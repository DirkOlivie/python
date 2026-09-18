import loopanalysemap2
import sys
#import cfiglayout
#
def main():
#
    print('+++ loopanalysemap +++')
    print('--- loopanalysemap ---')

#   the name of the prgoram is also an argument
    print(len(sys.argv))
    print(sys.argv)

    if ( len(sys.argv) != 2 ) :
        print('Incorrect number of arguments')
        exit(0)
    else :
        description = sys.argv[1]
        filename='../description-map/description.'+description+'.txt'

    print(filename)
#
#   open the file and read the lines
    f=open(filename)

    for line in f:

        if 'BEGIN' in line :
#           initialize
            expidlist=[]
            refidlist=[]
            figlayoutlist=['imposed'] # initialized 
            nrefid=0            # initialise 
            wlist=[1.,0.]       # initialise
            print('2')
            info=[]
            print(info)

        elif 'CODE=' in line :
            print('CODE')
            line=line.split('=')
            code=line[1].strip()
            print(code)

        elif 'FIGLAYOUTLIST=' in line :
            print('FIGLAYOUTLIST')
            line=line.strip()              # skip \n
            line=line.split('=')
            figlayoutlist=line[1].split(',')
        
        elif 'YEAR0=' in line :
            print('YEAR0')
            line=line.split('=')
            year0=int(line[1].strip())
            print(code)

        elif 'YEAR1=' in line :
            print('YEAR1')
            line=line.split('=')
            year1=int(line[1].strip())
            print(code)
          
        elif 'SEASONLIST=' in line :
            print('SEASONLIST')
            line=line.strip()              # skip \n
            line=line.split('=')
            seasonlist=line[1].split(',')

        elif 'WLIST=' in line :
            print('WLIST')
            line=line.strip()              # skip \n
            line=line.split('=')
            line=line[1].split(',')
            wlist[0]=float(line[0])
            wlist[1]=float(line[1]) 

        elif 'EXP=' in line :

            line=line.split('=') # EXP=.... -> EXP <expid>
            expid=line[1].strip()  # <expid>
            expidlist.append(expid)

        elif 'REF=' in line :

            line=line.split('=') # EXP=.... -> EXP <expid>
            refid=line[1].strip()  # <expid>
            refidlist.append(refid)

        elif 'VARLIST=' in line :
            print('varlist')
            line=line.strip()              # skip \n
            line=line.split('=')
            varlist=line[1].split(',')

        elif 'END' in line :
            print('3')
            if ( len(refidlist) == 0 ) : refidlist=expidlist
            loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)

    f.close()

if __name__ == '__main__':
    main()

#    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
#    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')

#   CESM2 - full chemistry
#   expidlist=['FC2010climo_f19_20210204_test1']
#    expidlist=['FC2010climo_prep_f19_20210204_test7']
#    varlist=['cb_O3']#['O3_SRF']#['NO2_SRF','NO_SRF']#['O3_SRF'] # ['cb_O3','O3_SRF','NO2_SRF','CO_SRF','SO2_SRF']#,'NO2','T']
#    varlist=['cb_O3','O3_SRF','NO2_SRF','CO_SRF','SO2_SRF']
#    year0=6 #16
#    year1=10
#   seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']#'JJA','DJF','YEA']
#    seasonlist=['DJF','MAM','JJA','SON']
#    loopanalysemap2.loopanalysemap2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysemap2.loopanalysemap2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout1)
#
#   NorESM2 - test
#    expidlist=['NF1850norbc_tropstratchem_f19_20210331_test14']
#    varlist=['O3_SRF']#,'NO2','T']
#    year0=20 # 16
#    year1=20
#    seasonlist=['YEA']#'JJA','DJF','YEA']
#    loopanalysemap2.loopanalysemap2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysemap2.loopanalysemap2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout1)
#
#   NorESM2 - test
#    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test01', \
#               'NF1850norbc_tropstratchem_f19_20210517_test02', \
#               'NF1850norbc_tropstratchem_f19_20210517_test03', \
#               'NF1850norbc_tropstratchem_f19_20210517_test04', \
#               'NF1850norbc_tropstratchem_f19_20210517_test05']
#    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test06']
#    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test01', \
#               'NF1850norbc_tropstratchem_f19_20210517_test05', \
#               'NF1850norbc_tropstratchem_f19_20210517_test09']
#    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test10']
#    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test11']
#    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test12']
#    expidlist=['NF2010norpddmsbc_tropstratchem_f19_20210517_test09']
#    varlist=['cb_O3']#['O3_SRF']#['NO2_SRF','NO_SRF','O3_SRF']#['cb_O3','O3_SRF','NO2_SRF','CO_SRF','SO2_SRF']
#    varlist=['O3_SRF']
#    varlist = ['cb_O3','O3_SRF','NO2_SRF','CO_SRF','SO2_SRF']
#    year0=6 # 16
#    year1=10
#   seasonlist=['JUL','AUG','SEP','OCT']#''YEA']#'JJA','DJF','YEA']
#    seasonlist=['DJF','MAM','JJA','SON','YEA']
#    loopanalysemap2.loopanalysemap2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#   loopanalysemap2.loopanalysemap2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout1)

#if __name__ == '__main__':
#    main()
