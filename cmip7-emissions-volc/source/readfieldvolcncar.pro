@../../routines/source/readnc
@../../routines/source/areafraction
@../../cmip6-emissions-gfed/source/getmolarweight
@../../cmip6-emissions-gfed/source/press2alt
;
  function readfieldvolcncar, sector=sector, species=species, year=year, month=month, origin=origin
;----------------------------
;
; MODIFICATIONS
;
; AIM 
;
; METHOD
;
; INPUT
;	
; RETURN
;	returns structure containing
;		3D field
;
; REMARK
;	
;
; CALLS 
;	readnc
;
; CALLED BY
;	analysefile
;
;=============================
;
  dircmip5_noresmonly='/lustre/storeB/users/dirkjlo/noresm/inputdata/noresm-only/atm/cam/chem/trop_mozart_aero/emis/ipcc_ar5'
  dircmip5='/lustre/storeB/users/dirkjlo/noresm/inputdata/atm/cam/chem/trop_mozart_aero/emis'
  dircmip6='/lustre/storeB/users/dirkjlo/noresm/inputdata/atm/cam/chem/emis/CMIP6_emissions_1750_2015_240717'
;
  case origin of 
    'ncarcmip5' : begin
        case species of
          'so2'    : filename=dircmip5_noresmonly+'/ar5_mam3_'+species+'_elev_1850-2005_c090804.nc'
          'so4_pr' : filename=dircmip5_noresmonly+'/ar5_mam3_'+species+'_elev_1850-2005_c090804.nc'
          'so4_a1' : filename=dircmip5+'/ar5_mam3_'+species+'_elev_1850-2005_c090804.nc'
          'so4_a2' : filename=dircmip5+'/ar5_mam3_'+species+'_elev_1850-2005_c090804.nc'
        endcase

        varinfile='contvolc'
        levunit='km'
        end
    'ncarcmip6-c20170208': begin 
        filename=dircmip6+'/emissions-cmip6_'+species+'_contvolcano_vertical_1750-2100_0.9x1.25_c170208.nc'
        varinfile='emiss_volcanoes'
        levunit='km'
        end
    'ncarcmip6-c20170322': begin 
        filename=dircmip6+'/emissions-cmip6_'+species+'_contvolcano_vertical_1750-2100_0.9x1.25_c20170322.nc'
        varinfile='emiss_volcanoes'
        levunit='km'
        end
    'ncarcmip6-c20170724': begin ; pressure level based emissions
        filename=dircmip6+'/emissions-cmip6_'+species+'_contvolcano_vertical_850-5000_0.9x1.25_c20170724.nc'
        varinfile='contvolcano'
        levunit='hPa'
        end  
     else : begin
               print, 'No origin recognized = ', origin
               stop
            end
  endcase
;
  print, filename

; 1. read longitude/latitude/levels

  longitude = readnc('lon',filename)
  latitude  = readnc('lat',filename)
  if ( levunit eq 'km' ) then begin
     lev       = readnc('altitude',filename)
     levbnds   = readnc('altitude_int',filename)
  endif else if ( levunit eq 'hPa' ) then begin
     lev       = readnc('lev',filename) ; hPa
     levbnds   = readnc('ilev',filename); hPa
;    convert into km  
     lev = press2alt(lev) $ ; hPa -> m
         / 1000.    ; m -> km    
     levbnds = press2alt(levbnds) $ ; hPa ->m 
             / 1000.    
  endif else begin
     stop
  endelse
 
  nlon = n_elements(longitude)
  nlat = n_elements(latitude)
  nlev = n_elements(lev)

; 2. read griddcellarea
  area = areafraction(longitude=longitude, latitude=latitude, type='area')

; 3. read dates
  datelist = readnc('date',filename) * 1L
  yearlist = datelist / 10000L
  monthlist = ( datelist mod 10000L ) / 100L

  itime = (where(yearlist eq year and monthlist eq month ))(0)

  print, 'itime = ', itime

  field=readnc(varinfile, $
               filename,$
               count  = [ nlon , nlat , nlev , 1     ], $
               offset = [    0 ,    0 ,    0 , itime ] )
;
  Mw = getmolarweight(species=species) ; kg/mole

  field = field   $ ; originally : molecules / cm3 / sec
        * 1.e6    $ ; cm-3 -> m-3
        / 6.022e23$  ; molecules -> mole
        * Mw         ; mole -> kg

  data = {field:field, $
          dim  : '3d', $
          unit : 'kg m-3 s-1',$
          nlon : nlon, $
          nlat : nlat, $ 
          nlev : nlev, $
          longitude : longitude, $
          latitude : latitude, $
          area : area, $
          areaunit : 'm-2', $ 
          levbnds : levbnds *1000., $ ; km -> m
          lev     : lev*1000., $      ; km -> m
          levunit : 'm', $
          year : year, $
          month: month }
;
  return, data
;
  end
