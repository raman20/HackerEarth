'''
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seven-segment-display-nov-easy-e7f87ce0/

Alice got a number written in seven segment format where each segment was creatted used a matchstick.

Example: If Alice gets a number 123 so basically Alice used 12 matchsticks for this number.

Alice is wondering what is the numerically largest value that she can generate by using at most the matchsticks that she currently possess.Help Alice out by telling her that number.


Input Format:

First line contains T (test cases).

Next T lines contain a Number N.

Output Format:

Print the largest possible number numerically that can be generated using at max that many number of matchsticks which was used to generate N.

'''


display = {'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6,'0':6}
n = int(input())
for i in range(n):
    num = input()
    stick = sum([display[j] for j in num])
    q,r = divmod(stick,2)
    print("7"*r+'1'*(q-r))
    
