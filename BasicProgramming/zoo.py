'''
You are required to enter a word that consists of x and y that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 2 x X = Y.

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

First line: A word that starts with several Zs and continues by several Os.


Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.
'''


zoo = input()
z,o=0,0
for i in zoo:
    if i == 'z':
        z=z+1
    else:
        o=o+1
if 2*z == o:
    print("Yes")
else:
    print("No")
