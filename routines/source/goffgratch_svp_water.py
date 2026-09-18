import math

def goffgratch_svp_water(t) :
#----------------------------
    '''
    BASED ON     
        src/physics/cam/wv_sat_methods.F90 :

            real(r8), intent(in) :: t  ! Temperature in Kelvin
            real(r8) :: es             ! SVP in Pa

            ! uncertain below -70 C
            es = 10._r8**(-7.90298_r8*(tboil/t-1._r8)+ &
                5.02808_r8*log10(tboil/t)- &
                1.3816e-7_r8*(10._r8**(11.344_r8*(1._r8-t/tboil))-1._r8)+ &
                8.1328e-3_r8*(10._r8**(-3.49149_r8*(tboil/t-1._r8))-1._r8)+ &
                log10(1013.246_r8))*100._r8

        /src/physics/cam/wv_saturation.F90 :

            tboil = 373.16_r8

    INPUT
        t : temperature [K]

    '''
  
    tboil = 373.16 # [K]

    es = 10.**(-7.90298*(tboil/t-1.)+ \
       5.02808*math.log10(tboil/t)- \
       1.3816e-7*(10.**(11.344*(1.-t/tboil))-1.)+ \
       8.1328e-3*(10.**(-3.49149*(tboil/t-1.))-1.)+ \
       math.log10(1013.246))*100.

    return es
