'''
{a,e,i,o,u,A,E,I,O,U}

Natural Language Understanding is the subdomain of Natural Language Processing where people used to design AI based applications 
have ability to understand the human languages. 
HashInclude Speech Processing team has a project named Virtual Assistant. 
For this project they appointed you as a data engineer 
(who has good knowledge of creating clean datasets by writing efficient code). 
As a data engineer your first task is to make vowel recognition dataset. 
In this task you have to find the presence of vowels in all possible substrings of the given string. 
For each given string you have to print the total number of vowels.

sample input:
1
baceb

sample output:
16

'''

n = int(input())
st = {'a','e','i','o','u','A','E','I','O','U'}
for _ in range(n):
    s = input().strip()
    c = 0
    for i in range(len(s)):
        if s[i] in st:
            c += i*(len(s)-i-1) + len(s)
    print('{}\n'.format(c))
