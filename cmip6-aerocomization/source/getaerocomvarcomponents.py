import sys

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import stool

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

def getaerocomvarcomponents(var, expid):
#---------------------------------------
    '''
    INPUT PARAMETERS
        var
        expid

    RETURN
        structure containing

    '''
    
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    chem=expidinfo['chem']
#
    cnoemer = None
    action = None
    desiredunits = None

#   airmass
    if (   var == 'vmro3' and chem == 'fullchem' ) : clist=['O3_SRF']          ; wlist=[1.] ; vtype='Surface'                                     ; long_name='Ozone mixing ratio'              ; desiredunits='ppb'
    elif ( var == 'vmro3' and chem == ''         ) : clist=['O3_surfacelayer'] ; wlist=[1.] ; vtype='Surface'                                     ; long_name='Ozone mixing ratio'              ; desiredunits='ppb'
    elif ( var == 'vmrco'                        ) : clist=['CO_SRF']      ; wlist=[1.] ; vtype='Surface'                                     ; long_name='Carbonmonoxide mixing ratio'     ; desiredunits='ppb'
    elif ( var == 'vmrno'                        ) : clist=['NO_SRF']      ; wlist=[1.] ; vtype='Surface'                                     ; long_name='Nitrogen oxide'                  ; desiredunits='ppt'
    elif ( var == 'vmrno2'                       ) : clist=['NO2_SRF']     ; wlist=[1.] ; vtype='Surface'                                     ; long_name='Nitrogen dioxide'                ; desiredunits='ppt'
    elif ( var == 'vmrso2'                       ) : clist=['SO2_SRF']     ; wlist=[1.] ; vtype='Surface'                                     ; long_name='Sulfur dioxide'                  ; desiredunits='nmol mol-1' # 'mole mole-1', 'mol mol-1' DOES NOT WORK
    elif ( var == 'od550aer'                     ) : clist=['DOD550']      ; wlist=[1.] ; vtype='Column'                                      ; long_name='Aerosol optical depth at 550 nm' ; desiredunits='1'
#
    elif ( var == 'concbc'                       ) : clist=['mmr_BC_as_concentration_surfacelayer']      ; wlist= [1.] ; vtype='Surface'  ; long_name='Black carbon concentration'          ; desiredunits='ug m-3'
    elif ( var == 'concoa'                       ) : clist=['mmr_OM_as_concentration_surfacelayer']      ; wlist= [1.] ; vtype='Surface'  ; long_name='Organic aerosol concentration'       ; desiredunits='ug m-3'
    elif ( var == 'concso4'                      ) : clist=['mmr_SULFATE_as_concentration_surfacelayer'] ; wlist= [1.] ; vtype='Surface'  ; long_name='Sulfate concentration'               ; desiredunits='ug m-3'
    elif ( var == 'concss'                       ) : clist=['mmr_SALT_as_concentration_surfacelayer']    ; wlist= [1.] ; vtype='Surface'  ; long_name='Sea-salt concentration'              ; desiredunits='ug m-3'
#
    elif ( var == 'emidms'                       ) : clist=['SFDMS']       ; wlist=[1.] ; vtype='Surface'                                      ; long_name='DMS emissions'   ; desiredunits='kg m-2 s-1'
    elif ( var == 'emichbr3'                     ) : clist=['SFCHBR3']     ; wlist=[1.] ; vtype='Surface'                                      ; long_name='CHBr3 emissions' ; desiredunits='kg m-2 s-1'
    elif ( var == 'sfcWind'                      ) : clist=['U10']         ; wlist=[1.] ; vtype='Surface'                                      ; long_name = "Near-Surface Wind Speed" ; desiredunits = "m s-1"

    else : 
        print('++++ getaerocomvarcomponents +++')
        print('No var recognized : ',var)
        quit()
#
#   check equal length of arrays
    if ( len(clist) != len(wlist) ) :
        print('++++ getaerocomvarcomponents +++')
        print('clist and wlist have different length :', len(clist), len(wlist))
        quit()
#
    print('+++ getaerocomvarcomponents +++')
    print('clist : ', clist)
    print('wlist : ', wlist)
    print('cnoemer : ', cnoemer)
    print('action : ', action)
#
    data = { 'clist'        : clist, \
             'wlist'        : wlist, \
             'cnoemer'      : cnoemer, \
             'vtype'        : vtype, \
             'action'       : action, \
             'long_name'    : long_name, \
             'desiredunits' : desiredunits}
#
    return data
