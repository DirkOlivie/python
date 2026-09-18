  function readfield, activity=activity, sector=sector, species=species, year=year, month=month, origin=origin
;-------------------
;
;
  if ( activity ne 'volc' ) then stop  

  case origin of
;
; aerocom
;    'aerocomascii'  : data = readfieldaerocomascii(activity=activity, species=species, origin=origin)
    'aerocomnetcdf'         : data = readfieldvolcaerocomnetcdf(sector=sector, species=species, year=year, month=month, origin=origin)
    'aerocomnetcdf1.9x2.5'  : data = readfieldvolcaerocomnetcdf(sector=sector, species=species, year=year, month=month, origin=origin)
    'aerocomnetcdf0.9x1.25' : data = readfieldvolcaerocomnetcdf(sector=sector, species=species, year=year, month=month, origin=origin)
;
; noresm1
    'noresm1aerocomascii'  : data = readfieldvolcnoresm1ascii(activity=activity,species=species, origin=origin)
;
; ncar
    'ncarcmip5'           : data = readfieldvolcncar(sector=sector, species=species, year=year, month=month, origin=origin)
    'ncarcmip6-c20170208' : data = readfieldvolcncar(sector=sector, species=species, year=year, month=month, origin=origin)
    'ncarcmip6-c20170322' : data = readfieldvolcncar(sector=sector, species=species, year=year, month=month, origin=origin)
    'ncarcmip6-c20170724' : data = readfieldvolcncar(sector=sector, species=species, year=year, month=month, origin=origin)
     else : begin 
               print, 'Origin not recognized = ', origin  
               stop
            end
  endcase

  return, data

  end
