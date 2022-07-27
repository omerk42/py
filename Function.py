# function with print return
def hi(name , nat):
    print("hi  "+ name)
    print ("our friend from " + nat )
# call the function
a = hi("saud" , "saudi")
print (a)                                       # the output here will be (None) which mean variable is empty

# function with single retun value
def area_triangle( haight , base):
    return haight * base / 2
# call the function
area_a = area_triangle(12,3)
area_b = area_triangle(5 , 3)
area_sum = area_a + area_b
print ( "triangle a and b areas is =  " + str(area_sum))

# function with multiple return values
def second2_H_M_S(sec):
    hours = sec // 3600                         # (//) mean that result will ignore dicmal part
    minuts = (sec - hours * 3600) // 60         # (//) mean that result will ignore dicmal part
    seconds = sec - hours * 3600 - minuts * 60
    return hours , minuts , seconds
# call the function
hours , minuts , seconds = second2_H_M_S(5000)  # multiple assignment to one fucvtion is valid 
print ( hours , minuts , seconds)

