def getspeciesinfo(species, activity) :
#-----------------
    '''
    MODIFICATIONS
	    (2021-02-23) : perturbations passing via commonblock
        (2021-05-15) : 
		    1). adding gas-phase species
		    2). allowing for mulitple contributing species
	    (2021-09-02) : replaced anthrosurf by anthrosurfgas
	    (2025-04-15) : added CH4
        (2025-02-06) : added BC, OC, SO2
        (2026-02-06) : added H2
        (2026-04-15) : Higher-Alkanes (CMIP6) -> HigherAlkanes (CMIP7)
                       Higher-Alkenes (CMIP6) -> HigherAlkenes (CMIP7)

    CALLED BY
	    buildemission
    '''
#--------------------------
#
#  print, '+++ getspeciesinfo +++'
#  print, 'species = ', species
#
# so4frac=getvalue_commonblock(descriptor='so4frac')
    so4frac='0.025'
#
#   standard species
    if   ( species == 'BC_N'  ) : Mw=12. ; origspecieslist=['BC']  ; origweightlist = [ 0.9 ]
    elif ( species == 'BC_AX' ) : Mw=12. ; origspecieslist=['BC']  ; origweightlist = [ 0.1 ]
    elif ( species == 'BC_NI' ) : Mw=12. ; origspecieslist=['BC']  ; origweightlist = [ 1.0 ]
    elif ( species == 'BC'    ) : Mw=12. ; origspecieslist=['BC']  ; origweightlist = [ 1.0 ] # added on 2026-02-06
    elif ( species == 'OM_NI' ) : Mw=12. ; origspecieslist=['OC']  ; origweightlist = [ 1.0 ]
    elif ( species == 'OC'    ) : Mw=12. ; origspecieslist=['OC']  ; origweightlist = [ 1.0 ]
    elif ( species == 'S'     ) : Mw=64. ; origspecieslist=['SO2'] ; origweightlist = [ 1.0 ]
    elif ( species == 'SO2'   ) : 
        Mw=64. ; origspecieslist=['SO2']
        if   ( so4frac == '0.000' ) : origweightlist = [ 1.0   ] 
        elif ( so4frac == '0.025' ) : origweightlist = [ 0.975 ] 
        elif ( so4frac == '0.075' ) : origweightlist = [ 0.925 ] 
        else :
            print('+++ getspeciesinfo +++') 
            print('No so4frac recognized : ', so4frac)
            quit()                
    elif ( species == 'SO4_PR') : 
        Mw=64. ; origspecieslist=['SO2'] #  Mw=64 because final emissions are in molecules/cm2/s (# SO2 molecules = # SO4 molecules)
        if   ( so4frac == '0.000' ) : origweightlist = [ 0.0   ]
        elif ( so4frac == '0.025' ) : origweightlist = [ 0.025 ]
        elif ( so4frac == '0.075' ) : origweightlist = [ 0.075 ]
        else :
            print('+++ getspeciesinfo +++')
            print('No so4frac recognized : ', so4frac)     
            quit()
    elif ( species == 'CO'    ) : Mw=28. ; origspecieslist=[species] ; origweightlist=[1.]
    elif ( species == 'NH3'   ) : Mw=17. ; origspecieslist=[species] ; origweightlist=[1.]
    elif ( species == 'CH4'   ) : Mw=16. ; origspecieslist=[species] ; origweightlist=[1.]
#
    elif ( species == 'H2'    ) : Mw=2. ; origspecieslist=[species] ; origweightlist=[1.]

#   aircraft
    elif ( activity == 'air' ) :
  
        if ( species == 'NO2') : Mw=46. ; origspecieslist=['NOx'] ; origweightlist=[1.] # aircraft input4MIPs files contain kg[NO2]
        else :
            print('+++ getspeciesinfo +++')
            print('No species recognized : ', species)
            quit()
#   biomass burning
    elif ( activity == 'bb' \
	    or activity == 'bbsurf' ) :
     
        if   ( species == 'NO'      ) : Mw=30. ; origspecieslist=['NOx']            ; origweightlist=[1.] # bb inpurt4MIPs files contain kg[NO] 
        elif ( species == 'BENZENE' ) : Mw=78. ; origspecieslist=['C6H6']           ; origweightlist=[1.]   
        elif ( species == 'BIGALK'  ) : Mw=72. ; origspecieslist=['HigherAlkanes']  ; origweightlist=[1.] # Higher-Alkanes in CMIP6
        elif ( species == 'BIGENE'  ) : Mw=56. ; origspecieslist=['HigherAlkenes']  ; origweightlist=[1.] # Higher-Alkenes in CMIP6
        elif ( species == 'C2H2'    ) : Mw=26. ; origspecieslist=['C2H2']           ; origweightlist=[1.]
        elif ( species == 'C2H4'    ) : Mw=28. ; origspecieslist=['C2H4']           ; origweightlist=[1.]
        elif ( species == 'C2H5OH'  ) : Mw=46. ; origspecieslist=['C2H5OH']         ; origweightlist=[1.]
        elif ( species == 'C2H6'    ) : Mw=30. ; origspecieslist=['C2H6']           ; origweightlist=[1.]
        elif ( species == 'C3H6'    ) : Mw=42. ; origspecieslist=['C3H6']           ; origweightlist=[1.]
        elif ( species == 'C3H8'    ) : Mw=44. ; origspecieslist=['C3H8']           ; origweightlist=[1.]
        elif ( species == 'CH2O'    ) : Mw=30. ; origspecieslist=['CH2O']           ; origweightlist=[1.]
        elif ( species == 'CH3CHO'  ) : Mw=44. ; origspecieslist=['C2H4O']          ; origweightlist=[1.]
        elif ( species == 'CH3CN'   ) : Mw=41. ; origspecieslist=['CO']             ; origweightlist=[0.002]
        elif ( species == 'CH3COCH3') : Mw=58. ; origspecieslist=['C3H6O']          ; origweightlist=[1.]  
        elif ( species == 'CH3COCHO') : Mw=72. ; origspecieslist=['CH3COCHO']       ; origweightlist=[1.]   
        elif ( species == 'CH3COOH' ) : Mw=60. ; origspecieslist=['CH3COOH']        ; origweightlist=[1.]  
        elif ( species == 'CH3OH'   ) : Mw=32. ; origspecieslist=['CH3OH']          ; origweightlist=[1.]
        elif ( species == 'DMS'     ) : Mw=62. ; origspecieslist=['C2H6S']          ; origweightlist=[1.]  
        elif ( species == 'GLYALD'  ) : Mw=60. ; origspecieslist=['HOCH2CHO']       ; origweightlist=[1.]
        elif ( species == 'HCN'     ) : Mw=27. ; origspecieslist=['HCN']            ; origweightlist=[1.]
        elif ( species == 'HCOOH'   ) : Mw=46. ; origspecieslist=['HCOOH']          ; origweightlist=[1.]
        elif ( species == 'ISOP'    ) : Mw=68. ; origspecieslist=['C5H8']           ; origweightlist=[1.]
        elif ( species == 'MEK'     ) : Mw=72. ; origspecieslist=['MEK']            ; origweightlist=[1.]
        elif ( species == 'MTERP'   ) : Mw=136.; origspecieslist=['C10H16']         ; origweightlist=[1.]
        elif ( species == 'TOLUENE' ) : Mw=92. ; origspecieslist=['C7H8']           ; origweightlist=[1.]
        elif ( species == 'XYLENES' ) : Mw=106.; origspecieslist=['C8H10']          ; origweightlist=[1.]
        else :
            print('+++ getspeciesinfo +++')
            print('No species recognized : ', species)
            quit()

    elif ( activity == 'anthrosurfgas' ) : # until 2021-09-02 'anthrosurf'

        if   ( species == 'NO'      ) : Mw=30. ; origspecieslist=['NOx']              ; origweightlist=[30./46.] # bb inpurt4MIPs files contain kg[NO2]
        elif ( species == 'BENZENE' ) : Mw=78. ; origspecieslist=['VOC13-benzene']    ; origweightlist=[1.]   
        elif ( species == 'BIGALK'  ) : Mw=72. ; origspecieslist=['VOC04-butanes','VOC05-pentanes','VOC06-hexanes-pl','VOC18-esters','VOC19-ethers'] ; origweightlist=[1.,1.,1.,1.,1.]                 
        elif ( species == 'BIGENE'  ) : Mw=56. ; origspecieslist=['VOC12-other-alke'] ; origweightlist=[1.]   
        elif ( species == 'C2H2'    ) : Mw=26. ; origspecieslist=['VOC09-ethyne']     ; origweightlist=[1.]   
        elif ( species == 'C2H4'    ) : Mw=28. ; origspecieslist=['VOC07-ethene']     ; origweightlist=[1.]   
        elif ( species == 'C2H5OH'  ) : Mw=46. ; origspecieslist=['VOC01-alcohols']   ; origweightlist=[0.85] 
        elif ( species == 'C2H6'    ) : Mw=30. ; origspecieslist=['VOC02-ethane']     ; origweightlist=[1.]                                                        
        elif ( species == 'C3H6'    ) : Mw=42. ; origspecieslist=['VOC08-propene']    ; origweightlist=[1.]   
        elif ( species == 'C3H8'    ) : Mw=44. ; origspecieslist=['VOC03-propane']    ; origweightlist=[1.]   
        elif ( species == 'CH2O'    ) : Mw=30. ; origspecieslist=['VOC21-methanal']   ; origweightlist=[1.]   
        elif ( species == 'CH3CHO'  ) : Mw=44. ; origspecieslist=['VOC22-other-alka'] ; origweightlist=[1.]   
        elif ( species == 'CH3CN'   ) : Mw=41. ; origspecieslist=['CO']               ; origweightlist=[0.002]                                                                        
        elif ( species == 'CH3COCH3') : Mw=58. ; origspecieslist=['VOC23-ketones']    ; origweightlist=[0.20]                                                           
        elif ( species == 'CH3COCHO') : print('No infformation for species : ', species)
        elif ( species == 'CH3COOH' ) : Mw=60. ; origspecieslist=['VOC24-acids']      ; origweightlist=[0.50] 
        elif ( species == 'CH3OH'   ) : Mw=32. ; origspecieslist=['VOC01-alcohols']   ; origweightlist=[0.15] 
        elif ( species == 'DMS'     ) : print('No infformation for species : ', species)
        elif ( species == 'GLYALD'  ) : print('No infformation for species : ', species)
        elif ( species == 'HCN'     ) : Mw=27. ; origspecieslist=['CO']               ; origweightlist=[0.006]
        elif ( species == 'HCOOH'   ) : Mw=46. ; origspecieslist=['VOC24-acids']      ; origweightlist=[0.50]                                                       
        elif ( species == 'ISOP'    ) : print('No infformation for species : ', species)
        elif ( species == 'MEK'     ) : Mw=72. ; origspecieslist=['VOC23-ketones']    ; origweightlist=[0.80] 
        elif ( species == 'MTERP'   ) : stop: print('No infformation for species : ', species)
        elif ( species == 'TOLUENE' ) : Mw=92. ; origspecieslist=['VOC14-toluene']    ; origweightlist=[1.]   
        elif ( species == 'XYLENES' ) : Mw=106.;origspecieslist=['VOC15-xylene','VOC16-trimethylb','VOC17-other-arom'] ; origweightlist=[1.,1.,1.]
        else :
            print('+++ getspeciesinfo +++')
            print('No species recognized : ', species)
            quit()
    else :
        print('+++ getspeciesinfo +++')
        print('No activity or species recognized : ', activity, species)
        quit()
#
    if ( len(origspecieslist) != len(origweightlist) ) :
        print('+++ getspeciesinfo +++')
        print('Length of arrays are differen : ')
        print('origspecieslist : ', len(origspecieslist))
        print('origweightlist  : ', len(origweightlist))
        quit() # this quit() was absent before 2026-08-20

#   data structyre
    data = { 'origspecieslist' : origspecieslist, \
             'origweightlist'  : origweightlist, \
	         'Mw'              : Mw}
#
#  print, 'data = ', data
#
#  print, '--- getspeciesinfo ---'
#
    return data
