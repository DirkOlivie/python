import loopanalysedistribution2
#
def main():
#----------    
#
    print('+++ loopanalysedistribution +++')
    print('--- loopanalysedistribution ---')
#
#   NorESM2 
    wlist=[1.,0.]
    expidlist=['n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST.2025-10-29', \
               'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr001.20251023', \
               'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr001.20251023']
    refidlist=expidlist  # reference
    timedescriptionlist=['361-390-seperate-YEA-seperate', \
                         '46-75-seperate-YEA-seperate', \
                         '46-75-seperate-YEA-seperate']
    varlist=['U10', \
             'U10', \
             'U10']
    typevarlist=['', \
                 '', \
                 '']
    finalresolutionlist=['orig','orig','2x2']

    legendlist=['2x2','1x1','1x1 -> 2x2']
    distributiontype='histogram'
    code='n20250814_noresm2.5_picontrol'

    loopanalysedistribution2.loopanalysedistribution2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, timedescriptionlist=timedescriptionlist, finalresolutionlist=finalresolutionlist, legendlist=legendlist,distributiontype=distributiontype,code=code)  
#
if __name__ == '__main__':
    main()
