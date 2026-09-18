  function readaerocomascii, origin=origin, activity=activity, sector=sector, species=species
;--------------------------

  print, sector

  case sector of 
    'continuous' : filename='/lustre/storeA/users/dirkjlo/emissions/aerocom/volc/continuous_volc.1x1.ascii'
    'explosive'  : filename='/lustre/storeA/users/dirkjlo/emissions/aerocom/volc/explosive_volc.1x1.ascii'
  endcase

  nmax=300
  lonlist=fltarr(nmax)
  latlist=fltarr(nmax)
  emissionlist=fltarr(nmax)
  height_low=fltarr(nmax)
  height_high=fltarr(nmax)
  topographylist=fltarr(nmax)


  openr, 1, filename

; skip first 3 lines
  line='' & readf,1, line 
  line='' & readf,1, line 
  line='' & readf,1, line 
  
  i=0

  while not eof(1) do begin
 
     line=''
     readf,1, line
     line=strsplit(strcompress(strtrim(line,2)),' ',/extract)

     lonlist(i)         = ( line(0) * 1. +720. ) mod 360.
     latlist(i)         = line(1) * 1.
     emissionlist(i)    = line(2) * 1. * 1.e-9 ; kg/yr -> Tg/yr
     height_low(i)   = line(3) * 1.
     height_high(i) = line(4) * 1.

     i=i+1

  endwhile

  n=i

  close, 1

  data={origin      : origin, $
        activity    : activity, $
        sector      : sector, $
        species     : 'SO2', $ 
        lonlist     : lonlist(0:n-1), $
        latlist     : latlist(0:n-1), $
        emistotlist : emissionlist(0:n-1), $
        height_low  : height_low(0:n-1),$
        height_high : height_high(0:n-1),$
        topographylist:topographylist(0:n-1),$
        n           : n }

  iset=where(data.height_high ne 0.) 
  print, min(data.height_high(iset)), max(data.height_high(iset))
  print, min(data.height_low(iset)), max(data.height_low(iset))

  return, data

  end



  pro testaerocomascii2, origin=origin, activity=activity, sectorlist=sectorlist, species=species
;----------------------
;
  nsector=n_elements(sectorlist)
  for isector=0,nsector-1 do begin
     sector=sectorlist(isector)
     
     data=readaerocomascii(origin=origin, activity=activity, sector=sector, species=species) 
     writeindividualvolcano, data=data 

  endfor
;
  end


  pro testaerocomascii
;---------------------
;
  activity='volc'
;
  dir='/lustre/storeA/users/dirkjlo/emissions/aerocom/volc'
;
; CONTINUOUS
  sectorlist=['continuous','explosive']
  origin='aerocomascii'
  species='SO2'
  testaerocomascii2, origin=origin, activity=activity, sectorlist=sectorlist, species=species
;
  end
