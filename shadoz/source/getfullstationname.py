def getfullstationname(station) :
#----------------------------

    if (   station == 'ascen'     ) : fullname='Ascension Island'
    elif ( station == 'costarica' ) : fullname='Costa Rica'
    elif ( station == 'fiji'      ) : fullname='Suva, Fiji'
    elif ( station == 'hanoi'     ) : fullname='Hanoi, Vietnam'
    elif ( station == 'hilo'      ) : fullname='Hilo, Hawaii'
    elif ( station == 'irene'     ) : fullname='Irene, South Africa'
    elif ( station == 'java'      ) : fullname='Java, Indonesia'
    elif ( station == 'kuala'     ) : fullname='Kuala Lumpur, Malaysia'
    elif ( station == 'nairobi'   ) : fullname='Nairobi, Kenya'
    elif ( station == 'natal'     ) : fullname='Natal, Brazil'
    elif ( station == 'paramaribo') : fullname='Paramaribo'
    elif ( station == 'reunion'   ) : fullname='La Reunion Island'
    elif ( station == 'samoa'     ) : fullname='Pago Pago, Samoa'
    elif ( station == 'sancrist'  ) : fullname='San Cristobal, Ecuador'
    else :
        print('No station recognized : ', station)
        quit()
    
    return fullname
