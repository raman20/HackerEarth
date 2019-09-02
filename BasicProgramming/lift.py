"""
There are 7 floors in BH3 and only 2 lifts. Initially Lift A is at the ground floor and Lift B at the top floor. 
Whenever someone calls the lift from N th floor, the lift closest to that floor comes to pick him up. 
If both the lifts are at equidistant from the N th floor, them the lift from the lower floor comes up.

sample input :
2 (test case)
3
5

sample output:
A
A
"""

test = int(input()) #test case
A,B=0,7
for i in range(test):
    floor = int(input())
    if (abs(floor-A) < abs(floor-B)) or abs(floor-A)==abs(floor-B):
        print("A")
        A=floor
    else:
        B=floor
        print('B')
