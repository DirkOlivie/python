def addbeg(prefix, data) :
#--------------------------

# check prefix
    if ( type(prefix) != str ) :
       print('Prefix is not a string')
       quit() 

# check list
    if ( type(data) != list) :
        print('Data is not a list')
        quit()
# new list   
    newdata = []

# loop over elements  
    for element in data :
        newdata.append(prefix+element)

    return newdata 


def addend(data, suffix) :
#-------------------------

# check list
    if ( type(data) != list) :
        print('Data is not a list')
        quit()

# check suffix
    if ( type(suffix) != str ) :
       print('Prefix is not a string')
       quit() 

# new list   
    newdata = []

# loop over elements  
    for element in data :
        newdata.append(element+suffix)

    return newdata 











