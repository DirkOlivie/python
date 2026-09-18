@../../routines/source/readnc
;
  pro test
;---------
;
  dir='/lustre/storeA/users/dirkjlo/emissions/aerocom/volc'
;
; CONTINUOUS
  filename=dir+'/contineous_volc.nc'
;
  field=readnc('field',filename)
  iset=where(field ne 0.)
  print, n_elements(iset)
  print, total(field)*1.e-9
;
  field=readnc('height_low',filename)
  iset=where(field ne 0.)
  print, size(field)
  stop

  print, n_elements(iset)
;
  height_low = readnc('height_low',filename) & print, min(height_low(iset)), max(height_low(iset))
  height_high = readnc('height_high',filename) & print, min(height_high(iset)), max(height_high(iset))
  volcano_heigth = readnc('volcano_heigth',filename) & print, min(volcano_heigth(iset)), max(volcano_heigth(iset))

; EXPLOSIVE
  filename=dir+'/explosive_volc.nc'

  field=readnc('field',filename)
  iset=where(field ne 0.)
  print, n_elements(iset)
  print, total(field)*1.e-9
; 
  field=readnc('height_low',filename)
  iset=where(field ne 0.)
  print, n_elements(iset)
;
  height_low = readnc('height_low',filename) & print, min(height_low(iset)), max(height_low(iset))
  height_high = readnc('height_high',filename) & print, min(height_high(iset)), max(height_high(iset))
  volcano_heigth = readnc('volcano_heigth',filename) & print, min(volcano_heigth(iset)), max(volcano_heigth(iset))

;  print, volcano_heigth(iset)

;  iiset=where(volcano_heigth(iset) eq 0)

;  print, field(iset(iiset))

;
  end
