#check whether a number is perfect number or not
n= int(input("enter the number:"))
sum=0 # Initialize sum of divisors to 0
for i in range(1,n): # Loop through all numbers from 1 to n-1
    if n%i==0:    # Check if i is a divisor of n
        sum=sum+i   # Add divisor to sum
if sum==n: # After loop, check if sum of divisors equals original number
    print("perfect number")
else: 
    print("not a perfect number")