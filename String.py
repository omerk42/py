
## define string

s1 = ' string    '
s2 = "STRING"
s3 = str(654)
Ss4 = ['omer', 'abdulaziz', 'ali', 'khan']
s5 = 'omer khan is your friend <.^.>'
## String methods

s1.upper()                  #make string captial
s2.lower()                  #make string small

s1.lstrip()                 #remove spaces from left
s1.rstrip()                 #remove spaces from right
s1.strip()                  #remove spaces from both sides

s1.count('s')               #cont num of char in string

s1.endswith('ing')          #boolean of end string

s1.isnumeric()              #bolean if string made of number
s3.isnumeric()

print('  '.join(Ss4))       #join between element in the list with(STR)
print("@@@".join(Ss4))

print(s5.split())           #split string to sub string list

