'''''
(if , elif , else) (condiotion) : 
* (to do statmen) *

'''
print("###################(if)#####(else)########")
print("######################(elif)##############")

def valid_user(UserName):

    if len(UserName) < 3:                     
        print ("too short name ")  
    elif len(UserName) > 17:               # elif is = to else if
        print ("fuk u it soo long")
    else:
        print ("nice , good username fag")

valid_user("bo") 
valid_user("dasdadsadas") 
valid_user("saud")

print("###################(while)################")
print("##########################################")

'''''
(while) (condiotion) : 
* (to do statmen) *

'''
x = 0
while x < 5 :
    print(x)
    x += 1                                 # in paython there is not x++

print("####################(for)##(in)################")    
print("#################################(range)##(1)##")


'''''
(for) (varible) in range(num) : 
* (to do statmen) *

'''

# range from 0 example
for i in range(5):                     # mean range will be 0 , 1 , 2 , 3 , 4
    print(i)

print("####################(for)##(in)################")    
print("#################################(range)##(2)##")

# range from X to Y example
for i in range(5,10):                  # mean range will be 5 , 6 , 7 , 8 , 9
    print(i) 

print("####################(for)##(in)################")    
print("#################################(range)##(3)##")

# range from X to Y and jumping Z
for i in range(0,101,10):              # mean range will be 0 , 10 , 20 , 30 ...
    print(i)

print("###(for)###################(in)################")    
print("############(nasted)#############(range)#######")

for left in range(7):
    for right in range (left,7):
        print("[" + str(left) + "|" + str(right) + "]" , end=" ")
    print()    

'''''
#varibles is list contain number of varible
(for) (varible) in (varibles) : 
* (to do statmen) *

'''
print("#(for)##(varible)##(in)################")    
print("############(varibles)####('string')###")

# 'string' list example
names = ['saud' , 'mike' , 'frank']
for name in names :
    print(" hi " + name)

print("#(for)##(varible)##(in)################")    
print("############(varibles)####(integer)####")

# integer list example
values = [5,656,3,423]
sum = 0 
num = 0
for value in values:
    sum += value
    num += 1
print( "sum of values is " + str(sum) + " avrage of them is " + str(sum/num))

print("#(for)##(varible)##(in)################")    
print("############(varibles)####(nasted)#####")

teams = ['itthad' , 'hilal' , 'ahli' , 'nasr']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print( home_team + " VS " + away_team)


