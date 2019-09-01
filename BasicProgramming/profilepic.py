L = int(input())
number = int(input())
data = []
for i in range(number):
    data = list(map(int,input().split()))
    W = data[0]
    H = data[1]
    if (W < L or H < L):print("UPLOAD ANOTHER")
    elif W == H:print("ACCEPTED")
    else:print("CROP IT")
