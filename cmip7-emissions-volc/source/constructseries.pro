@../../cmip6-emissions-ncar/source/getemptydata
@../../cmip6-emissions-gfed/source/convertfield
;
  function constructseries, activity=activity, sector=sector, species=species, yearlist=yearlist, origin=origin
;-------------------------
;
  nyear=n_elements(yearlist)
  nmonth=12
;
  S=getemptydata(ntimemax=nyear*nmonth,timestamp='date')
;
  itime=0

  topography=readtopography(origin=origin)

  for iyear=0,nyear-1 do begin
      
     year=yearlist(iyear)

     for imonth=0,nmonth-1 do begin

        month=imonth+1
;       read 3-dimensional data  
        A = readfield(activity=activity, sector=sector, species=species,year=year,month=month, origin=origin)
;
;       convert into global column
        F = getcolumn(data=A)

;       calculate global total
        global = total( F.field * F.area ) $
               * 86400. * 365.25 $ ; s-1 -> yr-1
               * 1.e-9             ; kg  -> Tg

        S.valuelist(itime)=global          
        S.timelist(itime)=year*10000L+month*100L      

        itime= itime+1
;
         Z =getzonalmean1D(data=F)

;        print, Z.field
;
;        plot, Z.latitude, Z.field
;        stop 
;
        volcanodata=scanforvolcanoes(data=A, activity=activity, sector=sector, species=species, origin=origin,topograph=topography)
        writeindividualvolcano, data=volcanodata
;
     endfor
  endfor

  S.name=species
  S.unit='Tg yr-1'
  S.ntime=itime

;
  return, S
;
  end
