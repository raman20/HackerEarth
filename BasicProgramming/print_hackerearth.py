#problem:-> https://bit.ly/2QeEVmT

data = ['h','a','c','k','e','r','e','a','r','t','h']
dataset = list(set(data))
n = int(input())
length = list()
dataset.sort()
string =  [x for x in input()]
for i in dataset:
    q,r = divmod(string.count(i),data.count(i))
    length.append(q)
length.sort()
print(length[0])
    
