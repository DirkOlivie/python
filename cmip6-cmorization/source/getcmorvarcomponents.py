import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')

import stool

def getcmorvarcomponents(var):
#-----------------------
    '''
    INPUT
        var

    RETURN
        clist
        wlist
        cnoemer : None | ...
        action  : None | expand (pfull and phalf) | columnintegrate)



    CALLED BY
        obtainfield    

    '''
    grav = 9.81

    Mw_N   = 14.0067
    Mw_NO  = 30.0061
    Mw_NO2 = 46.0055
#
    cnoemer = None
    action = None



#   airmass
    if (   var == 'areacella' ) : clist=['GRIDAREA']         ; wlist=[1.] ; vtype='Surface'
    elif ( var == 'orog'      ) : clist=['PHIS']             ; wlist=[1.] ; vtype='Surface'   # unit conversion and scaling happens elsewhere
    elif ( var == 'volume'    ) : clist=['PS']               ; wlist=[1.] ; vtype='ModelLevel'  ; action='special'
    elif ( var == 'abs550aer' ) : clist=['ABS550']           ; wlist=[1.] ; vtype='Column'  
    elif ( var == 'airmass'   ) : clist=['AIRMASSL']         ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'bldep'     ) : clist=['PBLH']             ; wlist=[1.] ; vtype='Surface'

#   temperature
    elif ( var == 'tas'    ) : clist=['TREFHT']          ; wlist=[1.]
    elif ( var == 'ta'     ) : clist=['T']               ; wlist=[1.]
    elif ( var == 'ts'     ) : clist=['TS']              ; wlist=[1.]
#
#   cloud droplet number concentration
#    elif ( var == 'ccn'    ) : clist
    elif ( var == 'cdnc'    ) : clist=['AWNC']            ; wlist=[1.] ; cnoemer='FREQL'
#
#   chemical production 
    elif ( var == 'chepsoa' ) : clist=stool.addbeg('GS_SOA',['_LV','_SV']) ; wlist=[1.,1.]
#
#   dry deposition
    elif ( var == 'drybc'  ) : clist=stool.addend(stool.addbeg('BC_',['N','NI','A','AI','AX','AC']+stool.addend(['N','NI','A','AI'     ,'AC'],'_OCW')),'DDF') ; wlist=[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.] ; vtype='Surface'
    elif ( var == 'drydust') : clist=stool.addend(stool.addbeg('DST_',['A2','A3']                 +stool.addend(['A2','A3']                  ,'_OCW')),'DDF') ; wlist=[1.,1.,1.,1.]                      ; vtype='Surface'
    elif ( var == 'dryo3'  ) : clist=['DF_O3'] ; wlist=[1.]
    elif ( var == 'dryoa'  ) : clist=stool.addend(stool.addbeg('OM_',['NI','AI','AC']             +stool.addend(['NI','AI','AC']             ,'_OCW')),'DDF') ; wlist=[1.,1.,1.,1.,1.,1.]                ; vtype='Surface'
    elif ( var == 'dryso2' ) : clist=['DF_SO2'] ; wlist=[1.]
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
    elif ( var == 'emibc'   ) : clist=stool.addbeg('SFBC_',['N','AX'])+stool.addend(stool.addbeg('BC_',['N','AX','NI']),'_CMXF') ; wlist=[1.,1.,1.,1.,1.]
    elif ( var == 'emibvoc' ) : clist=stool.addbeg('SF',['ISOP','MTERP']); wlist=[1.,1.] 
    elif ( var == 'emico'   ) : clist=['SFCO','CO_CMXF'] ; wlist=[1.,1.]
    elif ( var == 'emidms'  ) : clist=['SFDMS']                           ; wlist=[1.]    ; vtype='Surface'
    elif ( var == 'emidust' ) : clist=stool.addbeg('SFDST_',['A2','A3'])  ; wlist=[1.,1.] ; vtype='Surface' 
    elif ( var == 'emiisop' ) : clist=['SFISOP']; wlist=[1.] ; vtype='Surface'   
    elif ( var == 'emih2'   ) : clist=['SFH2']; wlist=[1.] ; vtype='Surface'   
    elif ( var == 'eminh3'  ) : clist=['SFNH3'] ; wlist=[1.] ; vtype='Surface'
    elif ( var == 'eminox'  ) : clist=['SFNO','NO_CMXF','SFNO2','NO2_CMXF'] ; wlist=[Mw_N/Mw_NO, Mw_N/Mw_NO, Mw_N/Mw_NO2, Mw_N/Mw_NO2] ; vtype='Surface'  # as N   
#    elif ( var == 'emilnox' ) :    
    elif ( var == 'emioa'   ) : clist=['SFOM_NI','OM_NI_CMXF']               ; wlist=[1.,1.]    ; vtype='Surface'
    elif ( var == 'emiso2'  ) : clist=['SFSO2','SO2_CMXF']                   ; wlist=[1.,1.]    ; vtype='Surface'
    elif ( var == 'emiso4'  ) : clist=['SFSO4_PR','SO4_PR_CMXF']             ; wlist=[1.,1.]    ; vtype='Surface'
    elif ( var == 'emiss'   ) : clist=stool.addbeg('SFSS_',['A1','A2','A3']) ; wlist=[1.,1.,1.] ; vtype='Surface' 
#    elif ( var == 'emivoc'  ) :    
   
#   aerosol mass mixing ratio
    elif ( var == 'mmroa'  ) :  clist=['mmr_OM']                       ; wlist=[1.]    ; vtype='ModelLevel' 
    elif ( var == 'mmrsoa' ) :  clist=stool.addbeg('SOA_',['NA','A1']) ; wlist=[1.,1.] ; vtype='ModelLevel' 
    elif ( var == 'mmrbc'  ) :  clist=['mmr_BC']                       ; wlist=[1.]    ; vtype='ModelLevel' 
    elif ( var == 'mmrso4' ) :  clist=['mmr_SULFATE']                  ; wlist=[1.]    ; vtype='ModelLevel' 
    elif ( var == 'mmrss'  ) :  clist=['mmr_SALT']                     ; wlist=[1.]    ; vtype='ModelLevel' 
    elif ( var == 'mmrdust') :  clist=['mmr_DUST']                     ; wlist=[1.]    ; vtype='ModelLevel' 

    elif ( var == 'mmraerh2o' ) : clist=['MMR_AH2O']                   ; wlist=[1.]    ; vtype='ModelLevel'


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
    elif ( var == 'od550dust'   ) : clist=['D550_DU']                                        ; wlist=[1.]                             
    elif ( var == 'od550lt1aer' ) : clist=['DLT_SS','DLT_DUST','DLT_SO4','DLT_BC','DLT_POM'] ; wlist=[1.,1.,1.,1.,1.]
    elif ( var == 'od550oa'     ) : clist=['D550_POM']                                       ; wlist=[1.]
    elif ( var == 'od550so4'    ) : clist=['D550_SO4']                                       ; wlist=[1.]                      
    elif ( var == 'od550ss'     ) : clist=['D550_SS']                                        ; wlist=[1.]                 
    elif ( var == 'od870aer'    ) : clist=['DOD870']                                         ; wlist=[1.]
#
#   aodvis
    elif ( var == 'aodvisvolso4') : clist=['AODVVOLC'] ; cnoemer='DAYFOC' ; wlist=[1.]


#   wet deposition

#   reaction rate
#    elif (var == 'jno2' ) :  
#    elif (var == '' ) :  
#    elif (var== 'o3loss') : 
#    elif (var== 'o3prod') :

    elif ( var == 'siconc'  ) : clist=['ICEFRAC'] ; wlist=[1.] ; vtype='Surface' 

#   chemical species    
    elif ( var == 'c2h2'  ) : clist=['C2H2'] ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'c2h4'  ) : clist=['C2H4'] ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'c2h6'  ) : clist=['C2H6'] ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'c3h6'  ) : clist=['C3H6'] ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'c3h8'  ) : clist=['C3H8'] ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'c6h6'  ) : clist=['BENZENE'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'ch3cho' ) : clist=['CH3CHO'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'ch3coch3'  ) : clist=['CH3COCH3'] ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'ch3cooh'   ) : clist=['CH3COOH'] ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'ch3oh'     ) : clist=['CH3OH'] ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'ch4' ) : clist=['CH4'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'co'    ) : clist=['CO']   ; wlist=[1.]  ; vtype='ModelLevel'
    elif ( var == 'dms' ) : clist=['DMS'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'h2o' ) : clist=['H2O'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'hcho' ) : clist=['CH2O'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'hcooh' ) : clist=['HCOOH'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'hcl' ) : clist=['HCL'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'hno3' ) : clist=['HNO3'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'ho2' ) : clist=['HO2'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'isop' ) : clist=['ISOP'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'nh3' ) : clist=['NH3'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'mhp' ) : clist=['CH3OOH'] ; wlist=[1.] ; vtype='ModelLevel' # methyl hydroperoxide
    elif ( var == 'mtp' ) : clist=['MTERP'] ; wlist=[1.] ; vtype='ModelLevel' # monoterpenes
    elif ( var == 'no'  ) : clist=['NO'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'no2' ) : clist=['NO2'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'no3' ) : clist=['NO3'] ; wlist=[1.] ; vtype='ModelLevel'
#   elif ( var == 'n2o' ) : clist=['N2OCHEM'] ; wlist=[1.] ; vtype='ModelLevel'  # N2OCHEM !!!
    elif ( var == 'n2o' ) : clist=['N2O']     ; wlist=[1.] ; vtype='ModelLevel'  # N2O     !!!
    elif ( var == 'pan' ) : clist=['PAN'] ; wlist=[1.] ; vype='ModelLevel'
    elif ( var == 'oh'  ) : clist=['OH'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'o3'  ) : clist=['O3'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'o1d'  ) : clist=['O1D'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'so2'  ) : clist=['SO2'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'toluene'  ) : clist=['TOLUENE'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'h2'  ) : clist=['H2'] ; wlist=[1.] ; vtype='ModelLevel'
#
    elif ( var == 'o3surface'  ) : clist=['O3_SRF'] ; wlist=[1.] ; vtype='Surface'
#
#   emissions
    elif ( var == 'emic2h2'     ) : clist=['SFC2H2']     ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emic2h4'     ) : clist=['SFC2H4']     ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emic2h6'     ) : clist=['SFC2H6']     ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emic3h6'     ) : clist=['SFC3H6']     ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emic3h8'     ) : clist=['SFC3H8']     ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emic6h6'     ) : clist=['SFBENZENE']  ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emich3cho'   ) : clist=['SFCH3CHO']   ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emich3coch3' ) : clist=['SFCH3COCH3'] ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emich3cooh'  ) : clist=['SFCH3COOH']  ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emich3oh'    ) : clist=['SFCH3OH']    ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emihcho'     ) : clist=['SFCH2O']     ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emihcooh'    ) : clist=['SFHCOOH']    ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'emimtp'      ) : clist=['SFMTERP']    ; wlist=[1.]  ; vtype='Surface' # monoterpenes

#   dry deposition
    elif ( var == 'drych3coch3'  ) : clist=['DF_CH3COCH3'] ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'drych3cooh'   ) : clist=['DF_CH3COOH']  ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'drych3oh'     ) : clist=['DF_CH3OH']    ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'drychocho'    ) : clist=['DF_GLYOXAL']   ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'dryhcooh'     ) : clist=['DF_HCOOH']    ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'drych4'       ) : clist=['DF_CH4']   ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'dryco'        ) : clist=['DF_CO']    ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'dryh2'        ) : clist=['DF_H2']    ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'dryhcho'      ) : clist=['DF_CH2O']  ; wlist=[1.]  ; vtype='Surface'
    elif ( var == 'drymhp'       ) : clist=['DF_CH3OOH']  ; wlist=[1.]  ; vtype='Surface' # methyl hydroperoxide
    elif ( var == 'drypan'       ) : clist=['DF_PAN']  ; wlist=[1.]  ; vtype='Surface' # methyl hydroperoxide

#   wet deposition
    elif ( var == 'wetch3cho'    ) : clist=['WD_CH3CHO'] ; wlist=[-1.]  ; vtype='Surface'
    elif ( var == 'wetch3coch3'  ) : clist=['WD_CH3COCH3'] ; wlist=[-1.]  ; vtype='Surface'
    elif ( var == 'wetch3oh'     ) : clist=['WD_CH3OH']    ; wlist=[-1.]  ; vtype='Surface'
    elif ( var == 'wethcho'      ) : clist=['WD_CH2O']     ; wlist=[-1.]  ; vtype='Surface'
    elif ( var == 'wethcooh'     ) : clist=['WD_HCOOH']    ; wlist=[-1.]  ; vtype='Surface'
    elif ( var == 'wetmhp'       ) : clist=['WD_CH3OOH']   ; wlist=[-1.]  ; vtype='Surface' # methyl hydroperoxide
    elif ( var == 'wetnh3'       ) : clist=['WD_NH3']      ; wlist=[-1.]  ; vtype='Surface' # methyl hydroperoxide


#   chemical loss rates
    elif ( var == 'ch4losscl' ) : clist = ['r_CL_CH4'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'ch4lossf'  ) : clist = ['r_F_CH4']  ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'ch4lossoh' ) : clist = ['r_CH4_OH'] ; wlist=[1.] ; vtype='ModelLevel'
    elif ( var == 'ch4losso1d') : clist = ['r_O1D_CH4a','r_O1D_CH4b','r_O1D_CH4c'] ; wlist= [1.,1.,1.] ; vtype='ModelLevel'

    elif (var == 'lossch3cho' )   : clist = ['CH3CHO_CHML']; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'lossch3coch3' ) : clist = ['CH3COCH3_CHML']; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'lossch3cooh' )  : clist = ['CH3COOH_CHML']; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'lossch3oh' )  : clist = ['CH3OH_CHML']; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'lossch4' )    : clist = ['CH4_CHML']  ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'losschocho' ) : clist = ['CHOCHO_CHML']  ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'lossco' )   : clist = ['CO_CHML']   ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'lossh2' )   : clist = ['H2_CHML']   ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'lossh2o' )  : clist = ['H2O_CHML']  ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'losshcho' ) : clist = ['CH2O_CHML'] ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'losshcooh' ) : clist = ['HCOOH_CHML'] ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'losshcooh' ) : clist = ['HCOOH_CHML'] ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'losspan' ) : clist = ['PAN_CHML'] ; wlist=[1.] ; vtype='ModelLevel'

#   chemical production rates
    elif (var == 'prodch3coch3' ) : clist = ['CH3COCH3_CHMP'] ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'prodch3cooh' ) : clist = ['CH3COOH_CHMP'] ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'prodch3oh' ) : clist = ['CH3OH_CHMP'] ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'prodco' )    : clist = ['CO_CHMP']    ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'prodh2' )    : clist = ['H2_CHMP']    ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'prodh2o' )   : clist = ['H2O_CHMP']   ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'prodhcho' )  : clist = ['CH2O_CHMP']  ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'prodhcooh' ) : clist = ['HCOOH_CHMP']  ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'prodmhp' )   : clist = ['CH3OOH_CHMP']  ; wlist=[1.] ; vtype='ModelLevel'
    elif (var == 'prodpan' )   : clist = ['PAN_CHMP']  ; wlist=[1.] ; vtype='ModelLevel'

    elif ( var == 'lwp' ) : clist=['TGCLDLWP'] ; wlist=[1.] ; vtype = 'Surface' # should this be 0.001
    elif ( var == 'pfull' ) : clist=['PS'] ; wlist=[1.] ; vtype='ModelLevel' ; action='expand'
    elif ( var == 'phalf' ) : clist=['PS'] ; wlist=[1.] ; vtype='ModelLevel' ; action='expand'
#    elif ( var == 'photo1d' ) :
#    elif ( var == 'pod0' ) :
    elif ( var == 'ps' ) : clist=['PS'] ; wlist=[1.] ; vtype='Surface'
    elif ( var == 'ptp' ) : clist=['TROP_P'] ; wlist=[1.] ; vtype='Surface' # 'Tropopause air pressure [Pa]'
#    elif ( var == 'reffclwtop' ) : # Two options
    elif ( var == 'toz'    ) : clist=['cb_O3'] ; wlist=[1.] ; vtype='Column'                           # total ozone column [m]
    elif ( var == 'tropoz' ) : clist=['O3']    ; wlist=[1.] ; vtype='Column' ; action='columnintegrate' # tropospheric ozone column [m]
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

    elif ( var == 'cod'   ) : clist=['TAUTMODIS'] ; wlist=[1.] ; cnoemer='CLTMODIS' ; vtype='Column'

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
    print('action : ', action)
#
    return clist, wlist, cnoemer, action
