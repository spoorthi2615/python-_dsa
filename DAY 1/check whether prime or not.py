#check whether prime or not 
n = int(input("enter the number:"))
flag=0  # Initialize flag to 0 (assume number is prime)
for i in range (2,n):  # Loop from 2 to n-1 to check divisibility
    if n%i==0:  # If number is divisible by i, it's not prime
        print ("not a prime no")
        flag=1
        break # Exit loop early since we found a divisor
if flag == 0: # After loop ends, check flag value
    print("prime number")
