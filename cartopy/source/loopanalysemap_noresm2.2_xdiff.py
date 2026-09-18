import loopanalysemap2
import cfiglayout
#
def main():
#
    print('+++ loopanalysemap +++')
    print('--- loopanalysemap ---')

    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
    figlayoutlist=[figlayout0,figlayout1]

    wlist=[1.,-1.]
    year0=6 #16
    year1=20
    seasonlist=['YEA']

#   NorESM2.2
    varlist=['SFisoprene','SFmonoterp']
    varlist=['MEG_isoprene','FSNO','NPP','SOILWATER_10CM','TLAI','TSA']

    expidlist=['NF1850norbc_f19_f19_20211013']   # noresm2.2
    refidlist=['NF1850norbc_f19_f19_20210530']   # noresm2.0
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)

#
    expidlist=['NF1850norbc_f19_f19_20211013']      # noresm2.2
    refidlist=['NF1850norbc_f19_20211113_test17']   # noresm2.2 with OLD clubb 
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
    expidlist=['NF1850norbc_f19_20211113_test17']   # noresm2.2 with OLD clubb
    refidlist=['NF1850norbc_f19_f19_20210530']      # noresm2.0
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)

#   CESM2.2
    varlist=['FSNO','SOILWATER_10CM','TLAI','TSA']
#
    expidlist=['F2000climo_f09_ver2.2_20211005']    # cesm2.2
    refidlist=['F2000climo_f09_ver2.1.3_20211005']  # cesm2.1
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)  
#
    expidlist=['F2000climo_f09_ver2.2_20211005']         # cesm2.2
    refidlist=['F2000climo_f09_20211109_cesm2.2_test04'] # cesm2.2 with OLD clubb
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
    expidlist=['F2000climo_f09_20211109_cesm2.2_test04']  # cesm2.2 with OLD clubb
    refidlist=['F2000climo_f09_ver2.1.3_20211005']        # cesm2.1
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)  
#
if __name__ == '__main__':
    main()
