# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/

,,,
Input
First line contains a number N and Q as input. Next line contains N space separated 0 or 1. Next Q lines contain description of each query

Output
Output for only query type 0 L R whether the number in range L to R is "EVEN" or "ODD" (without quotes).

Sample Input
5 2
1 0 1 1 0
1 2
0 1 4

sample output
ODD
,,,

N , Q = list(map(int , input().split()))
n = list(map(int , input().split()))
cal = 0
sum1 = 0
for i in range(Q):
    inp = list(map(int , input().split()))
    if(inp[0]==1):
        if(n[inp[1]-1]==0):
            n[inp[1]-1] = n[inp[1]-1]+1
        else:
            n[inp[1]-1] = n[inp[1]-1]-1
    else:
        if(n[inp[2]-1]==1):
            print("ODD")
        else:
            print("EVEN")
