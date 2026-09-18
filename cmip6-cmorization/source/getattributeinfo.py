import getattributeinfo_online
import getattributeinfo_offline

def getattributeinfo(var,realm) :
#-------------------
    '''
    INPUT
        var
        realm

    CALLS
        getattributeinfo_online
        getattributeinfo_offline

    '''

#
#   attributes for variable
    if ( var == 'aodvisvolso4' \
      \
      or var == 'ch3cooh' \
      or var == 'ch3oh' \
      or var == 'ch3cho' \
      or var == 'c2h4' \
      or var == 'c6h6' \
      or var == 'hcooh' \
      or var == 'h2' \
      or var == 'ho2' \
      or var == 'mhp' \
      or var == 'mtp' \
      or var == 'o1d' \
      or var == 'o3surface' \
      or var == 'nh3' \
      or var == 'no3' \
      or var == 'toluene' \

      or var == 'siconc'    \
      or var == 'ch4losscl' \
      or var == 'ch4lossf'  \
      or var == 'ch4lossoh' \
      or var == 'ch4losso1d' \
      \
      or var == 'drych3coch3' \
      or var == 'drych3cooh' \
      or var == 'drych3oh' \
      or var == 'drychocho' \
      or var == 'dryhcooh' \
      or var == 'drych4' \
      or var == 'dryco' \
      or var == 'dryhcho' \
      or var == 'dryh2' \
      or var == 'drymhp' \
      or var == 'drypan' \
      \
      or var == 'emic2h2' \
      or var == 'emic2h4' \
      or var == 'emic2h6' \
      or var == 'emic3h6' \
      or var == 'emic3h8' \
      or var == 'emic6h6' \
      or var == 'emich3cho' \
      or var == 'emich3coch3' \
      or var == 'emich3cooh' \
      or var == 'emich3oh' \
      or var == 'emihcho' \
      or var == 'emihcooh' \
      or var == 'emih2' \
      or var == 'emimtp' \
      \
      or var == 'lossch3cho' \
      or var == 'lossch3coch3' \
      or var == 'lossch3cooh' \
      or var == 'lossch3oh' \
      or var == 'losschocho' \
      or var == 'losshcho' \
      or var == 'losshcooh' \
      or var == 'lossh2' \
      or var == 'lossh2o' \
      or var == 'lossisop' \
      or var == 'losspan' \
      \
      or var == 'prodch3coch3' \
      or var == 'prodch3cooh' \
      or var == 'prodch3oh' \
      or var == 'prodchocho' \
      or var == 'prodco' \
      or var == 'prodh2' \
      or var == 'prodh2o' \
      or var == 'prodhcho' \
      or var == 'prodhcooh' \
      or var == 'prodmhp' \
      or var == 'prodpan' \
      \
      or var == 'volume' \
      \
      or var == 'wetch3cho' \
      or var == 'wetch3coch3' \
      or var == 'wetch3oh' \
      or var == 'wethcho' \
      or var == 'wethcooh' \
      or var == 'wetmhp' \
      \
      or ( var == 'o3' and realm == 'AERZmon' ) ) :
        attributeinfo=getattributeinfo_offline.getattributeinfo_offline(var=var)
    else :
        attributeinfo=getattributeinfo_online.getattributeinfo_online(var=var, realm=realm)

    return attributeinfo
