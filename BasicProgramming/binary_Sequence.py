# problem :-  https://bit.ly/2QavBQV

test = int(input())
for i in range(test):
    x,y,a,b = list(map(int,input().split()))
    if x*y == a+b:
        print('Yes')
    else:
        print('No')
