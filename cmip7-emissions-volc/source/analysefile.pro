@../../cmip6-emissions-ncar/source/convertdatetoyearseries
;
;
; CONTAINS
;
; MODIFICATIONS
;	(2014-04-18) converted from UiO to met.no
;	
; 
  pro analysefile, sector=sector, activity=activity, species=species, yearlist=yearlist, origin=origin
;----------------
;
; MODIFICATIONS
;
; AIM 
;	writing ascii file with annual totals, for different sectors if multiple in the file
;	writing ascii file with global mean profile (averaged over all years)
;
; METHOD
;	every variable (from the original file) goes through modifyvalue before it is written to the new file	
;
; REMARK
;
; CALLS 
;	constructseries
;       convertdatatoyearseries 	
;
; CALLED BY
;	analysefilelist
;
;=============================
;
; 1. read 3D/4D data
;-------------------
;
  data = constructseries(sector=sector, activity=activity, species=species, yearlist=yearlist, origin=origin)
;
; 2. reduce to annual values
;===========================
;
  D = convertdatetoyearseries(D=data)
;
; 3. write global totals
;======================= 
;
; 3.1 global totals (2D and 3D fields)
  openw, 1, '../info/globaltotal_'+origin+'_'+activity+'_'+sector+'_'+species+'.txt'

  printf, 1, 'YEAR', D(*).name, 'total', format='(a4,10(x,a15))'
  for iyear=0,D(0).ntime-1 do begin
     printf, 1, D(0).timelist(iyear), D(*).valuelist(iyear), total(D(*).valuelist(iyear)), format='(i4,10(x,e15.3))'
  endfor

  close, 1

; 3.2 global profiles (3D fields)
  if ( D(0).doaltitude eq 1 ) then begin

     openw, 1, '../info/profile_'+filename+'.txt'
  
     n3=n_elements(D)
     ntime=D(0).ntime
     naltitude=D(0).naltitude 

     meanprofile=fltarr(n3,naltitude)
     for i3=0,n3-1 do begin
        for ialtitude=0,naltitude-1 do begin
           meanprofile(i3,ialtitude) = total(D(i3).profilelist(0:ntime-1,ialtitude)) / float(D(i3).ntime)
        endfor 
     endfor

     normalizedprofile=fltarr(n3,naltitude)
     for i3=0,n3-1 do begin
        normalizedprofile(i3,*) = meanprofile(i3,*) / max(meanprofile(i3,*) )
     endfor

     printf, 1, 'LEVEL', D(*).name, format='(a6,10(x,a15))'
     for ialtitude=naltitude-1,0,-1 do begin
        printf, 1, D(0).altitude(ialtitude), normalizedprofile(*,ialtitude), format='(f6.3,10(x,e15.3))'
     endfor
   
     close, 1

  endif

  end
