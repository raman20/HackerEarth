l,r,k = input().split(" ")
count = 0
for i in range(int(l),int(r)):
    if i % int(k) == 0:
        count+=1
if int(r)%int(k)==0:
    count+=1
print(count)        
