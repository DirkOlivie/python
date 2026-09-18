import stool

def getcmorvarcomponents(var):
#-----------------------
    '''


    '''
    cnoemer = None

#   airmass
    if (   var == 'abs550aer' ) : clist=['ABS550']           ; wlist=[1.] ; vtype='Column'  
    elif ( var == 'airmass' )   : clist=['AIRMASSL']          ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'bldep'  )    : clist=['PBLH']             ; wlist=[1.] ; vtype='Surface'

#   temperature
    elif ( var == 'tas'    ) : clist=['TREFHT']          ; wlist=[1.]
    elif ( var == 'ta'     ) : clist=['T']               ; wlist=[1.]
    elif ( var == 'ts'     ) : clist=['TS']              ; wlist=[1.]
#
#   cloud droplet number concentration
#    elif ( var == 'ccn'    ) : clist
    elif ( var == 'cdnc'   ) : clist=['AWNC']            ; wlist=[1.] ; cnoemer='FREQL'
#
#   chemical production 
    elif ( var == 'chepsoa' ) : clist=stool.addbeg('GS_SOA,'['_LV','_SV']) ; wlist=[1.,1.]

#
#   dry deposition
    elif ( var == 'drybc'  ) : clist=stool.addend(stool.addbeg('BC_',['N','NI','A','AI','AX','AC']+stool.addend(['N','NI','A','AI'     ,'AC'],'_OCW')),'DDF') ; wlist=[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.] ; vtype='Surface'
    elif ( var == 'drydust') : clist=stool.addend(stool.addbeg('DST_',['A2','A3']                 +stool.addend(['A2','A3']                  ,'_OCW')),'DDF') ; wlist=[1.,1.,1.,1.]                      ; vtype='Surface'
    elif ( var == 'dryo3'  ) : clist=['DRY_O3'] ; wlist=[1.]
    elif ( var == 'dryoa'  ) : clist=stool.addend(stool.addbeg('OM_',['NI','AI','AC']             +stool.addend(['NI','AI','AC']             ,'_OCW')),'DDF') ; wlist=[1.,1.,1.,1.,1.,1.]                ; vtype='Surface'
    elif ( var == 'dryso2' ) : clist=['DRY_SO2'] ; wlist=[1.]
    elif ( var == 'dryso4' ) : clist=stool.addend(stool.addbeg('SO4_',['NA','PR','A1','A2','AC']  +stool.addend(['NA','PR','A1','A2','AC']   ,'_OCW')),'DDF') ; wlist=[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]    ; vtype='Surface'
    elif ( var == 'dryss'  ) : clist=stool.addend(stool.addbeg('SS_',['A1','A2','A3']             +stool.addend(['A1','A2','A3']             ,'_OCW')),'DDF') ; wlist=[1.,1.,1.,1.,1.,1.]                ; vtype='Surface'

#   wetdeposition
    elif ( var == 'wetbc'  ) : clist=stool.addend(stool.addbeg('BC_',['N','NI','A','AI','AX','AC']+stool.addend(['N','NI','A','AI'     ,'AC'],'_OCW')),'SFWET') ; wlist=[-1.,-1.,-1.,-1.,-1.,-1.,-1.,-1.,-1.,-1.,-1.] ; vtype='Surface'
    elif ( var == 'wetdust') : clist=stool.addend(stool.addbeg('DST_',['A2','A3']                 +stool.addend(['A2','A3'],'_OCW'                  )),'SFWET') ; wlist=[-1.,-1.,-1.,-1.]                             ; vtype='Surface'
    elif ( var == 'wetoa'  ) : clist=stool.addend(stool.addbeg('OM_',['NI','AI','AC']             +stool.addend(['NI','AI','AC'],'_OCW'             )),'SFWET') ; wlist=[-1.,-1.,-1.,-1.,-1.,-1.]                     ; vtype='Surface'
    elif ( var == 'wetso2' ) : clist=['WD_SO2'] ; wlist=[1.]
    elif ( var == 'wetso4' ) : clist=stool.addend(stool.addbeg('SO4_',['NA','PR','A1','A2','AC']  +stool.addend(['NA','PR','A1','A2','AC']   ,'_OCW')),'SFWET') ; wlist=[-1.,-1.,-1.,-1.,-1.,-1.,-1.,-1.,-1.,-1.]     ; vtype='Surface'
    elif ( var == 'wetss'  ) : clist=stool.addend(stool.addbeg('SS_',['A1','A2','A3']             +stool.addend(['A1','A2','A3']             ,'_OCW')),'SFWET') ; wlist=[-1.,-1.,-1.,-1.,-1.,-1.]                     ; vtype='Surface'

#   emissions
#    elif ( var == 'emiaco' ) :    
#    elif ( var == 'emianox' ) :    
#    elif ( var == 'emiaoa' ) :    
    elif ( var == 'emibc' ) :    clist=stool.addbeg('SFBC_',['N','AX'])+stool.addend(stool.addbeg('BC_',['N','AX','NI']),'_CMXF')
#    elif ( var == 'emibvoc' ) : 
#    elif ( var == 'emico' ) :    
    elif ( var == 'emidms' ) :    clist=['SFDMS']                           ; wlist=[1.]    ; vtype='Surface'
    elif ( var == 'emidust' ) :   clist=stool.addbeg('SFDST_',['A2','A3'])  ; wlist=[1.,1.] ; vtype='Surface' 
#    elif ( var == 'emiisop' ) :    
#    elif ( var == 'emilnox' ) :    
#    elif ( var == 'eminh3'  ) :    
#    elif ( var == 'eminox'  ) :    
    elif ( var == 'emioa'   ) : clist=['SFOM_NI','OM_NI_CLXF']               ; wlist=[1.,1.]    ; vtype='Surface'
    elif ( var == 'emiso2'  ) : clist=['SFSO2','SO2_CLXF']                   ; wlist=[1.,1.]    ; vtype='Surface'
    elif ( var == 'emiso4'  ) : clist=['SFSO4_PR','SO4_PR_CLXF']             ; wlist=[1.,1.]    ; vtype='Surface'
    elif ( var == 'emiss'   ) : clist=stool.addbeg('SFSS_',['A1','A2','A3']) ; wlist=[1.,1.,1.] ; vtype='Surface' 
#    elif ( var == 'emivoc'  ) :    
   
#   aerosol mass mixing ratio
    elif ( var == 'mmroa'  ) :  clist=['mmr_OM']                       ; wlist=[1.]    ; vtype='ModelLevel' 
    elif ( var == 'mmrsoa' ) :  clist=stool.addbeg('SOA_',['NA','A1']) ; wlist=[1.,1.] ; vtype='ModelLevel' 
    elif ( var == 'mmrbc'  ) :  clist=['mmr_BC']                       ; wlist=[1.]    ; vtype='ModelLevel' 
    elif ( var == 'mmrso4' ) :  clist=['mmr_SULFATE']                  ; wlist=[1.]    ; vtype='ModelLevel' 
    elif ( var == 'mmrss'  ) :  clist=['mmr_SALT']                     ; wlist=[1.]    ; vtype='ModelLevel' 
    elif ( var == 'mmrdust') :  clist=['mmr_DUST']                     ; wlist=[1.]    ; vtype='ModelLevel' 








#   latent and sensible heatflux
    elif ( var == 'hfls'   ) : clist=['LHFLX']           ; wlist=[1.]     
    elif ( var == 'hfss'   ) : clist=['SHFLX']           ; wlist=[1.]    
#
#   precipitation
    elif ( var == 'pr'     ) : clist=['PRECC','PRECL']   ; wlist=[1., 1.]
#
#   surface pressure
    elif ( var == 'ps'     ) : clist=['PS']              ; wlist=[1.]
    elif ( var == 'psl'    ) : clist=['PSL']             ; wlist=[1.] ; vtype='Surface'

#   radiation fluxes
    elif ( var == 'rlds'   ) : clist=['FLDS']            ; wlist=[1.]     # Surface Downwelling Longwave Radiation
    elif ( var == 'rlus'   ) : clist=['FLDS','FLNS']     ; wlist=[1., 1.] # Surface Upwelling Longwave Radiation
    elif ( var == 'rsds'   ) : clist=['FSDS']            ; wlist=[1.]     # Surface Downweliing Shortwave Radiation
    elif ( var == 'rsus'   ) : clist=['FSDS','FSNS']     ; wlist=[1.,-1.] # Surface Upwelling Shortwave Radiation
    elif ( var == 'rsdscs' ) : clist=['FSDSC']           ; wlist=[1.]     # Surface Downwelling Clear-Sky Shortwave Radiation
    elif ( var == 'rsuscs' ) : clist=['FSDSC','FSNSC']   ; wlist=[1.,-1.] # Surface Upwelling Clear-Sky Shortwave Radiation
    elif ( var == 'rldscs' ) : clist=['FLDSC']           ; wlist=[1.]     # Surface Downwelling Clearsky Longwave Radiation
    elif ( var == 'rsdt'   ) : clist=['FSUTOA','FSNTOA'] ; wlist=[1., 1.] # TOA Incident Shortwave Radiation - FSDTOA not in EmissionMIP simulations
    elif ( var == 'rsut'   ) : clist=['FSUTOA']          ; wlist=[1.]     # TOA Outgoing Shortwave Radiation
    elif ( var == 'rlut'   ) : clist=['FLUT']            ; wlist=[1.]     # TOA Outgoing Longwave Radiation
    elif ( var == 'rlutcs' ) : clist=['FLUTC']           ; wlist=[1.]     # TOA Outgoing Clear-Sky Longwave Radiation
    elif ( var == 'rsutcs' ) : clist=['FSUTOA','FSNTOA','FSNTOAC'] ; wlist=[1.,1.,-1.] #

    elif ( var == 'rlutaf'      ) : clist=['FLNT_DRF'] ; wlist=[1.]
    elif ( var == 'rlutcsaf'    ) : clist=['FLNTCDRF'] ; wlist=[1.]
    elif ( var == 'rsutaf'      ) : clist=['FSNT_DRF'] ; wlist=[-1.]
    elif ( var == 'rsutcsaf'    ) : clist=['FSNTCDRF'] ; wlist=[-1.]

    elif ( var == 'rtmt' ) : clist=['FSNT','FLNT'] ; wlist=[1.,-1.]
#
#   aerosol burden
    elif ( var == 'loadbc'  ) : clist=['cb_BC']          ; wlist=[1.] 
    elif ( var == 'loadoa'  ) : clist=['cb_OM']          ; wlist=[1.] 
    elif ( var == 'loadss'  ) : clist=['cb_SALT']        ; wlist=[1.] 
    elif ( var == 'loaddust') : clist=['cb_DUST']        ; wlist=[1.] 
    elif ( var == 'loadso4' ) : clist=['cb_SULFATE']     ; wlist=[1.] 
    elif ( var == 'loadso2' ) : clist=['cb_SO2']         ; wlist=[1.]
#
#   aod
    elif ( var == 'od440aer'    ) : clist=['DOD440']                                         ; wlist=[1.]
    elif ( var == 'od550aer'    ) : clist=['DOD550']                                         ; wlist=[1.]
    elif ( var == 'od550aerh2o' ) : clist=['DOD550','OD550DRY']                              ; wlist=[1.,-1.]
    elif ( var == 'od550bc'     ) : clist=['D550_BC']                                        ; wlist=[1.]
    elif ( var == 'od550csaer'  ) : clist=['CDOD550']                                        ; wlist=[1.]
    elif ( var == 'od550duest'  ) : clist=['D550_DU']                                        ; wlist=[1.]                             
    elif ( var == 'od550lt1aer' ) : clist=['DLT_SS','DLT_DUST','DLT_SO4','DLT_BC','DLT_POM'] ; wlist=[1.,1.,1.,1.,1.]
    elif ( var == 'od550oa'     ) : clist=['D550_POM']                                       ; wlist=[1.]
    elif ( var == 'od550so4'    ) : clist=['D550_SO4']                                       ; wlist=[1.]                      
    elif ( var == 'od550ss'     ) : clist=['D550_SS']                                        ; wlist=[1.]                 
#
#   wet deposition

#   reaction rate
#    elif (var == 'jno2' ) :  
#    elif (var == '' ) :  
#    elif (var == 'lossch4' ) :  
#    elif (var == 'lossco' ) :  
#    elif (var == 'lossn2o' ) :  

#    elif (var== 'o3loss') : 
#    elif (var== 'o3prod') :



#   chemical species
    elif ( var == 'co'  ) : clist=['CO'] ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'ch4' ) : clist=['CH4'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'dms' ) : clist=['DMS'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'h2o' ) : clist=['H2O'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'hcho' ) : clist=['HCHO'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'hcl' ) : clist=['HCL'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'hno3' ) : clist=['HNO3'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'isop' ) : clist=['ISOP'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'no'  ) : clist=['NO'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'no2' ) : clist=['NO2'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'pan' ) : clist=['PAN'] ; wlist=[1.] ; vype='ModelLevel'
    elif ( var == 'oh'  ) : clist=['OH'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'o3'  ) : clist=['O3'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'so2'  ) : clist=['SO2'] ; wlist=[1.] ; vtype='ModelLevel'
#

    elif ( var == 'lwp' ) : clist=['TGCLDLWP'] ; wlist=[0.001] ; vtype = 'Surface'
#    elif ( var == 'pfull' ) 
#    elif ( var == 'phalf' )
#    elif ( var == 'photo1d' ) :
#    elif ( var == 'pod0' ) :
    elif ( var == 'ps' ) : clist=['PS'] ; wlist=[1.] ; vtype='Surface'
    elif ( var == 'ptp' ) : clist=['TROP_P'] ; wlist=[1.] ; vtype='Surface' # 'Tropopause air pressure [Pa]'
#    elif ( var == 'reffclwtop' ) : # Two options
#    elif ( var == 'toz'    ) : # total ozone column [m]
#    elif ( var == 'tropoz' ) : # tropospheric ozone column [m]
#    elif ( var == 'ttop' ) # temperature at cloud top
    elif ( var == 'ua' ) : clist=['U'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'va' ) : clist=['V'] ; wlist=[1.] ; vtype='ModelLevel'
#    elif ( var == 'wa' ) :
    elif ( var == 'ztp') : clist=['TROP_Z'] ; wlist=[1.] ; vtype='Surface'
    elif ( var == 'zg' ) : clist=['Z3'] ; wlist=[1.] ; vtype='ModelLevel' # geopotential height [m]
 
#   Amon
    elif ( var == 'ci'    ) : clist=['FREQZM']   ; wlist=[1.] ; vtype='Surface' # Fraction of Time Convection Occurs (in NorESM : only ZM)
    elif ( var == 'cl'    ) : clist=['CLOUD']    ; wlist=[1.] ; vtype='ModelLevel' # 
    elif ( var == 'cli'   ) : clist=['CLDICE']   ; wlist=[1.] ; vtype='ModelLevel' # Mass fraction of cloud ice
    elif ( var == 'clivi' ) : clist=['TGCLDIWP'] ; wlist=[1.] ; vtype='Column' #
    elif ( var == 'clt'   ) : clist=['CLDTOT']   ; wlist=[1.] ; vtype='Column'
    elif ( var == 'clw'   ) : clist=['CLDLIQ']   ; wlist=[1.] ; vtype='Column'
    elif ( var == 'clwvi' ) : clist=['TGCLDLWP'] ; wlist=[1.] ; vtype='Column'

    elif ( var == 'evspsbl' ) : clist=['QFLX']  ; wlist=[1.] ; vtype='Surface'
    elif ( var == 'hfls'    ) : clist=['LHFLX'] ; wlist=[1.] ; vtype='Surface' 
    elif ( var == 'hfss'    ) : clist=['SHFLX'] ; wlist=[1.] ; vtype='Surface'

    elif ( var == 'hur'  ) : clist=['RELHUM']  ; wlist=[1.]                      # Relative Humidity - is already in % in NorESM
    elif ( var == 'hurs' ) : clist=['RHREFHT'] ; wlist=[1.] ; vtype='Surface'
    elif ( var == 'hus'  ) : clist=['Q']       ; wlist=[1.] ; vtype='ModelLevel' # Specific Humidity
    elif ( var == 'huss' ) : clist=['QREFHT']  ; wlist=[1.] ; vtype='Surface'    

    elif ( var == 'pr'   ) : clist=['PRECT']           ; wlist=[1.]    ; vtype='Surface'
    elif ( var == 'prc'  ) : clist=['PRECC']           ; wlist=[1.]    ; vtype='Surface'
    elif ( var == 'prsn' ) : clist=['PRECSC','PRECSL'] ; wlist=[1.,1.] ; vtype='Surface'
    elif ( var == 'prw'  ) : clist=['TMQ']             ; wlist=[1.]    ; vtype='Column'  # water vapour path vertically integrated

    elif ( var == 'sfcWind' ) : clist=['U10'] ; wlist=[1.] ; vtype='Surface' 

    elif ( var == 'tauu' ) : clist=['TAUX'] ; wlist=[1.] ; vtype='Surface'
    elif ( var == 'tauv' ) : clist=['TAUY'] ; wlist=[1.] ; vtype='Surface'

    elif ( var == 'wap' ) : clist=['OMEGA'] ; wlist=[1.] ; vtype='ModelLevel'
#
#   ORIGINAL NORESM VARIABLES
    elif ( var == 'CDNUMC' ) : clist=[var] ; wlist=[1.]

    else : 
        print('++++ getcmorvarcomponents +++')
        print('No var recognized : ',var)
        quit()

    if ( len(clist) != len(wlist) ) :
        print('++++ getcmorvarcomponents +++')
        print('clist and wlist have different length :', len(clist), len(wlist))
        quit()

    print('+++ getcmorvarcomponents +++')
    print('clist : ', clist)
    print('wlist : ', wlist)
    print('cnoemer : ', cnoemer)
#
    return clist, wlist, cnoemer
