a=int(input())
temp=a# Store original number
count=0 
# Variable to count digits
while temp>0:
    temp=temp//10
    count=count+1
n=a # Store original number for comparison

sum=0 # Variable to store sum

for i in range(count): # Loop through each digit
    reminder=a%10 # Get last digit
    sum=sum+(reminder**count)  # Add power of digit to sum
    a=a//10 # Remove last digit
if(sum==n):# Check if number is Armstrong number
    print("armstring number")
else:
    print("not a armstring number")
