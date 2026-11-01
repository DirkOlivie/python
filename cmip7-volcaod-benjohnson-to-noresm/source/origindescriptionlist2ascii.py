def origindescriptionlist2ascii(origindescriptionlist) :
#------------------------------
    '''



    '''
    origin=''

    for origindescription in origindescriptionlist :
#       year
        origin=origin+'year:'+str("%4.4i"% origindescription['year'])+','
#       i4mpdownload
        origin=origin+'contributing year:'+str("%4.4i"% origindescription['origyear'])+','
#       period
        origin=origin+'extracted from period:'+origindescription['origperiod']+','
#       i4mpdownload
        origin=origin+'sourceid:'+origindescription['i4mpdownload']+','
#       scenario
        origin=origin+'scenario:'+origindescription['scenario']+','
#
#       go to new line
        origin=origin+'\n'

    return origin
