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
    expidlist=['NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08']
    refidlist=expidlist  # reference
    timedescriptionlist=['2006-2014-seperate-YEA-seperate', \
                         '2006-2014-seperate-YEA-seperate', \
                         '2006-2014-seperate-YEA-seperate', \
                         '2006-2014-seperate-YEA-seperate', \
                         '2006-2014-seperate-YEA-seperate', \
                         '2006-2014-seperate-YEA-seperate', \
                         '2006-2014-seperate-YEA-seperate', \
                         '2006-2014-seperate-YEA-seperate']
#    timedescriptionlist=['2006-2014-average-YEA-average', \
#                         '2006-2014-average-YEA-average', \
#                         '2006-2014-average-YEA-average']
    varlist=['CHBR3_extrapolate00m', \
             'CHBR3_surfacelayer', \
             'CHBR3_secondsurfacelayer', \
             'CHBR3_thirdsurfacelayer', \
             'CHBR3_extrapolate00m', \
             'CHBR3_surfacelayer', \
             'CHBR3_secondsurfacelayer', \
             'CHBR3_thirdsurfacelayer']
    typevarlist=['SEA', \
                 'SEA', \
                 'SEA', \
                 'SEA', \
                 'LAND', \
                 'LAND', \
                 'LAND', \
                 'LAND']
    legendlist=['0m (sea)','first layer (sea)','second layer (sea)','thirdlayer (sea)','0m (land)','first layer (land)','second layer (land)','thirdlayer (land)']
    distributiontype='histogram'
    code='bromoform'

#    loopanalysedistribution2.loopanalysedistribution2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, timedescriptionlist=timedescriptionlist, legendlist=legendlist,distributiontype=distributiontype,code=code)  
#
# PBLH
    wlist=[1.,0.]
#   NorESM2 - no chemistry
    expidlist=['NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08']
    refidlist=expidlist  # reference
    timedescriptionlist=['2006-2014-seperate-YEA-seperate', \
                         '2006-2014-seperate-YEA-seperate']
    varlist=['PBLH', \
             'PBLH']
    typevarlist=['SEA','LAND']
    legendlist=['(sea)','(land)']
    distributiontype='histogram'
    code='bromoform'

#   loopanalysedistribution2.loopanalysedistribution2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, timedescriptionlist=timedescriptionlist, legendlist=legendlist,distributiontype=distributiontype,code=code)
#
# ratio between (middle of) surface layer and extrapolation to the surface
    wlist=[1.,0.]
#   NorESM2 - no chemistry
    expidlist=['NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08']
    refidlist=expidlist  # reference
    timedescriptionlist=['2006-2014-seperate-YEA-seperate', \
                         '2006-2014-seperate-YEA-seperate']
    varlist=['CHBR3_ratioextrapolate00mTOsurfacelayer', \
             'CHBR3_ratioextrapolate00mTOsurfacelayer']
    typevarlist=['SEA','LAND']
    legendlist=['(sea)','(land)']
    distributiontype='histogram'
    code='bromoform'

    loopanalysedistribution2.loopanalysedistribution2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, timedescriptionlist=timedescriptionlist, legendlist=legendlist,distributiontype=distributiontype,code=code)
#
if __name__ == '__main__':
    main()
