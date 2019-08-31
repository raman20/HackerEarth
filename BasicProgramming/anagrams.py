n = int(input())
for i in range(n):
    d=0
    a = input()
    b = input() 
    l1 = list(a)
    l2 = list(b)
    for i in l1[:]:
        if i in l2:
            l2.remove(i)            
            l1.remove(i)
        else:
            d+=1
    d+=len(l2)
    print(d)
