  function scanforvolcanoes, data=data, activity=activity, sector=sector, species=species, origin=origin, topography=topography
;--------------------------


  nlev=data.nlev
  nmax=1000
  lonlist=fltarr(nmax)
  latlist=fltarr(nmax)
  emistotlist=fltarr(nmax)
  hghlist=fltarr(nmax)
  lowlist=fltarr(nmax)
  proflist=fltarr(nmax,nlev)
  ihghlist=intarr(nmax)
  ilowlist=intarr(nmax)
  height_low=fltarr(nmax)
  height_high=fltarr(nmax)
  volcano_height=fltarr(nmax)
  topographylist=fltarr(nmax)

  i=0
 
  for ilon=0,data.nlon-1 do begin
     for ilat=0,data.nlat-1 do begin
        
        if ( total(data.field(ilon,ilat,*)) ne 0. ) then begin

           lonlist(i)=(data.longitude(ilon)+720.) mod 360. ; garantee that all longitudes are positive
           latlist(i)=data.latitude(ilat)
;           for ilev=0,data.nlev-1 do begin
;             if ( data.field(ilon,ilat,ilev) ne 0. ) then begin
;                printf, 1, ilev, data.levbnds(ilev), data.levbnds(ilev+1), data.field(ilon,ilat,ilev),format='(i2,x,i5,x,i5,e10.3)'
;             endif
;          endfor
           proflist(i,*) = data.field(ilon,ilat,*)/max(data.field(ilon,ilat,*)) ; normalized profile
           

           ilist=where(data.field(ilon,ilat,*) ne 0.)
           ilow = min(ilist)
           ihgh = max(ilist) 
            
           lowlist(i) = min([data.levbnds(ilow),data.levbnds(ilow+1),data.levbnds(ihgh),data.levbnds(ihgh+1)])
           hghlist(i) = max([data.levbnds(ilow),data.levbnds(ilow+1),data.levbnds(ihgh),data.levbnds(ihgh+1)])

           ilowlist(i) = min([ilow,ihgh])
           ihghlist(i) = max([ilow,ihgh])

           emistotlist(i) = data.area(ilon,ilat) $ ; m2
                   * total ( abs( data.levbnds(1:data.nlev) - data.levbnds(0:data.nlev-1) ) * data.field(ilon,ilat,*) ) $
                   * 365.25 * 86400  $
                   * 1.e-9 ; kg -> Tg
;
           if ( origin eq 'aerocomnetcdf' ) then begin

              height_low(i)=data.height_low(ilon,ilat)
              height_high(i)=data.height_high(ilon,ilat)
              volcano_height(i)=data.volcano_height(ilon,ilat)

           endif 
;
           topographylist(i) = topography(ilon,ilat)

           i=i+1

        endif
     endfor
  endfor
  n=i
;
  volcanolist={origin : origin, $
               activity    : activity, $
               sector      : sector, $
               species     : 'SO2', $
               lonlist     : lonlist(0:n-1), $
               latlist     : latlist(0:n-1), $
               emistotlist : emistotlist(0:n-1), $
               hghlist     : hghlist(0:n-1),$
               lowlist     : lowlist(0:n-1),$
               ihghlist    : ihghlist(0:n-1),$
               ilowlist    : ilowlist(0:n-1),$
               proflist    : proflist(0:n-1,*),$
               height_low     : height_low(0:n-1),$
               height_high    : height_high(0:n-1),$
               volcano_height : volcano_height(0:n-1),$
               topographylist : topographylist(0:n-1),$
;
               n           : n }

  return, volcanolist
;
  end
