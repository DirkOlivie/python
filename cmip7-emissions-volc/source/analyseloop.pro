   
  pro analyseloop2, activity=activity, sectorlist=sectorlist, specieslist=specieslist, yearlist=yearlist, origin=origin
;-----------------
;
; AIM 
;	calls analysefile for every individual file
;
; INPUT 
;	directory : directory of files (all files have to be in the same directory)
;
; CALLS
;	analysefile
;
; CALLED BY
;	analyseloop
;
  nsector=n_elements(sectorlist)
  nspecies=n_elements(specieslist)

  for isector=0,nsector-1 do begin
  for ispecies=0,nspecies-1 do begin
     sector=sectorlist(isector)
     species=specieslist(ispecies)

     analysefile, activity=activity, sector=sector, species=species, yearlist=yearlist, origin=origin

  endfor
  endfor

  end

  pro analyseloop
;----------------------
; 
; CALLS 
;	analysefilelist
;
; 
  activity='volc'
;
; I. pure AEROCOM
; I.1 ascii file

; I.2 netcdffile
  origin='aerocomnetcdf'
  sectorlist=['continuous','explosive']
  specieslist=['SO2']
  yearlist=[9999]
  analyseloop2, activity=activity, sectorlist=sectorlist, specieslist=specieslist,yearlist=yearlist, origin=origin
;
  origin='aerocomnetcdf1.9x2.5'
  sectorlist=['continuous','explosive','continuousexplosive']
  specieslist=['SO2']
  yearlist=[9999]
  analyseloop2, activity=activity, sectorlist=sectorlist, specieslist=specieslist,yearlist=yearlist, origin=origin
;
  origin='aerocomnetcdf0.9x1.25'
  sectorlist=['continuous','explosive','continuousexplosive']
  specieslist=['SO2']
  yearlist=[9999]
  analyseloop2, activity=activity, sectorlist=sectorlist, specieslist=specieslist,yearlist=yearlist, origin=origin
;
  stop
;
; II. NorESM1 - ascii
  origin='noresm1aerocomascii'
  sectorlist=['ALL']
  specieslist=['so2']
  yearlist=[9999]

  analyseloop2, activity=activity, sectorlist=sectorlist, specieslist=specieslist,yearlist=yearlist, origin=origin
;
; III. CMIP5 NCAR DATA
; cmip5ncar
  origin='ncarcmip5'
  sectorlist=['cont']
  specieslist=['so2'];,'so4_pr','so4_a1','so4_a2']
  yearlist=[1849];,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2006]

;  analyseloop2, activity=activity, sectorlist=sectorlist, specieslist=specieslist,yearlist=yearlist, origin=origin
;
  stop

; IV. CMIP6 NCAR DATA
; version 20170208
  origin = 'ncarcmip6-c20170208'
  sectorlist=['cont']
  specieslist=['SO2'];,'so4_a1','so4_a2']
  yearlist=[1750];,1850,2000,2015,2100]

  analyseloop2, activity=activity, sectorlist=sectorlist, specieslist=specieslist,yearlist=yearlist, origin=origin

; version 20170322  
  origin = 'ncarcmip6-c20170322'
  sectorlist=['cont']
  specieslist=['SO2'];,'so4_a1','so4_a2']
  yearlist=[1750];,1850,2000,2010,2015,2100] ; has one decade extra

  analyseloop2, activity=activity, sectorlist=sectorlist, specieslist=specieslist,yearlist=yearlist, origin=origin  
;
; version 20170724
  origin = 'ncarcmip6-c20170724'
  sectorlist=['cont']
  specieslist=['SO2'];,'so4_a1','so4_a2']
  yearlist=[850];,1850,1960,2000,2005,2010,5000] ; has one decade extra

  analyseloop2, activity=activity, sectorlist=sectorlist, specieslist=specieslist,yearlist=yearlist, origin=origin
;
  end
;
