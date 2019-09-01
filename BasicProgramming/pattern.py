'''
sample input:
1 (no. of test case)
9 (no. of rows)

sample output:

*################*
**##############**
***############***
****##########****
*****########*****
******######******
*******####*******
********##********
******************
'''

t=int(input())
for o in range(t):
    n=int(input())
    p=list()
    for i in range(1,n+1):
        p.clear()
        for j in range(i):
            p.append('*')
        for j in range(n-i):
            p.append("##")
        for j in range(i):
            p.append("*")
        l=''.join(p)
        print(l)
    print("\n") 
