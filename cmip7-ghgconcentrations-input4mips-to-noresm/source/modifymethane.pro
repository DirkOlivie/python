  pro modifymethane, data=data, scenario=scenario
;------------------
; 
; ONLY WORKS for ANNUAL DATA / NOT FOR MONTHLY DATA
;

  n=data.ntime

  for i=0,n-1 do begin

     date=data.timelist(i) 

     year= date / 10000L
     mmdd = date mod 10000L

;    only valid for annual files (we have only annual values from AMAP)
     if ( mmdd ne 0701L ) then stop

;    year <= 2014 
     if ( year le 2014 ) then begin ; 0000-2014

        cle=data.valuelist(i) 
        mfr=data.valuelist(i)

;    year <= 2050
     endif else if ( year le 2050 ) then begin ; 2015-2050

        case year of
           2015 : begin & cle= 1837.94 & mfr= 1837.94 & end
           2016 : begin & cle= 1844.64 & mfr= 1844.64 & end
           2017 : begin & cle= 1851.61 & mfr= 1851.61 & end
           2018 : begin & cle= 1858.89 & mfr= 1858.89 & end
           2019 : begin & cle= 1866.41 & mfr= 1866.41 & end
           2020 : begin & cle= 1874.14 & mfr= 1873.93 & end
           2021 : begin & cle= 1882.28 & mfr= 1877.82 & end
           2022 : begin & cle= 1891.00 & mfr= 1875.26 & end
           2023 : begin & cle= 1900.25 & mfr= 1866.66 & end
           2024 : begin & cle= 1910.00 & mfr= 1852.49 & end
           2025 : begin & cle= 1920.19 & mfr= 1833.35 & end
           2026 : begin & cle= 1930.59 & mfr= 1812.81 & end
           2027 : begin & cle= 1941.00 & mfr= 1793.70 & end
           2028 : begin & cle= 1951.41 & mfr= 1776.00 & end
           2029 : begin & cle= 1961.82 & mfr= 1759.61 & end
           2030 : begin & cle= 1972.24 & mfr= 1744.42 & end
           2031 : begin & cle= 1982.71 & mfr= 1730.25 & end
           2032 : begin & cle= 1993.27 & mfr= 1716.94 & end
           2033 : begin & cle= 2003.90 & mfr= 1704.43 & end
           2034 : begin & cle= 2014.61 & mfr= 1692.65 & end
           2035 : begin & cle= 2025.40 & mfr= 1681.54 & end
           2036 : begin & cle= 2036.34 & mfr= 1671.06 & end
           2037 : begin & cle= 2047.49 & mfr= 1661.16 & end
           2038 : begin & cle= 2058.85 & mfr= 1651.78 & end
           2039 : begin & cle= 2070.39 & mfr= 1642.90 & end
           2040 : begin & cle= 2082.10 & mfr= 1634.47 & end
           2041 : begin & cle= 2093.80 & mfr= 1626.46 & end
           2042 : begin & cle= 2105.38 & mfr= 1618.85 & end
           2043 : begin & cle= 2116.83 & mfr= 1611.61 & end
           2044 : begin & cle= 2128.17 & mfr= 1604.71 & end
           2045 : begin & cle= 2139.40 & mfr= 1598.13 & end
           2046 : begin & cle= 2150.54 & mfr= 1591.84 & end
           2047 : begin & cle= 2161.61 & mfr= 1585.81 & end
           2048 : begin & cle= 2172.61 & mfr= 1580.03 & end
           2049 : begin & cle= 2183.55 & mfr= 1574.47 & end
           2050 : begin & cle= 2194.43 & mfr= 1569.13 & end
        end
;
;    year > 2050
     endif else begin ; 2051-...

        cle=2194.43 & mfr= 1569.13 ; same value as 2050     

     endelse
;
     case scenario of 
       'hist_ssp245_amap_CLE' : data.valuelist(i)=cle
       'hist_ssp245_amap_MFR' : data.valuelist(i)=mfr
     endcase

  endfor
;    
  end
