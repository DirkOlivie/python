@../../routines/source/readnc
@../../routines/source/areafraction
@../../cmip6-emissions-gfed/source/getmolarweight
@../../routines/source/lon2lonbnds
@../../routines/source/lat2latbnds
@../../routines/source/lev2levbnds
@../../routines/source/intplon
@../../routines/source/intplat
@../../cmip6-emissions-gfed/source/camlevels
@../../cmip6-emissions-gfed/source/press2alt
;
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
    'continuous' : filename0=dir+'/contineous_volc.nc'       
    'explosive'  : filename0=dir+'/explosive_volc.nc'
  endcase
;
  print, filename0

; 1. read longitude/latitude/levels
  longitude0 = readnc('lon',filename0)
  latitude0  = readnc('lat',filename0)
  gridbox_area = readnc('gridbox_area', filename0)

  nlon0 = n_elements(longitude)
  nlat0 = n_elements(latitude)

  lonbnds0=lon2lonbnds(longitude=longitude0)
  latbnds0=lat2latbnds(latitude=latitude0)
;
; 2. read griddcellarea
  area0 = areafraction(longitude=longitude0, latitude=latitude0, type='area')

; 3. read data
  field          = readnc('field', filename0) ; kg/yr/gridbox
  
  field = field            $ ; kg/yr
        / 365.25           $ ; kg/yr -> kg/day  
        / 86400.           $ ; kg/day -> kg/sec
        / area0               ; 1/gridbox -> 1/m2

;  print, total(field*area0)*86400*365.25*1.e-9
;  stop

  height_low     = readnc('height_low', filename0)
  height_high    = readnc('height_high', filename0)
  volcano_height = readnc('volcano_heigth', filename0)
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
  case origin of 
    'aerocomnetcdf'         : filename1 = filename0
    'aerocomnetcdf0.9x1.25' : filename1 = '/lustre/storeA/users/dirkjlo/noresm/cases/SOA_r610_PD/atm/hist/SOA_r610_PD.cam.h0.1979-01.nc'
    'aerocomnetcdf1.9x2.5'  : filename1 = '/lustre/storeA/users/dirkjlo/noresm/cases/Test147f19_f19/atm/hist/Test147f19_f19.cam.h0.0001-01.nc'
  endcase     

  topo=readtopography(origin=origin)

  longitude1=readnc('lon', filename1)
  latitude1=readnc('lat',filename1)

  nlon1=n_elements(longitude1)
  nlat1=n_elements(latitude1)
 
  latbnds1=lat2latbnds(latitude=latitude1)
  lonbnds1=lon2lonbnds(longitude=longitude1)
;
  newfield=fltarr(nlon1,nlat1,nlev)
;
  intplon,loninbd=lonbnds0, lonoutbd=lonbnds1, conv=convlon,wt=wtlon,pt=ptlon
  intplat,latinbd=latbnds0, latoutbd=latbnds1, conv=convlat,wt=wtlat,pt=ptlat


  for ilon1=0,nlon1-1 do begin
     nlon=ptlon(ilon1,0) ; how many neigbours used for this point    
     for ilat1=0,nlat1-1 do begin
        nlat=ptlat(ilat1,0) ; how many neighbours used for this point           
        for ilon=1,nlon do begin
           ilon0=ptlon(ilon1,ilon)
           wlon=wtlon(ilon1,ilon)
           for ilat=1,nlat do begin
              ilat0=ptlat(ilat1,ilat)
              wlat=wtlat(ilat1,ilat)

              if (field(ilon0,ilat0) ne 0. ) then begin

;                ilon1, ilat1 grid box shoulbe increased with infield(ilon0,ilat0) *wlon*wlat ; kg/m2/s 
;                this amount should be vertically distributed 

                 dh = height_high(ilon0,ilat0) - height_low(ilon0,ilat0) 
 
                 if ( dh gt 0. ) then begin
             
                    for ilev=0,nlev-1 do begin

;                      original data set
                       minx=height_low( ilon0,ilat0)
                       maxx=height_high(ilon0,ilat0)

;                      final data set
                       miny=min([levbnds(ilev),levbnds(ilev+1)])+topo(ilon1,ilat1)
                       maxy=max([levbnds(ilev),levbnds(ilev+1)])+topo(ilon1,ilat1)             

                       low= max([minx,miny])  
                       hgh= min([maxx,maxy])

                       overlap = hgh - low

                       if ( overlap gt 0. ) then begin

                          newfield(ilon1,ilat1,ilev) = newfield(ilon1,ilat1,ilev) $
                                                     + overlap / abs(levbnds(ilev+1)-levbnds(ilev)) $
                                                     * field(ilon0,ilat0) / dh * wlon * wlat                       

                          
                          print, 'overlap = ', ilon1, ilat1, ilon0, ilat0, ilev, dh, overlap, newfield(ilon1,ilat1,ilev)
                    
                       endif
                    endfor
;
;                   below the orography -> put in lowest layer
                    minx=min([height_low( ilon,ilat),topo(ilon1,ilat1)])
                    miny=min([height_high(ilon,ilat),topo(ilon1,ilat1)])  

                    if (miny gt minx ) then begin
;                 
; CAREFULL : is lowest layer 0?
                       newfield(ilon1,ilat1,0) = newfield(ilon1,ilat1,0) $
                                               + (miny-minx) / abs(levbnds(0)-levbnds(1)) $
                                               * field(ilon0,ilat0) /dh * wlon*wlat
;                           
                    endif

                 endif else begin

                    print, 'volcano without vertical extend ...'
                    print, 'at LON = ', longitude0(ilon)
                    print, 'at LAT = ', latitude0(ilat)
                    print, 'put all in lowest layer'
                    newfield(ilon1,ilat1,0) = newfield(ilon1,ilat1,0) $
                                            + field(ilon0,ilat0) / abs(levbnds(0)-levbnds(1)) $
                                            * wlon*wlat


;                   stop

                 endelse
            
              endif
 
           endfor

        endfor

     endfor

  endfor

  area1 = areafraction(longitude=longitude1, latitude=latitude1, type='area')

  if ( origin eq 'aerocomnetcdf' ) then begin
;
     data = {field:newfield, $
             height_low     : height_low,$
             height_high    : height_high,$
             volcano_height : volcano_height,$
             dim  : '3d', $
             unit : 'kg m-3 s-1',$
             nlon : nlon1, $
             nlat : nlat1, $ 
             nlev : nlev, $
             longitude : longitude1, $
             latitude : latitude1, $
             area : area1, $
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
     
     data = {field:newfield, $
             dim  : '3d', $
             unit : 'kg m-3 s-1',$
             nlon : nlon1, $
             nlat : nlat1, $ 
             nlev : nlev, $
             longitude : longitude1, $
             latitude : latitude1, $
             area : area1, $
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
