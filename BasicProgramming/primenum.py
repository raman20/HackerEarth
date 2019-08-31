n = int(input())
for i in range(2,n+1):
    flag = 0
    for j in range(2,i):
        if i%j==0:
            flag+=1
            break
        else:
            continue
    if flag==0:
        print(i,end=" ")
