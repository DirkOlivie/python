;@../../cmip6-ghgconcentrations-input4mips/source/getemptydata [appeared not to exist]
;
  function biascorrectseries, S0=S0, S1=S1
;---------------------------
;
; INPUT
;	S0 : series with correct length [FORCeS]
;	S1 : only historical period
;
       
;	S1 : --------------------------------------
;            |            |              |        |
;       S0 : |            ------------------------------------------------
;            |            |              |        |                      |  
;          1750         1990           2010     2014                   2051
;



;
; CALLS
;	getemptydata
;-----------------------------
;
; check 
  if ( S0.unit ne S1.unit) then stop
  if ( S0.name ne S1.name  and ( S0.name ne 'methane_pct50' and S1.name ne 'methane' ) ) then begin 
     print, 'S0.name : ', S0.name
     print, 'S1.name : ', S1.name
     stop
  endif

  n0=S0.ntime ; # dates in S0
  n1=S1.ntime ; # dates in S1
;
; extract list wiht only years
  yearlist0 = S0.timelist / 10000L ; [1990, 1990, 1990, ..., 1990, 1991, ..., 1991, 1991, ...]
  yearlist1 = S1.timelist / 10000L
;
; find bias based on 2010-2014 period
; find subset of years between 2010 and 2014
  iset0 = where (yearlist0 ge 2010 and yearlist0 le 2014 ) 
  iset1 = where (yearlist1 ge 2010 and yearlist1 le 2014 ) 
  if ( n_elements(iset0) ne n_elements(iset1) ) then stop

; calculate bias over 2010-2014 period
  bias = total( S1.valuelist(iset1) ) / float( n_elements( S1.valuelist(iset1) ) ) $
       - total( S0.valuelist(iset0) ) / float( n_elements( S0.valuelist(iset0) ) )
; 
; new series
  S=getemptydata(ntimemax=n0,timestamp='date')
  S.timelist=S0.timelist
  S.name=S0.name
  S.unit=S0.unit
  S.ntime=n0

; correct S0 timeseries
  for itime=0,n0-1 do begin
     if ( yearlist0(itime) le 2014 ) then begin ; years ...-2014
        ifound=where(S0.timelist(itime) eq S1.timelist)
        S.valuelist(itime) = S1.valuelist(ifound)
     endif else begin                           ; year 2015-...
        S.valuelist(itime) = S0.valuelist(itime) + bias
     endelse
  endfor 
;
  return, S
;
  end
