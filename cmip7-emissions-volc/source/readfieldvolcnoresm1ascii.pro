;
@../../cmip6-emissions-gfed/source/camlevels
@../../cmip6-emissions-gfed/source/press2alt
@../../routines/source/areafraction
;
; CONTAINS
;
  function readfieldvolcnoresm1ascii, origin=origin, activity=activity, species=species
;-----------------------------------
;
; AIM : reads 4-dimesional data from ascii file
;
; CALLED BY :
;
; CALLS :
; 	
; CAREFULL about units : some are in kg[SO2] other in kg[S]
;
; FV09
; 1850.soxbb.FV09.asciiflat:IPCC 2000 SOX biomass emissions     kg SO2 m-2 /s
; 1850.soxff.FV09.asciiflat:IPCC 2000 SOX fossil fuel emissions kg SO2 m-2 /s
; 2000.soxbb.FV09.asciiflat:IPCC 2000 SOX biomass emissions     kg SO2 m-2 /s
; 2000.soxff.FV09.asciiflat:IPCC 2000 SOX fossil fuel emissions kg SO2 m-2 /s
;
; FV19
; 1850.soxbb.FV19.asciiflat:IPCC 2000 SOX biomass emissions      kg SO2 m-2 /s
; 1850.soxbb_ver2.FV19.asciiflat:IPCC 2000 SOX biomass emissions kg SO2 m-2 /s
; 1850.soxff.FV19.asciiflat:IPCC 2000 SOX fossil fuel emissions  kg SO2 m-2 /s
; 2000.soxbb.FV19.asciiflat:IPCC 2000 SOX biomass emissions      kg SO2 m-2 /s
; 2000.soxbb_ver2.FV19.asciiflat:IPCC 2000 SOX biomass emissions kg SO2 m-2 /s                                   
; 2000.soxff.FV19.asciiflat:IPCC 2000 SOX fossil fuel emissions  kg SO2 m-2 /s
                               
; aerocom.soxbb.FV19.asciiflat:Aerocom B SOX biomass burning emissions kg S m-2 /s
; aerocom.soxvolc.FV19.asciiflat:Aerocom B SOX volcanic emissions      kg S m-2 /s                                    
; preind.soxbb.FV19.asciiflat:Aerocom B SOX biomass burning emissions  kg S m-2 /s
; preind.soxff.FV19.asciiflat:Aerocom B SOX fossil fuel emissions      kg S m-2 /s
;
;
; 0. FILENAME
;------------
  dir='/lustre/storeB/users/dirkjlo/noresm/inputdata/atm/cam/camoslo/emissions'

  nlev=9
  filename = dir+'/aerocom.soxvolc.FV19.asciiflat'
;
  nlon=144
  nlat=96

  nmonth=1

  print, filename

; I. READ DATA FROM FILE
;-----------------------
; read all 12 months on the file
  data=fltarr(nlon,nlat,nlev,nmonth)  
  openr,1,filename
;
; LOOP over months
  for imonth=0,nmonth-1 do begin
;
; 1. READ INFO LINES
; first line : number of dimension
     version=0
     readf,1, version
;
; second line : size of dimensions
     readf,1, itot, jtot, ktot, ntextlines, $
                ixcordinfo, iycordinfo, izcordinfo

; third line : longitudes : shift + resolution
     if ( ixcordinfo eq 1 ) then begin
        longinfo=fltarr(2)
        readf,1, longinfo
     endif
;
; fourth line : latitudes : shift + resolution
     if ( iycordinfo eq 1 ) then begin
        latinfo=fltarr(2)
        readf, 1, latinfo
     endif
;
; fifth line : levels : shift + resolution
     if ( izcordinfo eq 1 ) then begin
        levinfo=fltarr(2)
        readf, 1, levinfo
     endif
;
; fifth line : some general information
     for iline=0,ntextlines-1 do begin
        line=''
        readf, 1, line
     endfor

     print, line
;     stop
    
; 2. CONVERSION FACTOR : we want [SO2] (so possibly conversion of [S] to [SO2])
;
     factor=1.  
     npos=strpos(line,'kg S m-2')
     if ( npos ne -1 ) then factor=2
;
     npos=strpos(filename,'pomsoa')
     if ( npos ne -1 ) then factor=1.96        
;
; 3. READING THE ACTUAL DATA
     i=0
     itot=0L
;     for ilev=nlev-1,0,-1 do begin
     for ilev=0,nlev-1 do begin
     for ilat=0,nlat-1 do begin
     for ilon=0,nlon-1 do begin
        if ( i eq 0 ) then begin
;           lineline=''
;           readf, 1, lineline
;           print, 'lineline = ', lineline
;           stop
;           lineline=strsplit(strtrim(strcompress(lineline),2),' ',/extract)
;           if (n_elements(lineline) ne 8 ) then stop 
;           a=lineline*1.
            a=dblarr(8)          
            readf,1, a, format='(8e14.6)'
;           print, 'values = ', a
           itot=itot+1L
        endif
;        print, i, itot, imonth, ilev, ilat, ilon
        data(ilon,ilat,ilev,imonth)=a(i)*factor
        i = (i+1) mod 8
     endfor
     endfor
     endfor
;
  endfor ; loop over nomth
;
  close,1
;
; III. SELECT CORRECT MONTH
;--------------------------
  month=1
  year=9999
  data= data(*,*,*,month-1)

; IV. convert to intensive units
;-------------------------------
; down means : pressure decreases (so it means : start at Earth's surface)
  press    = camlevels(updown='down', type='midlevels')
  pressbnd = camlevels(updown='down', type='boundaries')
;
; select only levels one needs
  press    = press(0:nlev-1)
  pressbnd = pressbnd(0:nlev) 
;
  levbnds = press2alt(pressbnd / 100.) ; hPa
  levbnds = levbnds - min(levbnds) ; make sure that starts at 0m above sea-level

  lev = 0.5 * ( levbnds(0:nlev-1) + levbnds(1:nlev) )
 
;  print, 'noresmascii = ', levbnds
;  stop

; conversion to kg/m3/s
  for ilev=0,nlev-1 do begin
     dz = abs(levbnds(ilev) - levbnds(ilev+1)) ; m
     data(*,*,ilev)=data(*,*,ilev)/dz
  endfor

; V. longitude - latitude - area
;-------------------------------
; get longitud -latitude from some standard file
  if ( nlon eq 144 and nlat eq 96 ) then begin
     filename='/lustre/storeA/users/dirkjlo/noresm/cases/Test147f19_f19/atm/hist/Test147f19_f19.cam.h0.0001-01.nc'
  endif else if ( nlon eq 288 and nlat eq 192 ) then begin
     filename='/lustre/storeA/users/dirkjlo/noresm/cases/SOA_r610_PD/atm/hist/SOA_r610_PD.cam.h0.1979-01.nc'
  endif else begin
     stop
  endelse

  longitude = readnc('lon', filename)
  latitude = readnc('lat', filename)

  if ( n_elements(longitude) ne nlon ) then begin 
     print, nlon, n_elements(longitude)
     stop
  endif else if ( n_elements(latitude) ne nlat ) then begin
     print, nlat, n_elements(latitude)
     stop
  endif 


  area = areafraction(longitude=longitude, latitude=latitude, type='area')

; VI. FINAL DATA STRUCTURE
;-------------------------
  data = {field:data, $
          dim  : '3d', $
          unit : 'kg m-3 s-1', $
          nlon : nlon, $
          nlat : nlat, $
          nlev : nlev, $
          longitude : longitude, $
          latitude : latitude, $
          area : area, $
          areaunit : 'm-2',$
          levbnds : levbnds,$
          lev  : lev, $
          levunit : 'm', $
          year : year, $
          month : month $
          } 
;
  return, data

  end
