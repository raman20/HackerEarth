'''
Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another, and started doing their work. They decided , they end up with a fun challenge who will put the last brick.

They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.

There are only N bricks, you need to help find the challenge result to find who put the last brick.

sample input:
13
sample output:
Motu
'''

bricks = int(input())
n=bricks
for i in range(n):
    if bricks <=i:
        print("Patlu")
        break
    if bricks > i:
        bricks-=i
    if bricks <=2*i:
        print("Motu")
        break
    if bricks > 2*i:
        bricks-=2*i
