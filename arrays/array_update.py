# problem -> https://bit.ly/364J2GS

test = int(input())
for _ in range(test):
    N,K = list(map(int,input().split()))
    a = [int(i) for i in input().split()]
    mini = min(a)
    if K>=mini:
        print(K-mini)
    else:
        print(0)
