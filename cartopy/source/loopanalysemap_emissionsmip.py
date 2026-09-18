import loopanalysemap2
import cfiglayout
#
def main():
#----------    
#
    print('+++ loopanalysemap +++')
    print('--- loopanalysemap ---')

    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
    figlayoutlist=[figlayout0,figlayout1]

    wlist=[1.,-1.]
    year0list=[2001,2001,2001,2001,2001]
    year1list=[2005,2005,2005,2005,2005]
    seasonlist=['YEA']

    varlist=['SWCF']

    expidlist=['NFHISTnorpddmsbcsdyn_so2_at_height_f09_mg17_20210226', \
               'NFHISTnorpddmsbcsdyn_f2_ship_30red_f09_mg17_20220824', \
               'NFHISTnorpddmsbcsdyn_f2_ship_60red_f09_mg17_20220824', \
               'NFHISTnorpddmsbcsdyn_f2_ship_atlanticshift_f09_mg17_20220824', \
               'NFHISTnorpddmsbcsdyn_f2_ship_indianshift_f09_mg17_20220824']
    refidlist=['NFHISTnorpddmsbcsdyn_base_f09_mg17_20210226', \
               'NFHISTnorpddmsbcsdyn_f2_base_f09_mg17_20220824', \
               'NFHISTnorpddmsbcsdyn_f2_base_f09_mg17_20220824', \
               'NFHISTnorpddmsbcsdyn_f2_base_f09_mg17_20220824', \
               'NFHISTnorpddmsbcsdyn_f2_base_f09_mg17_20220824']

    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
if __name__ == '__main__':
    main()
