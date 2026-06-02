#n=5 find XOR of 1 to n 
n=int(input("enter the number:"))
if n % 4==0: #if reminder is 0 ,XOR from 1 to n is n 
    print (n)
elif n % 4 == 1: #if reminder is 1 ,XOR from 1 to n is 0
    print (1)
elif n % 4 == 2: #if reminder is 2 ,XOR from 1 to n is n + 1+
    print (2)
else:
    print(0)
