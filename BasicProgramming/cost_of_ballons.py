n=int(input())
for i in range(n):
    g,p=input().split(" ")
    g,p=int(g),int(p)
    cand = int(input())
    sum1,sum2=0,0                #check the total price for both ballons price
    for i in range(cand):
        q1,q2=input().split(" ")
        q1,q2=int(q1),int(q2)
        if q1 == 1:
            sum1+=g
            sum2+=p
        if q2 == 1:
            sum1+=p
            sum2+=g
    print(min(sum1,sum2))        # then print the min of both price
