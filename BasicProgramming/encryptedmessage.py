'''
Indian army is going to do a surprise attack on one of its enemies country. The President of India, the Supreme Commander of the Indian Army will be sending an alert message to all its commanding centers. As enemy would be monitoring the message, Indian army is going to encrypt(cipher) the message using basic encryption technique. A decoding key 'K' (number) would be sent secretly.

You are assigned to develop a cipher program to encrypt the message. Your cipher must rotate every character in the message by a fixed number making it unreadable by enemies.

Given a single line of string 'S' containing alpha, numeric and symbols, followed by a number '0<=N<=1000'. Encrypt and print the resulting string.

Note: The cipher only encrypts Alpha and Numeric. (A-Z, a-z, and 0-9) . All Symbols, such as - , ; %, remain unencrypted.

sample input:

All-convoYs-9-be:Alert1.
4

sample output:

Epp-gsrzsCw-3-fi:Epivx5.
'''

message = input()
k = int(input())
encrypted = str()
for i in message:
    l=ord(i)
    if 65<=l<=90:
        for _ in range(k):
            l+=1
            if l>90:
                l=65
        encrypted+=chr(l)
    elif 97<=l<=122:
        for _ in range(k):
            l+=1
            if l>122:
                l=97
        encrypted+=chr(l)
    elif 48<=l<=57:
        for _ in range(k):
            l+=1
            if l>57:
                l=48
        encrypted+=chr(l)
    else:
        encrypted+=chr(l)
print(encrypted)        
