def getattributeinfo(var):
#-------------------
#
#   https://github.com/PCMDI/cmip6-cmor-tables/blob/main/Tables/CMIP6_Emon.json


    cell_methods='area: time: mean'
    cell_measure='area: areacell'
    missing_value=1.e+20
    _Fillvalue=1.e+2
    coordinates=None
    cdim='2d'

#Amon
#----------------------------------------------------
#   cloud fraction    
    if  ( var == 'clt'   ) : standard_name = "cloud_area_fraction"               ; long_name = "Total Cloud Cover Percentage"      ; units = "%"     ; original_name = "CLDTOT"  ; original_units = "1" 

#   latent and sensible heatflux
    elif ( var == 'hfls' ) : standard_name = "surface_upward_latent_heat_flux"   ; long_name = "Surface Upward Latent Heat Flux"   ; units = "W m-2" ; original_name = "LHFLX"   ; original_units = "W/m2" 
    elif ( var == 'hfss' ) : standard_name = "surface_upward_sensible_heat_flux" ; long_name = "Surface Upward Sensible Heat Flux" ; units = "W m-2" ; original_name = "SHFLX"   ; original_units = "W/m2"

#   relative and specific humidity
    elif ( var == 'hurs' ) : standard_name = "relative_humidity"                 ; long_name = "Near-Surface Relative Humidity"    ; units = "%"     ; original_name = "RHREFHT"                            ; coordinates = "height" 
    elif ( var == 'huss' ) : standard_name = "specific_humidity"                 ; long_name = "Near-Surface Specific Humidity"    ; units = "1"     ; original_name = "QREFHT"  ; original_units = "kg/kg" ; coordinates = "height"

#   precipitation
    elif ( var == 'pr'     ) : standard_name = "precipitation_flux"                     ; long_name = "Precipitation"            ; units = "kg m-2 s-1" ; original_name = "PRECT"
    elif ( var == 'prc'    ) : standard_name = "convective_precipitation_flux"          ; long_name = "Convective Precipitation" ; units = "kg m-2 s-1" ; original_name = "PRECC" 
    elif ( var == 'prsn'   ) : standard_name = "snowfall_flux"                          ; long_name = "Snowfall Flux"            ; units = "kg m-2 s-1" ; original_name = "PRECSC+PRECSL"

    elif ( var == 'prw'    ) : standard_name = "atmosphere_mass_content_of_water_vapor" ; long_name = "Water Vapor Path"         ; units = "kg m-2"     ; original_name = "Q"  # must be integrated

#   surface pressure
    elif ( var == 'ps'     ) : standard_name = "surface_air_pressure"                   ; long_name = "Surface Air Pressure"     ; units = "Pa"         ; original_name = "PS" 
    elif ( var == 'psl'    ) : standard_name = "air_pressure_at_mean_sea_level"         ; long_name = "Sea Level Pressure"       ; units = "Pa"         ; original_name = "PSL" 

#   radiation fluxes
    elif ( var == 'rlds'   ) : standard_name = "surface_downwelling_longwave_flux_in_air"                     ; long_name = "Surface Downwelling Longwave Radiation"            ; units = "W m-2" ; original_name = "FLDS"                ; original_units = "W/m2"
    elif ( var == 'rlus'   ) : standard_name = "surface_upwelling_longwave_flux_in_air"                       ; long_name = "Surface Upwelling Longwave Radiation"              ; units = "W m-2" ; original_name = "FLDS+FLNS"           ; original_units = "W/m2"
    elif ( var == 'rlut'   ) : standard_name = "toa_outgoing_longwave_flux"                                   ; long_name = "TOA Outgoing Longwave Radiation"                   ; units = "W m-2" ; original_name = "FSNTOA-FSNT+FLNT"    ; original_units = "W/m2" 
    elif ( var == 'rlutcs' ) : standard_name = "toa_outgoing_longwave_flux_assuming_clear_sky"                ; long_name = "TOA Outgoing Clear-Sky Longwave Radiation"         ; units = "W m-2" ; original_name = "FSNTOAC-FSNTC+FLNTC" ; original_units = "W/m2" 
    elif ( var == 'rsds'   ) : standard_name = "surface_downwelling_shortwave_flux_in_air"                    ; long_name = "Surface Downwelling Shortwave Radiation"           ; units = "W m-2" ; original_name = "FSDS"                ; original_units = "W/m2" 
    elif ( var == 'rsdscs' ) : standard_name = "surface_downwelling_shortwave_flux_in_air_assuming_clear_sky" ; long_name = "Surface Downwelling Clear-Sky Shortwave Radiation" ; units = "W m-2" ; original_name = "FSDSC"               ; original_units = "W/m2" 
    elif ( var == 'rsdt' )   : standard_name = "toa_incoming_shortwave_flux"                                  ; long_name = "TOA Incident Shortwave Radiation"                  ; units = "W m-2" ; original_name = "FSNTOA+FSUTOA"       ; original_units = "W/m2" 
    elif ( var == 'rsus' )   : standard_name = "surface_upwelling_shortwave_flux_in_air"                      ; long_name = "Surface Upwelling Shortwave Radiation"             ; units = "W m-2" ; original_name = "FSDS-FSNS"           ; original_units = "W/m2" 
    elif ( var == 'rsuscs' ) : standard_name = "surface_upwelling_shortwave_flux_in_air_assuming_clear_sky"   ; long_name = "Surface Upwelling Clear-Sky Shortwave Radiation"   ; units = "W m-2" ; original_name = "FSDSC-FSNSC"         ; original_units = "W/m2" 
    elif ( var == 'rsut' )   : standard_name = "toa_outgoing_shortwave_flux"                                  ; long_name = "TOA Outgoing Shortwave Radiation"                  ; units = "W m-2" ; original_name = "FSUTOA"              ; original_units = "W/m2" 
    elif ( var == 'rsutcs' ) : standard_name = "toa_outgoing_shortwave_flux_assuming_clear_sky"               ; long_name = "TOA Outgoing Clear-Sky Shortwave Radiation"        ; units = "W m-2" ; original_name = "SOLIN-FSNTOAC"       ; original_units = "W/m2" 
    elif ( var == 'rtmt' )   : standard_name = "net_downward_radiative_flux_at_top_of_atmosphere_model"       ; long_name = "Net Downward Radiative Flux at Top of Model"       ; units = "W m-2" ; original_name = "FSNT-FLNT"           ; original_units = "W/m2" 

#   surface wind
    elif ( var == 'sfcWind' ) : standard_name = "wind_speed"                                                  ; long_name = "Near-Surface Wind Speed" ; comment = " " ; units = "m s-1" ; original_name = "U10" ; original_units = "m/s" ; coordinates = "height" 

#   surface temperature
    elif ( var == 'tas'    ) : standard_name = "air_temperature"     ; long_name = "Near-Surface Air Temperature" ; units = "K" ; original_name = "TREFHT" ; coordinates = "height"
    elif ( var == 'ts'     ) : standard_name = "surface_temperature" ; long_name = "Surface Temperature"          ; units = "K" ; original_name = "TS" 

# AERMon
#--------------------------------------------------------
    elif ( var == 'bs550aer' ) : standard_name = "atmosphere_absorption_optical_thickness_due_to_ambient_aerosol_particles"                                                         ; long_name = "Ambient Aerosol Absorption Optical Thickness at 550nm"       ; units = "1"          ; original_name = "ABS550AL" ; coordinates = "wavelength" 
    elif ( var == 'bldep'    ) : standard_name = "atmosphere_boundary_layer_thickness"                                                                                              ; long_name = "Boundary Layer Depth"                                        ; units = "m"          ; original_name = "PBLH" 

    elif ( var == 'cdnc'     ) : standard_name = "number_concentration_of_cloud_liquid_water_particles_in_air"                                                                      ; long_name = "Cloud Liquid Droplet Number Concentration"                   ; units = "m-3"        ; original_name = "AWNC/FREQL" ; cdim='3d'
    elif ( var == 'chepsoa'  ) : standard_name = "tendency_of_atmosphere_mass_content_of_secondary_particulate_organic_matter_dry_aerosol_particles_due_to_net_chemical_production" ; long_name = "Chemical Production of Dry Aerosol Secondary Organic Matter" ; units = "kg m-2 s-1" ; original_name = "GS_SOA_LV+GS_SOA_SV" ; original_units = "kg/m2/s"

    elif ( var == 'cod'      ) : standard_name = "atmosphere_optical_thickness_due_to_cloud"                                                                                        ; long_name = "Cloud Optical Depth"                                         ; units = "1"          ; original_name = "TAUTMODIS/CLTMODIS" ;

#   dry deposition
    elif ( var == 'drybc'   ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_elemental_carbon_dry_aerosol_particles_due_to_dry_deposition"           ; long_name = "Dry Deposition Rate of Black Carbon Aerosol Mass"        ; units = "kg m-2 s-1" ; original_name = "BC_ACDDF+BC_AC_OCWDDF+BC_ADDF+BC_AIDDF+BC_AI_OCWDDF+BC_AXDDF+BC_A_OCWDDF+BC_NDDF+BC_NIDDF+BC_NI_OCWDDF+BC_N_OCWDDF"      ; original_units = "kg/m2/s"
    elif ( var == 'drydust' ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_dust_dry_aerosol_particles_due_to_dry_deposition"                       ; long_name = "Dry Deposition Rate of Dust"                             ; units = "kg m-2 s-1" ; original_name = "DST_A2DDF+DST_A3DDF+DST_A2_OCWDDF+DST_A3_OCWDDF"                                                                         ; original_units = "kg/m2/s" 
    elif ( var == 'dryoa'   ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_particulate_organic_matter_dry_aerosol_particles_due_to_dry_deposition" ; long_name = "Dry Deposition Rate of Dry Aerosol Total Organic Matter" ; units = "kg m-2 s-1" ; original_name = "OM_ACDDF+OM_AIDDF+OM_NIDDF+OM_AC_OCWDDF+OM_AI_OCWDDF+OM_NI_OCWDDF+SOA_A1DDF+SOA_NADDF+SOA_A1_OCWDDF+SOA_NA_OCWDDF"       ; original_units = "kg/m2/s" 
    elif ( var == 'dryso2'  ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_sulfur_dioxide_due_to_dry_deposition"                                   ; long_name = "Dry Deposition Rate of SO2"                              ; units = "kg m-2 s-1" ; original_name = "DF_SO2"                                                                                                                  ; original_units = "kg/m2/s"
    elif ( var == 'dryso4'  ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_sulfate_dry_aerosol_particles_due_to_dry_deposition"                    ; long_name = "Dry Deposition Rate of SO4"                              ; units = "kg m-2 s-1" ; original_name = "SO4_A1DDF+SO4_A2DDF+SO4_ACDDF+SO4_NADDF+SO4_PRDDF+SO4_A1_OCWDDF+SO4_A2_OCWDDF+SO4_AC_OCWDDF+SO4_NA_OCWDDF+SO4_PR_OCWDDF" ; original_units = "kg/m2/s" 
    elif ( var == 'dryss'   ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_sea_salt_dry_aerosol_particles_due_to_dry_deposition"                   ; long_name = "Dry Deposition Rate of Sea-Salt Aerosol"                 ; units = "kg m-2 s-1" ; original_name = "SS_A1DDF+SS_A2DDF+SS_A3DDF+SS_A1_OCWDDF+SS_A2_OCWDDF+SS_A3_OCWDDF"                                                       ; original_units = "kg/m2/s" 

#   emissions
    elif ( var == 'emibc'   ) : standard_name = "tendency_of_atmosphere_mass_content_of_elemental_carbon_dry_aerosol_particles_due_to_emission" ; long_name = "Total Emission Rate of Black Carbon Aerosol Mass" ; units = "kg m-2 s-1" ; original_name = "SFBC_A+SFBC_AC+SFBC_AI+SFBC_AX+SFBC_N+SFBC_NI+BC_AX_CMXF+BC_NI_CMXF+BC_N_CMXF" ; original_units = "kg/m2/s" ;
    elif ( var == 'emibvoc' ) : standard_name = "tendency_of_atmosphere_mass_content_of_biogenic_nmvoc_expressed_as_carbon_due_to_emission"     ; long_name = "Total Emission Rate of Biogenic NMVOC"            ; units = "kg m-2 s-1" ; original_name = "SFisoprene+SFmonoterp"   ; original_units = "kg/m2/s" 
    elif ( var == 'emidms'  ) : standard_name = "tendency_of_atmosphere_mass_content_of_dimethyl_sulfide_due_to_emission"                       ; long_name = "Total Emission Rate of DMS"                       ; units = "kg m-2 s-1" ; original_name = "SFDMS"                   ; original_units = "kg/m2/s" 
    elif ( var == 'emidust' ) : standard_name = "tendency_of_atmosphere_mass_content_of_dust_dry_aerosol_particles_due_to_emission"             ; long_name = "Total Emission Rate of Dust"                      ; units = "kg m-2 s-1" ; original_name = "SFDST_A2+SFDST_A3"       ; original_units = "kg/m2/s"
    elif ( var == 'emiisop' ) : standard_name = "tendency_of_atmosphere_mass_content_of_isoprene_due_to_emission"                               ; long_name = "Total Emission Rate of Isoprene"                  ; units = "kg m-2 s-1" ; original_name = "SFisoprene"              ; original_units = "kg/m2/s"
    elif ( var == 'emioa'   ) : standard_name = "tendency_of_atmosphere_mass_content_of_particulate_organic_matter_dry_aerosol_particles_due_to_net_chemical_production_and_emission" ; long_name = "Primary Emission and Chemical Production of Dry Aerosol Organic Matter" ; units = "kg m-2 s-1" ; original_name = "SFOM_AC+SFOM_AI+SFOM_NI+OM_NI_CMXF" ; original_units = "kg/m2/s" ;
    elif ( var == 'emiso2'  ) : standard_name = "tendency_of_atmosphere_mass_content_of_sulfur_dioxide_due_to_emission"                         ; long_name = "Total Emission Rate of SO2"                       ; units = "kg m-2 s-1" ; original_name = "SFSO2+SO2_CMXF"          ; original_units = "kg/m2/s" 
    elif ( var == 'emiso4'  ) : standard_name = "tendency_of_atmosphere_mass_content_of_sulfate_dry_aerosol_particles_due_to_emission"          ; long_name = "Total Direct Emission Rate of SO4"                ; units = "kg m-2 s-1" ; original_name = "SFSO4_PR+SO4_PR_CMXF"    ; original_units = "kg/m2/s"
    elif ( var == 'emiss'   ) : standard_name = "tendency_of_atmosphere_mass_content_of_sea_salt_dry_aerosol_particles_due_to_emission"         ; long_name = "Total Emission Rate of Sea-Salt Aerosol"          ; units = "kg m-2 s-1" ; original_name = "SFSS_A1+SFSS_A2+SFSS_A3" ; original_units = "kg/m2/s" 
    elif ( var == 'emivoc'  ) : standard_name = "tendency_of_atmosphere_mass_content_of_nmvoc_due_to_emission"                                  ; long_name = "Total Emission Rate of NMVOC"                     ; units = "kg m-2 s-1" ; original_name = "SFisoprene+SFmonoterp"   ; original_units = "kg/m2/s" 

    elif ( var == 'lwp'     ) : standard_name = "atmosphere_mass_content_of_cloud_liquid_water" ; long_name = "Liquid Water Path" ; units = "kg m-2" ; original_name = "TGCLDLWP" ; original_units = "kg/m2"

#   mass mixing ratios
    elif ( var == 'mmraerh2o' ) : standard_name = "mass_fraction_of_water_in_ambient_aerosol_particles_in_air"                         ; long_name = "Aerosol Water Mass Mixing Ratio"             ; units = "kg kg-1" ; original_name = "MMR_AH2O"      ; original_units = "kg/kg" ; cdim='3d'
    elif ( var == 'mmrbc'     ) : standard_name = "mass_fraction_of_elemental_carbon_dry_aerosol_particles_in_air"                     ; long_name = "Elemental Carbon Mass Mixing Ratio"          ; units = "kg kg-1" ; original_name = "mmr_BC"        ; original_units = "kg/kg" ; cdim='3d'  
    elif ( var == 'mmrdust'   ) : standard_name = "mass_fraction_of_dust_dry_aerosol_particles_in_air"                                 ; long_name = "Dust Aerosol Mass Mixing Ratio"              ; units = "kg kg-1" ; original_name = "mmr_DUST"      ; original_units = "kg/kg" ; cdim='3d'
    elif ( var == 'mmroa'     ) : standard_name = "mass_fraction_of_particulate_organic_matter_dry_aerosol_particles_in_air"           ; long_name = "Total Organic Aerosol Mass Mixing Ratio"     ; units = "kg kg-1" ; original_name = "mmr_OM"        ; original_units = "kg/kg" ; cdim='3d'
    elif ( var == 'mmrso4'    ) : standard_name = "mass_fraction_of_sulfate_dry_aerosol_particles_in_air"                              ; long_name = "Aerosol Sulfate Mass Mixing Ratio"           ; units = "kg kg-1" ; original_name = "mmr_SULFATE"   ; original_units = "kg/kg" ; cdim='3d'
    elif ( var == 'mmrsoa'    ) : standard_name = "mass_fraction_of_secondary_particulate_organic_matter_dry_aerosol_particles_in_air" ; long_name = "Secondary Organic Aerosol Mass Mixing Ratio" ; units = "kg kg-1" ; original_name = "SOA_NA+SOA_A1" ; original_units = "kg/kg" ; cdim='3d'
    elif ( var == 'mmrss'     ) : standard_name = "mass_fraction_of_sea_salt_dry_aerosol_particles_in_air"                             ; long_name = "Sea-Salt Aerosol Mass Mixing Ratio"          ; units = "kg kg-1" ; original_name = "mmr_SALT"      ; original_units = "kg/kg" ; cdim='3d'

#   ozone
    elif ( var == 'o3'        ) : standard_name = "mole_fraction_of_ozone_in_air" ; long_name = "Mole Fraction of O3" ; units = "mol mol-1" ; original_name = "ozone" ; original_units = "mol/mol"  ; cdim='3d'

#   aerosol optical depth
    elif ( var == 'od440aer'    ) : standard_name = "atmosphere_optical_thickness_due_to_ambient_aerosol_particles"                            ; long_name = "Ambient Aerosol Optical Thickness at 440nm"  ; units = "1" ; original_name = "DOD440" 
    elif ( var == 'od550aer'    ) : standard_name = "atmosphere_optical_thickness_due_to_ambient_aerosol_particles"                            ; long_name = "Ambient Aerosol Optical Thickness at 550nm"  ; units = "1" ; original_name = "DOD550"                                 ; coordinates = "wavelength"
    elif ( var == 'od550aerh2o' ) : standard_name = "atmosphere_optical_thickness_due_to_water_in_ambient_aerosol_particles"                   ; long_name = "Aerosol Water Optical Thickness at 550nm"    ; units = "1" ; original_name = "DOD550-OD550DRY"                        ; coordinates = "wavelength"
    elif ( var == 'od550bc'     ) : standard_name = "atmosphere_optical_thickness_due_to_black_carbon_ambient_aerosol"                         ; long_name = "Black Carbon Optical Thickness at 550nm"     ; units = "1" ; original_name = "D550_BC"                                ; coordinates = "wavelength" 
    elif ( var == 'od550csaer'  ) : standard_name = "atmosphere_optical_thickness_due_to_ambient_aerosol_particles"                            ; long_name = "Ambient Aerosol Optical Thickness at 550nm"  ; units = "1" ; original_name = "CDOD550"                                ; coordinates = "wavelength" 
    elif ( var == 'od550duest'  ) : standard_name = "atmosphere_optical_thickness_due_to_dust_ambient_aerosol_particles"                       ; long_name = "Dust Optical Thickness at 550nm"             ; units = "1" ; original_name = "D550_DU"                                ; coordinates = "wavelength" 
    elif ( var == 'od550lt1aer' ) : standard_name = "atmosphere_optical_thickness_due_to_pm1_ambient_aerosol_particles"                        ; long_name = "Ambient Fine Aerosol Optical Depth at 550nm" ; units = "1" ; original_name = "DLT_SS+DLT_DUST+DLT_SO4+DLT_BC+DLT_POM" ; coordinates = "wavelength"
    elif ( var == 'od550oa'     ) : standard_name = "atmosphere_optical_thickness_due_to_particulate_organic_matter_ambient_aerosol_particles" ; long_name="Total Organic Aerosol Optical Depth at 550nm"  ; units = "1" ; original_name = "D550_POM"                               ; coordinates = "wavelength" 
    elif ( var == 'od550so4'    ) : standard_name = "atmosphere_optical_thickness_due_to_sulfate_ambient_aerosol_particles"                    ; long_name = "Sulfate Aerosol Optical Depth at 550nm"      ; units = "1" ; original_name = "D550_SO4"                               ; coordinates = "wavelength" 
    elif ( var == 'od550ss'     ) : standard_name = "atmosphere_optical_thickness_due_to_sea_salt_ambient_aerosol_particles"                   ; long_name = "Sea-Salt Aerosol Optical Depth at 550nm"     ; units = "1" ; original_name = "D550_SS"                                ; coordinates = "wavelength" 
    elif ( var == 'od870aer'    ) : standard_name = "atmosphere_optical_thickness_due_to_ambient_aerosol_particles"                            ; long_name = "Ambient Aerosol Optical Depth at 870nm"      ; units = "1" ; original_name = "DOD870"

#   oh
    elif ( var == 'oh' ) : standard_name = "mole_fraction_of_hydroxyl_radical_in_air" ; long_name = "OH Volume Mixing Ratio" ; units = "mol mol-1" ; original_name = "OH_aft"  ; cdim='3d'

#   reffclwtop
    elif ( var == 'reffclwtop' ) :standard_name = "effective_radius_of_cloud_liquid_water_particles_at_liquid_water_cloud_top" ; long_name = "Cloud-Top Effective Droplet Radius" ; units = "m" ; original_name = "REFFCLWMODIS/CLWMODIS"

#   toa radiative fluxes
    elif ( var == 'rlutaf'      ) : standard_name = "toa_outgoing_longwave_flux"                                    ; long_name = "TOA Outgoing Aerosol-Free Longwave Radiation"             ; units = "W m-2" ; original_name = "FLNT_DRF" ; original_units = "W/m^2" 
    elif ( var == 'rlutcsaf'    ) : standard_name = "toa_outgoing_longwave_flux_assuming_clear_sky"                 ; long_name = "TOA Outgoing Clear-Sky, Aerosol-Free Longwave Radiation"  ; units = "W m-2" ; original_name = "FLNTCDRF" ; original_units = "W/m^2"
    elif ( var == 'rsutaf'      ) : standard_name = "toa_outgoing_shortwave_flux"                                   ; long_name = "TOA Outgoing Aerosol-Free Shortwave Radiation"            ; units = "W m-2" ; original_name = "FSNT_DRF" ; original_units = "W/m^2"
    elif ( var == 'rsutcsaf'    ) : standard_name = "toa_outgoing_shortwave_flux_assuming_clear_sky_and_no_aerosol" ; long_name = "TOA Outgoing Clear-Sky, Aerosol-Free Shortwave Radiation" ; units = "W m-2" ; original_name = "FSNTCDRF" ; original_units = "W/m^2"

#   so2
    elif ( var == 'so2' ) : standard_name = "mole_fraction_of_sulfur_dioxide_in_air" ; long_name = "SO2 Volume Mixing Ratio" ; units = "mol mol-1" ; original_name = "SO2" ; original_units = "mol/mol" ; cdim='3d'

#   wind 
    elif ( var == 'ua' ) : standard_name = "eastward_wind"  ; long_name = "Eastward Wind"  ; units = "m s-1" ; original_name = "U" ; original_units = "m/s" ; cdim='3d'
    elif ( var == 'va' ) : standard_name = "northward_wind" ; long_name = "Northward Wind" ; units = "m s-1" ; original_name = "V" ; original_units = "m/s" ; cdim='3d'

#   wet deposition
    elif ( var == 'wetbc'   ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_elemental_carbon_dry_aerosol_particles_due_to_wet_deposition"           ; long_name = "Wet Deposition Rate of Black Carbon Aerosol Mass"        ; units = "kg m-2 s-1" ; original_name = "BC_ACSFWET+BC_AISFWET+BC_ASFWET+BC_AXSFWET+BC_NISFWET+BC_NSFWET+BC_AC_OCWSFWET+BC_AI_OCWSFWET+BC_A_OCWSFWET+BC_NI_OCWSFWET+BC_N_OCWSFWET"    ; original_units = "kg/m2/s"
    elif ( var == 'wetdust' ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_dust_dry_aerosol_particles_due_to_wet_deposition"                       ; long_name = "Wet Deposition Rate of Dust"                             ; units = "kg m-2 s-1" ; original_name = "DST_A2SFWET+DST_A3SFWET+DST_A2_OCWSFWET+DST_A3_OCWSFWET"                                                                                     ; original_units = "kg/m2/s"
    elif ( var == 'wetoa'   ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_particulate_organic_matter_dry_aerosol_particles_due_to_wet_deposition" ; long_name = "Wet Deposition Rate of Dry Aerosol Total Organic Matter" ; units = "kg m-2 s-1" ; original_name = "OM_ACSFWET+OM_AISFWET+OM_NISFWET+OM_AC_OCWSFWET+OM_AI_OCWSFWET+OM_NI_OCWSFWET+SOA_A1SFWET+SOA_NASFWET+SOA_A1_OCWSFWET+SOA_NA_OCWSFWET"       ; original_units = "kg/m2/s"
    elif ( var == 'wetso2'  ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_sulfur_dioxide_due_to_wet_deposition"                                   ; long_name = "Wet Deposition Rate of SO2"                              ; units = "kg m-2 s-1" ; original_name = "WD_A_SO2"                                                                                                                                    ; original_units = "kg/m2/s"
    elif ( var == 'wetso4'  ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_sulfate_dry_aerosol_particles_due_to_wet_deposition"                    ; long_name = "Wet Deposition Rate of SO4"                              ; units = "kg m-2 s-1" ; original_name = "SO4_A1SFWET+SO4_A2SFWET+SO4_ACSFWET+SO4_NASFWET+SO4_PRSFWET+SO4_A1_OCWSFWET+SO4_A2_OCWSFWET+SO4_AC_OCWSFWET+SO4_NA_OCWSFWET+SO4_PR_OCWSFWET" ; original_units = "kg/m2/s" 
    elif ( var == 'wetss'   ) : standard_name = "minus_tendency_of_atmosphere_mass_content_of_sea_salt_dry_aerosol_particles_due_to_wet_deposition"                   ; long_name = "Wet Deposition Rate of Sea-Salt Aerosol"                 ; units = "kg m-2 s-1" ; original_name = "SS_A1SFWET+SS_A2SFWET+SS_A3SFWET+SS_A1_OCWSFWET+SS_A2_OCWSFWET+SS_A3_OCWSFWET"                                                               ; original_units = "kg/m2/s" 
#   zg
    elif ( var == 'zg'      ) : standard_name = "geopotential_height" ; long_name = "Geopotential Height" ; units = "m" ; original_name = "Z3" ;
    elif ( var == 'ztp'     ) : standard_name = "tropopause_altitude" ; long_name = "Tropopause Altitude Above Geoid" ; units = "m" ; original_name = "TROP_Z" 
#
# ORIGINAL NORESM
    elif ( var == 'CDNUMC'  ) : standard_name = "vertically_integrated_droplet_concentration" ; long_name = "Vertically integrated droplet concentration" ; units = "m-2" ; original_name = var ;

# Emon
#---------------------------------------
    elif ( var == 'loaddust' ) : standard_name = "atmosphere_mass_content_of_dust_dry_aerosol_particles"     ; long_name = "Load of Dust"             ; units = "kg m-2" ; original_name = "DST_A2+DST_A3" ;
    elif ( var == 'loadss'   ) : standard_name = "atmosphere_mass_content_of_sea_salt_dry_aerosol_particles" ; long_name = "Load of Sea-Salt Aerosol" ; units = "kg m-2" ; original_name = "SS_A1+SS_A2+SS_A3" 
 
    else :
        print('No var recognized : ', var) 
        quit()

    data={ 'standard_name' : standard_name, \
           'long_name'     : long_name, \
           'units'         : units, \
           'original_name' : original_name, \
           'cdim'          : cdim }

    return data  
