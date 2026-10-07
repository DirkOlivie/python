def origindescriptionlist2ascii(origindescriptionlist) :
#------------------------------
    '''



    '''
    origin=''

    for origindescription in origindescriptionlist :
#       year
        origin=origin+'year:'+str("%4.4i"% origindescription['year'])+','
#       i4mpdownload
        origin=origin+'sourceid:['
        for i4mpdownload in origindescription['i4mpdownloadlist'] :
            origin=origin+i4mpdownload+','
        origin=origin+'],'
#       scenario
        origin=origin+'scenario:['
        for scenario in origindescription['scenariolist'] :
            origin=origin+scenario+','
        origin=origin+'],'
#       origyearlist
        origin=origin+'contributingyears:['
        for origyear in origindescription['origyearlist'] :
            origin=origin+str("%4.4i"% origyear)+','
        origin=origin+'],'
#       origweightlist
        origin=origin+'weights:['
        for origweight in origindescription['origweightlist'] :
            origin=origin+str("%1.4f"% origweight)+','
        origin=origin+'],'
        origin=origin+'\n'

    return origin
