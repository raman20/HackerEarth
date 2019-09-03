'''
Rahul is a very busy persion he dont wan't to waste his time .
He keeps account of duration of each and every work. 
Now he don't even get time to calculate duration of works, 
So your job is to count the durations for each work and give it to rahul.

sample input:
1 (test case)
1 44 2 14

sample output:
0 30
'''

N=int(input())
for i in range(N):
    SH,SM,EH,EM=input().split()
    TM=(int(EH)*60+int(EM))-(int(SH)*60+int(SM))
    HH=TM//60
    MM=TM%60
    print(HH,MM)
