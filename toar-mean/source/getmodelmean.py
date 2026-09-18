import numpy as np


def getmodelmean() :
#-------------------
#
#   
#    MODIFICATIONS
#        (2025-05-08) added CESM2 fixed-ODS simulations
#        
#    RESULTS NOVEMBER 2024
#    64.77499999999999 -0.08821333333333332 0.11194333333333333 -0.13175833333333334 -0.019815833333333335
#    3.550806246474173 0.05637728374285358 0.07707647818166635 0.05307535662202899 0.04030497823022472
#    65.84333333333332 -0.10428333333333334 0.14281333333333332 -0.15071 -0.007876666666666669
#    2.7666626505994962 0.07174780569621779 0.09738935784890576 0.054351199312128035 0.04434180445383591
#    -0.04826 0.03212333333333334 -0.06803666666666668 -0.03591066666666667
#    0.03621292863053194 0.041967930878496054 0.02233279253076565 0.04495211631156968
#    
#
#   REFERENCE 
#   see n20241001_toar_multimodel_mean.txt
    clt=np.array([ 69.12, \
                   62.37, \
                   \
                   66.02, \
                   60.03, \
                   \
                   61.97, \
                   69.14])
#
#   see n20241001_toar_multimodel_meandiff.txt
    cltchange=np.array([ -0.08049, \
                         -0.03399, \
                          \
                         -0.07606, \
                         -0.03656, \
                          \
                         -0.09938, \
                         -0.2028])                     
#
#   see n20241001_toar_multimodel_fluxes_meandiff.txt
    swerf=np.array([ 0.09549, \
                     0.04984, \
                     \
                     0.1013, \
                     0.04977, \
                     \
                     0.09796, \
                     0.2773])                     
#
    lwerf=np.array([ -0.1715, \
                     -0.09103, \
                      \
                     -0.1386, \
                     -0.06452, \
                      \
                     -0.1024, \
                     -0.2225])                    
#
    swlwerf=np.array([ -0.07603, \
                       -0.04120, \
                        \
                       -0.03722, \
                       -0.01475, \
                        \
                       -0.004485, \
                        0.05479])
#
    print(clt.mean(), cltchange.mean(), swerf.mean(), lwerf.mean(), swlwerf.mean())
    print(clt.std() , cltchange.std() , swerf.std() , lwerf.std() , swlwerf.std() )
#
#   REFERENCE FOR SUBGROUP
#    subset=[1,2,5]   # november 2024 (first submission
    subset=[0,1,2,5] # may 2025      (resubmission)
    print(clt[subset].mean(), cltchange[subset].mean(), swerf[subset].mean(), lwerf[subset].mean(), swlwerf[subset].mean())
    print(clt[subset].std() , cltchange[subset].std() , swerf[subset].std() , lwerf[subset].std() , swlwerf[subset].std() )
#
#   FIXED-ODS 
#   see n20241001_toar_multimodelsensitivity_meandiff.txt (first submission)
#   cltchange=np.array([-0.007250, -0.04220, -0.09533])
#   see n20250508_toar_multimodelsensitivity_meandiff.txt (revision = adding CESM2)
    cltchange=np.array([-0.01978,-0.007250, -0.04220, -0.09533])

#   see n20241001_toar_multimodelsensitivity_meandiff.txt
#    swerf=np.array([0.03209,-0.01926,0.08354])
#    lwerf=np.array([-0.03671,-0.08022,-0.08718])
#    swlwerf=np.array([-0.004620,-0.09948,-0.003632])
    swerf=np.array([-0.009107,0.03209,-0.01926,0.08354])
    lwerf=np.array([-0.1279,-0.03671,-0.08022,-0.08718])
    swlwerf=np.array([-0.1370,-0.004620,-0.09948,-0.003632])
    print(cltchange.mean(), swerf.mean(), lwerf.mean(), swlwerf.mean())
    print(cltchange.std() , swerf.std() , lwerf.std() , swlwerf.std() )

if __name__ == '__main__':
    getmodelmean()
