n = int(input())
for i in range(n):
    s = int(input())
    if s<=108:
        if s%12 == 1:
            s+=11
            print(s,"WS")
        elif s%12 == 2:
            s+=9
            print(s, "MS")
        elif s%12 == 3:
            s+=7
            print(s,'AS')
        elif s%12 == 4:
            s+=5
            print(s, 'AS')
        elif s%12 == 5:
            s+=3
            print(s, 'MS')
        elif s%12 == 6:
            s+=1
            print(s, 'WS')
        elif s%12 == 7:
            s-=1
            print(s, 'WS')
        elif s%12 == 8:
            s-=3
            print(s, 'MS')
        elif s%12 == 9:
            s-=5
            print(s, "AS")
        elif s%12 == 10:
            s-=7
            print(s, 'AS')
        elif s%12 == 11:
            s-=9
            print(s, 'MS')
        elif s%12 == 0:
            s-=11
            print(s, "WS")
