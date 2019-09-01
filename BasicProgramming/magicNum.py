# this code converts a string to another whose character ascii value is nearest prime no. and contains only alphabet.
# sample input:
# AFREEN   
# sample output:
# CGSCCO

def prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
    else:
        return True
            
def nextprime(a):
    if ((65<=a<=90)or(97<=a<=122)) and prime(a):
        return a
    low = a-1
    high = a+1
    while(True):
        if ((65<=low<=90) or (97<=low<=122)) and prime(low) :
            return low
        elif ((65<=high<=90) or (97<=high<=122)) and prime(high):
            return high
        else:
            low-=1
            high+=1
            
n = int(input())
for i in range(n):
    magicstring=str()
    lenofstr = int(input())
    string = input()
    if len(string)==lenofstr:
        for i in string:
            magicstring+=chr(nextprime(ord(i)))
        print(magicstring)   
