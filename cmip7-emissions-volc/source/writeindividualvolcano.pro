  pro writeindividualvolcano, data=D
;---------------------------

; INPUT
;	data
;


 print, D.origin+'_'+D.activity+'_'+D.sector+'_'+D.species
 n=D.n

  openw, 1, '../info/individualvolcano_'+D.origin+'_'+D.activity+'_'+D.sector+'_'+D.species+'.txt'

; I. global overview
  printf, 1, 'VOLCANOES = ', n, format='(a12,x,i3)'
  printf, 1, 'TOTAL [Tg/yr] = ', total(D.emistotlist(*)), format='(a15,x,f6.2)'

;  explicitly given as field
  if ( D.origin eq 'aerocomnetcdf--' $
    or D.origin eq 'aerocomascii--' ) then begin
;
;      look at all volcanoes
       printf, 1, 'ALL'
       printf, 1, 'LOW [m]=', min(D.height_low(*)), max(D.height_low(*)), format='(a8,x,i4,x,i4)'
       printf, 1, 'HGH [m]=', min(D.height_high(*)), max(D.height_high(*)), format='(a8,x,i4,x,i4)'
       if ( D.origin eq 'aerocomnetcdf' ) then printf, 1, 'PEAK [m]=', min(D.volcano_height(*)), max(D.volcano_height(*)), format='(a8,x,i4,x,i4)'

;      look at ones with top higher than 0
       iset = where(D.height_high ne 0.)       
       printf, 1, 'SELECTION'
       printf, 1, 'LOW [m]=', min(D.height_low(iset)), max(D.height_low(iset)), format='(a8,i4,x,i4)'
       printf, 1, 'HGH [m]=', min(D.height_high(iset)), max(D.height_high(iset)), format='(a8,x,i4,x,i4)'
       if ( D.origin eq 'aerocomnetcdf' ) then printf, 1, 'PEAK [m]=', min(D.volcano_height(iset)), max(D.volcano_height(iset)), format='(a8,x,i4,x,i4)'
;
   endif else begin ; derived from 3D fields
;
;      look at all volcanoes
       printf, 1, 'ALL'
       printf, 1, 'LOW [m]=', min(D.lowlist(*)), max(D.lowlist(*)), format='(a8,x,i4,x,i4)'
       printf, 1, 'HGH [m]=', min(D.hghlist(*)), max(D.hghlist(*)), format='(a8,x,i4,x,i4)'

;      look at ones with top higher than 0
       iset = where(D.hghlist ne 0.)
       printf, 1, 'SELECTION'
       printf, 1, 'LOW [m]=', min(D.lowlist(iset)), max(D.lowlist(iset)), format='(a8,i4,x,i4)'
       printf, 1, 'HGH [m]=', min(D.hghlist(iset)), max(D.hghlist(iset)), format='(a8,x,i4,x,i4)'
;
;
     endelse

;II. list individual volcanoes

; order according to latitude and longitude

  ilist=sort(D.latlist(0:n-1)+D.lonlist(0:n-1)*0.00001)

  for isort=0,n-1 do begin
     i=ilist(isort)
; sort
     c0='TOPO [m]='+string(D.topographylist(i), format='(i4)')
     c1='LON='+string(D.lonlist(i), format='(x,f8.2)')
     c2='LAT='+string(D.latlist(i), format='(x,f8.2)')
     c3= 'TOTAL [Tg/yr]='+string(D.emistotlist(i), format='(x,f10.4)')

     if ( D.origin eq 'aerocomnetcdf--' $
       or D.origin eq 'aerocomascii--' ) then begin
;	explicitly given as field
        c4= 'LOW [m]='+string(D.height_low(i), format='(x,i4)')
        c5= 'HGH [m]='+string(D.height_high(i), format='(x,i4)')
        c6= '';,'PEAK [m]='+string(D.volcano_height(i), format='(x,i4)')
;
     endif else begin
;       derived from 3D fields
        c4= 'LOW [m]='+string(D.lowlist(i), format='(x,i4)')
        c5= 'HGH [m]='+string(D.hghlist(i), format='(x,i4)')
        c6=''
        for ilev=D.ilowlist(i),D.ihghlist(i) do begin
           c6=c6+' '+string(D.proflist(i,ilev),format='(f4.2)')
        endfor
        c6 = c6+' ['+string(D.ilowlist(i),format='(i2)')+'-'+string(D.ihghlist(i),format='(i2)')+']' 
;
     endelse

     printf, 1, c0+' '+c1+' '+c2+' '+c3+' '+c4+' '+c5+c6
;
  endfor




  close, 1

  end
