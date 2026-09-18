@../../routines/source/readnc
@../../routines/source/areafraction
@../../cmip6-emissions-gfed/source/getmolarweight
@../../routines/source/lon2lonbnds
@../../routines/source/lat2latbnds
@../../routines/source/lev2levbnds
@../../routines/source/intpfield
@../../cmip6-emissions-gfed/source/camlevels
@../../cmip6-emissions-gfed/source/press2alt
;
  function readfieldvolcaerocomnetcdfsingle, sector=sector, species=species, year=year, month=month, origin=origin
;------------------------------------------
;
; MODIFICATIONS
;	(2018-03-20) : extended to also be able to generate fields at different resolutions
;				1x1 (original, as input is on this resolution)
;				1.9x2.5
;				0.9x1.25
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
;	returns also original
;		2D fields : height_low, height_high, volcano_height
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
  if ( species ne 'SO2' ) then stop

  dir='/lustre/storeA/users/dirkjlo/emissions/aerocom/volc'
;
  case sector of 
    'continuous' : filename=dir+'/contineous_volc.nc'       
    'explosive'  : filename=dir+'/explosive_volc.nc'
  endcase
;
  print, filename

; 1. read longitude/latitude/levels

  longitude = readnc('lon',filename)
  latitude  = readnc('lat',filename)
  gridbox_area = readnc('gridbox_area', filename)

  nlon = n_elements(longitude)
  nlat = n_elements(latitude)

; 2. read griddcellarea
  area = areafraction(longitude=longitude, latitude=latitude, type='area')

; 3. read data
  field          = readnc('field', filename) ; kg/yr/gridbox
  height_low     = readnc('height_low', filename)
  height_high    = readnc('height_high', filename)
  volcano_height = readnc('volcano_heigth', filename)
;
; 4. create vertical field
; 4.1 standard option
;  nlev=20
;  levbnds = indgen(nlev+1) * 500. ; 500 m thick layers
;  lev     = indgen(nlev  ) * 500. + 250.
;
; 4.2 use standard noresm 26 grid
; down means : pressure decreases (so it means : start at Earth's surface)
  nlev=20
  press    = camlevels(updown='down', type='midlevels')  ; uses ps=p0=100000 Pa
  pressbnd = camlevels(updown='down', type='boundaries') ; uses ps=p0=100000 Pa
;
; select only levels one needs
  press    = press(0:nlev-1)
  pressbnd = pressbnd(0:nlev)
;
  levbnds = press2alt(pressbnd / 100.) ; hPa
  levbnds = levbnds - min(levbnds) ; make sure that starts at 0m above sea-level

  lev = 0.5 * ( levbnds(0:nlev-1) + levbnds(1:nlev) )
  nlev=n_elements(lev)

;
; 5. interpolate to new grid

  newfield=fltarr(nlon,nlat,nlev)
  for ilon=0,nlon-1 do begin
     for ilat=0,nlat-1 do begin

        if ( field(ilon,ilat) ne 0. ) then begin ; only where emissions are different from zero

           dh = height_high(ilon,ilat) - height_low(ilon,ilat) 

           print, longitude(ilon), latitude(ilat), height_low(ilon,ilat), height_high(ilon,ilat), volcano_height(ilon,ilat), field(ilon,ilat)

           if ( dh gt 0. ) then begin
             
              emission = field(ilon,ilat) $ ; kg/yr
                       / 365.25           $ ; kg/yr -> kg/day  
                       / 86400.           $ ; kg/day -> kg/sec
                       / area(ilon,ilat)  $ ; 1/gridbox -> 1/m2
                       / dh                ; kg/m3/s

              for ilev=0,nlev-1 do begin

;                 print,  height_low(ilon,ilat), height_high(ilon,ilat), levbnds(ilev),levbnds(ilev+1)

                 minx=height_low(ilon,ilat)
                 maxx=height_high(ilon,ilat)

                 miny=min([levbnds(ilev),levbnds(ilev+1)])
                 maxy=max([levbnds(ilev),levbnds(ilev+1)])             

                 low= max([minx,miny])  
                 hgh= min([maxx,maxy])

                 overlap = hgh - low

;                 print, 'ilev, overlap = ', ilev, overlap

                 if ( overlap gt 0. ) then begin

                    newfield(ilon,ilat,ilev) = newfield(ilon,ilat,ilev) $
                                             + overlap / abs(levbnds(ilev+1)-levbnds(ilev)) * emission 
                    
                 endif

              endfor

           endif else begin

              print, 'volcano without vertical extend ...'
              print, 'at LON = ', longitude(ilon)
              print, 'at LAT = ', latitude(ilat)
;             stop

           endelse

        endif 

     endfor

  endfor


  if ( origin eq 'aerocomnetcdf' ) then begin
;
     data = {field:newfield, $
             height_low     : height_low,$
             height_high    : height_high,$
             volcano_height : volcano_height,$
             dim  : '3d', $
             unit : 'kg m-3 s-1',$
             nlon : nlon, $
             nlat : nlat, $ 
             nlev : nlev, $
             longitude : longitude, $
             latitude : latitude, $
             area : area, $
             areaunit : 'm-2', $ 
             levbnds : levbnds, $ ; m
             lev     : lev, $     ; m
             levunit : 'm', $
             year : year, $
             month: month }
;
  endif else if ( origin eq 'aerocomnetcdf1.9x2.5' $
               or origin eq 'aerocomnetcdf0.9x1.25' ) then begin
;
; find somewhere latitudes and longitudes    
    
     case origin of
       'aerocomnetcdf1.9x2.5'  : filename='/lustre/storeA/users/dirkjlo/noresm/cases/Test147f19_f19/atm/hist/Test147f19_f19.cam.h0.0001-01.nc'
       'aerocomnetcdf0.9x1.25' : filename='/lustre/storeA/users/dirkjlo/noresm/cases/SOA_r610_PD/atm/hist/SOA_r610_PD.cam.h0.1979-01.nc'
     endcase

     longitude2 = readnc('lon',filename)
     latitude2  = readnc('lat',filename)

     nlon2=n_elements(longitude2)
     nlat2=n_elements(latitude2)

     area2 = areafraction(longitude=longitude2, latitude=latitude2, type='area')
;
;    original boundaries
     lonbnds=lon2lonbnds(longitude=longitude)
     latbnds=lat2latbnds(latitude=latitude)
     
;    final boundaries
     lonbnds2=lon2lonbnds(longitude=longitude2)
     latbnds2=lat2latbnds(latitude=latitude2)
;    
;    interpolation
     intpfield, infield=newfield, outfield=outfield, latinbd=latbnds, latoutbd=latbnds2, loninbd=lonbnds, lonoutbd=lonbnds2, levinbd=levbnds, levoutbd=levbnds

     print, min(newfield), max(newfield)
     print, min(outfield), max(outfield)

;     stop
    
     data = {field:outfield, $
             dim  : '3d', $
             unit : 'kg m-3 s-1',$
             nlon : nlon2, $
             nlat : nlat2, $ 
             nlev : nlev, $
             longitude : longitude2, $
             latitude : latitude2, $
             area : area2, $
             areaunit : 'm-2', $ 
             levbnds : levbnds, $ ; m
             lev     : lev, $     ; m
             levunit : 'm', $
             year : year, $
             month: month }
;
  endif else begin
     stop
  endelse

  return, data
;
  end


  function readfieldvolcaerocomnetcdf, sector=sector, species=species, year=year, month=month, origin=origin
;------------------------------------
;  
  if ( sector eq 'continuous' or sector eq 'explosive' ) then begin
 
     data = readfieldvolcaerocomnetcdfsingle(sector=sector, species=species, year=year, month=month, origin=origin)

  endif else if ( sector eq 'continuousexplosive' ) then begin

     D0=readfieldvolcaerocomnetcdfsingle(sector='continuous', species=species, year=year, month=month, origin=origin)
     D1=readfieldvolcaerocomnetcdfsingle(sector='explosive' , species=species, year=year, month=month, origin=origin)
     
     data = {field: D0.field+D1.field, $
             dim  : D0.dim, $
             unit : D0.unit,$
             nlon : D0.nlon, $
             nlat : D0.nlat, $ 
             nlev : D0.nlev, $
             longitude : D0.longitude, $
             latitude : D0.latitude, $
             area : D0.area, $
             areaunit : D0.areaunit, $ 
             levbnds : D0.levbnds, $ ; m
             lev     : D0.lev, $     ; m
             levunit : D0.levunit, $
             year : D0.year, $
             month: D0.month }

  endif else begin

     stop

  endelse

  return, data 

  end
