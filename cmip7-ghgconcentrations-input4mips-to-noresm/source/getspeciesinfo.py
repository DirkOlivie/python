def getspeciesinfo(species, i4mpdownload) :
#-----------------
    '''
    INPUT
	    species : 'CO2' | 'CH4' | 'N2O' | 'CFC11eq' | 'CFC12eq' | 'CFC12' | 'ADJ' | 
                  'CO2_LBC' | 'CH4_LBC' | ...
	    i4mpdownload : '', '-cmip7', ...

    RETURN 
	    structure containing
		    origspecies   : species name in input4MIPs NetCDF file 
		    finalspecies  : species name in final NetCDF file (as needed by CESM/NorESM)
		    finallongname : long_name  in final NetCDF file
		    finalunit     : units in final NetCDF file

     CALLED BY 
	    buildconcentration
	
    CALLS	

    MODIFICATIONS
	    (2025-09-12)
        (2026-08-27) : extension to full-chemistry 
    '''
#------------------------
# 
#   I. original species
#   default values
    fixedvalue  = None
    source      = 'standard'

#   cmip7
    if ( i4mpdownload == 'CR-CMIP-1-0-0' \
      or i4mpdownload == 'CR-h-1-0-0' \
      or i4mpdownload == 'CR-vl-1-0-0' ) :

#       NoreESM species               | input4MIPs species
#       global
        if (   species == 'CO2'     ) : orgsp = 'co2'
        elif ( species == 'CH4'     ) : orgsp = 'ch4'
        elif ( species == 'N2O'     ) : orgsp = 'n2o'
        elif ( species == 'CFC11'   ) : orgsp = 'cfc11'
        elif ( species == 'CFC11eq' ) : orgsp = 'cfc11eq'
        elif ( species == 'CFC12'   ) : orgsp = 'cfc12'
        elif ( species == 'ADJ'     ) : orgsp = '-'

#       zonal resolved
        elif ( species == 'CO2_LBC'     ) : orgsp = 'co2'     
        elif ( species == 'CH4_LBC'     ) : orgsp = 'ch4'     
        elif ( species == 'N2O_LBC'     ) : orgsp = 'n2o'     
        elif ( species == 'CFCL3_LBC'   ) : orgsp = 'cfc11'
        elif ( species == 'CFC11eq_LBC' ) : orgsp = 'cfc11eq'
        elif ( species == 'CF2CL2_LBC'  ) : orgsp = 'cfc12'

#       zonal resolved
        elif ( species == 'CCL4_LBC'     ) : orgsp = 'ccl4'  
        elif ( species == 'CF2CLBR_LBC'  ) : orgsp = 'halon1211' # HALON1211 (seen in CESM file)  
        elif ( species == 'CF3BR_LBC'    ) : orgsp = 'halon1301' # HALON1301 (seen in CESM file)
        elif ( species == 'CFC11_LBC'    ) : orgsp = 'cfc11'     # CFCL3_LBC
        elif ( species == 'CFC113_LBC'   ) : orgsp = 'cfc113'    
        elif ( species == 'CFC12_LBC'    ) : orgsp = 'cfc12'     # CF2CL2_LBC  
        elif ( species == 'CH3BR_LBC'    ) : orgsp = 'ch3br'  
        elif ( species == 'CH3CCL3_LBC'  ) : orgsp = 'ch3ccl3' 
        elif ( species == 'CH3CL_LBC'    ) : orgsp = 'ch3cl'  
        elif ( species == 'H2_LBC'       ) : orgsp = 'h2'      ; source='fixedvalue' ; fixedvalue= 5.0e-7 # not in input4MIPs :  5e-07 in CESM2/CMIP6 and CESM3/CMIP7 file (historical and SSP245)
        elif ( species == 'HCFC22_LBC'   ) : orgsp = 'hcfc22'  
        elif ( species == 'CFC114_LBC'   ) : orgsp = 'cfc114'  
        elif ( species == 'CFC115_LBC'   ) : orgsp = 'cfc115'  
        elif ( species == 'HCFC141B_LBC' ) : orgsp = 'hcfc141b'  
        elif ( species == 'HCFC142B_LBC' ) : orgsp = 'hcfc142b'  
        elif ( species == 'CH2BR2_LBC'   ) : orgsp = 'ch2br2'     ; source='fixedvalue' ; fixedvalue=1.2e-12   # not in input4MIPs : 1.2e-12 in CESM2/CMIP6 and CESM3/CMIP7 file
        elif ( species == 'CHBR3_LBC'    ) : orgsp = 'chbr3'      ; source='fixedvalue' ; fixedvalue=1.2e-12   # not in input4MIPs : 1.2e-12 in CESM2/CMIP6 and CESM3/CMIP7 file 
        elif ( species == 'H2402_LBC'    ) : orgsp = 'halon2402' # HALON2402
        elif ( species == 'OCS_LBC'      ) : orgsp = 'ocs'     ; source='cesm2-cmip6' # not in input4MIPs  
        elif ( species == 'SF6_LBC'      ) : orgsp = 'sf6' 
#
#       else
        else : 
            print('+++ getspeciesinfo +++')
            print('No species recognized = ', species)
            quit()
#   cmip6    
    elif ( i4mpdonwload == 'cmip6' ) :

#       global mean
        if (   species == 'CO2'     ) : orgsp='carbon_dioxide' 
        elif ( species == 'CH4'     ) : orgsp='methane'        
        elif ( species == 'N2O'     ) : orgsp='nitrous_oxide'  
        elif ( species == 'CFC11eq' ) : orgsp='cfc11eq'        
        elif ( species == 'CFC12'   ) : orgsp='cfc12'          
        elif ( species == 'ADJ'     ) : orgsp='-'              
#       zonal resolved
        elif ( species == 'CO2_LBC'     ) : orgsp='carbon_dioxide' 
        elif ( species == 'CH4_LBC'     ) : orgsp='methane'        
        elif ( species == 'N2O_LBC'     ) : orgsp='nitrous_oxide'  
        elif ( species == 'CFC11eq_LBC' ) : orgsp='cfc11eq'        
        elif ( species == 'CF2CL2_LBC'  ) : orgsp='cfc12'          
#       else
        else : 
            print('+++ getspeciesinfo +++')
            print('No species recognized = ', species)
            quit()
#
    else :
        print('+++ getspeciesinfo +++')
        print('No i4mpdownload recognized = ', i4mpdownload)
        quit()


#   II. final species informations
    
#   global mean 
    if   ( species == 'CO2'     ) : finsp=species   ; finlong=species                     ; finunits='1e-6 mol mol-1'  
    elif ( species == 'CH4'     ) : finsp=species   ; finlong=species                     ; finunits='1e-9 mol mol-1'  
    elif ( species == 'N2O'     ) : finsp=species   ; finlong=species                     ; finunits='1e-9 mol mol-1'  
    elif ( species == 'CFC11'   ) : finsp='f11'     ; finlong='CFC-11'                    ; finunits='1e-12 mol mol-1' 
    elif ( species == 'CFC11eq' ) : finsp='f11'     ; finlong='CFC-11 (adjusted)'         ; finunits='1e-12 mol mol-1' 
    elif ( species == 'CFC12'   ) : finsp='f12'     ; finlong='CFC-12'                    ; finunits='1e-12 mol mol-1' 
    elif ( species == 'ADJ'     ) : finsp='adj'     ; finlong='adj factor for f11'        ; finunits='unitless'        
#   zonally resolved
    elif ( species == 'CO2_LBC'     ) : finsp=species   ; finlong='CO2 (carbon dioxide) lower boundary condition'                                        ; finunits='mol mol-1'  
    elif ( species == 'CH4_LBC'     ) : finsp=species   ; finlong='CH4 (methane) lower boundary condition'                                               ; finunits='mol mol-1'  
    elif ( species == 'N2O_LBC'     ) : finsp=species   ; finlong='N2O (nitrous oxide) lower boundary condition'                                         ; finunits='mol mol-1'  
    elif ( species == 'CFCL3_LBC'   ) : finsp=species   ; finlong='CFCl3 (CFC-11) lower boundary condition'                                              ; finunits='mol mol-1'
    elif ( species == 'CFC11eq_LBC' ) : finsp=species   ; finlong='CFC11eq (table 5, option 2, Meinshausen et al., GMD, 2017) lower boundary condition'  ; finunits='mol mol-1' 
    elif ( species == 'CF2CL2_LBC'  ) : finsp=species   ; finlong='CF2Cl2 (CFC-12) lower boundary condition'                                             ; finunits='mol mol-1' 
#   zonal resolved
    elif ( species == 'CFC113_LBC'   ) : finsp=species   ; finlong='CCl2FCClF2 (CFC-113) lower boundary condition'        ; finunits='mol mol-1'
    elif ( species == 'CFC114_LBC'   ) : finsp=species   ; finlong='CClF2CClF2 (CFC-114) lower boundary condition'        ; finunits='mol mol-1'
    elif ( species == 'CFC115_LBC'   ) : finsp=species   ; finlong='CClF2CF3 (CFC-115) lower boundary condition'          ; finunits='mol mol-1'
    elif ( species == 'CCL4_LBC'     ) : finsp=species   ; finlong='CCl4 (carbon tetrachloride) lower boundary condition' ; finunits='mol mol-1'
    elif ( species == 'CH3CCL3_LBC'  ) : finsp=species   ; finlong='CH3CCl3 (methyl chloroform) lower boundary condition' ; finunits='mol mol-1'
    elif ( species == 'HCFC22_LBC'   ) : finsp=species   ; finlong='CHClF2 (HCFC-22) lower boundary condition'            ; finunits='mol mol-1'
    elif ( species == 'HCFC141B_LBC' ) : finsp=species   ; finlong='CH3CCl2F (HCFC-141B) lower boundary condition'        ; finunits='mol mol-1'
    elif ( species == 'HCFC142B_LBC' ) : finsp=species   ; finlong='CH3CClF2 (HCFC-142B) lower boundary condition'        ; finunits='mol mol-1'
    elif ( species == 'CH3CL_LBC'    ) : finsp=species   ; finlong='CH3Cl (methyl chloride) lower boundary condition'     ; finunits='mol mol-1'
    elif ( species == 'CH3BR_LBC'    ) : finsp=species   ; finlong='CH3Br (methyl bromide) lower boundary condition'      ; finunits='mol mol-1'
    elif ( species == 'CHBR3_LBC'    ) : finsp=species   ; finlong='CHBr3 (bromoform) lower boundary condition'           ; finunits='mol mol-1'
    elif ( species == 'CH2BR2_LBC'   ) : finsp=species   ; finlong='CH2Br2 (dibromomethane) lower boundary condition'     ; finunits='mol mol-1'
    elif ( species == 'CF2CLBR_LBC'  ) : finsp=species   ; finlong='CF2ClBr (halon-1211) lower boundary condition'        ; finunits='mol mol-1'
    elif ( species == 'CF3BR_LBC'    ) : finsp=species   ; finlong='CF3Br (halon-1301)lower boundary condition'           ; finunits='mol mol-1'
    elif ( species == 'H1202_LBC'    ) : finsp=species   ; finlong='CF2Br2 (halon-1202) lower boundary condition'         ; finunits='mol mol-1'
    elif ( species == 'H2402_LBC'    ) : finsp=species   ; finlong='CF2BrCF2Br (halon-2402) lower boundary condition'     ; finunits='mol mol-1'
    elif ( species == 'H2_LBC'       ) : finsp=species   ; finlong='H2 (molecular hydrogen) lower boundary condition'     ; finunits='mol mol-1'
    elif ( species == 'TOT_CLOY'     ) : finsp=species   ; finlong='total organic chlorine'                               ; finunits='mol mol-1'
    elif ( species == 'TOT_BROY'     ) : finsp=species   ; finlong='total organic Bromine'                                ; finunits='mol mol-1'
    elif ( species == 'TOT_FOY'      ) : finsp=species   ; finlong='total organic fluorine'                               ; finunits='mol mol-1'
    elif ( species == 'SF6_LBC'      ) : finsp=species   ; finlong='SF6 (sulfur hexaflouride) lower boundary condition'   ; finunits='mol mol-1'
    elif ( species == 'OCS_LBC'      ) : finsp=species   ; finlong='OCS (carbonyl sulfide) lower boundary condition'      ; finunits='mol mol-1'
    else :
        print('+++ getspeciesinfo +++')
        print('No species recognized = ', species)
        quit()
#
#   III. create data structure
    data = { 'origspecies'   : orgsp, \
             'finalspecies'  : finsp, \
             'finallongname' : finlong, \
             'finalunits'    : finunits, \
             'fixedvalue'    : fixedvalue, \
             'source'        : source } 
#
    return data
