# sample input
# abcE
# sample output
# ABCe

string = input()
newstring = ''
for i in string:
    if i.isupper():
        newstring+=i.lower()
    elif i.islower():
        newstring+=i.upper()
print(newstring)    
