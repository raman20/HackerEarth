'''
Given two strings of equal length, you have to tell whether they both strings are identical.

Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.

sample input:
3
sumit mitsu
ambuj jumba
abhi hibb

sample output:
YES
YES
NO
'''
testcase= int(input())
for i in range(testcase):
    count = 0
    string,substring = input().split(" ")
    string,substring = list(string),list(substring)
    string.sort()
    substring.sort()
    if len(string)==len(substring):
        for j in range(len(string)):
            if string[j] == substring[j]:
                count+=1
        if count == len(substring):
            print("YES")
        else:
            print("NO")
