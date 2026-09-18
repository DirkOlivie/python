import loopanalysemap2
import cfiglayout
#
def main():
#----------    
#
    print('+++ loopanalysemap +++')
    print('--- loopanalysemap ---')
#
    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
    figlayoutlist=[figlayout0,figlayout1]
#
    code='n20221216_spaer'
#
#   STANDARD ERF contribution plots (Stephanies manuscript)
#----------------------------------
    wlist=[1.,-1.]
    seasonlist=['YEA']
    varlist=['FSLNT','direct_ERF_noresm2','cloud_ERF_noresm2','surfalb_ERF_noresm2']
#
#   year0list=[1 ,1 ,1 ]
#   year1list=[30,30,30]
#   expidlist=['piClim-SpAer2014'        ,'NF1850norbc_aer2014_f19_20190727','NF1850frc2norbc_aer2014_f09_20200108']
#   refidlist=['NF1850norbc_f19_20190727','NF1850norbc_f19_20190727'        ,'NF1850frc2norbc_f09_20200108'        ]
#
#    year0list=[1 ,1 ]
#    year1list=[30,30]
#    expidlist=['NF1850norbc_spAer_aer2014_f19_20210523','NF1850norbc_aer2014_f19_20191025']
#    refidlist=['NF1850norbc_f19_20191025'              ,'NF1850norbc_f19_20191025'        ]
#
#    year0list=[1 ]
#   year1list=[30]
#   expidlist=['NF1850norbc_aer2014_f19_20191025']
#   refidlist=['NF1850norbc_f19_20191025'        ]
#
#    year0list=[1 ]
#    year1list=[90]
#    expidlist=['NF1850norbc_spAer_aer2014_f19_20210523']
#    refidlist=['NF1850norbc_f19_20191025'              ]

    year0list=[1 ]
    year1list=[30]
    expidlist=['NF1850norbc_spAer_aer2014_f19_20230127']
    refidlist=['NF1850norbc_f19_20191025'              ]



    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
#   SPAERO ERF contribution plots (Alfs plots)
#--------------------------------
    wlist=[1.,0.]
    year0list=[3 ]
    year1list=[90]
    seasonlist=['YEA']
#
    varlist=['FSNT_SP2_minus_FSNT_SP','FSNT_SP3_minus_FSNT_SP2','FSNT_SP3_minus_FSNT_SP', \
             'FSNS_SP2_minus_FSNS_SP','FSNS_SP3_minus_FSNS_SP2','FSNS_SP3_minus_FSNS_SP']
#
#   expidlist=['piClim-SpAer2014']
    expidlist=['NF1850norbc_spAer_aer2014_f19_20210523']
    refidlist=expidlist
#
    code='n20221216_spaer'
#
#    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#    
if __name__ == '__main__':
    main()
