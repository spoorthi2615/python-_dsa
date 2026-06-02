#magic number, if the sum of its digits are calculated till a single digit 
def magic_number(n):
    sum=0 # Variable to store the sum of digits
    while n>0:  # Loop to calculate the sum of digits
        reminder=n%10  # Get the last digit of the number
        sum=sum+reminder  # Add the digit to sum
        n=n//10  # Remove the last digit from the number
    # If the sum has more than one digit,
    # call the function again recursively
    if sum>9:
        return magic_number(sum)
    else:     # Otherwise return the single digit sum
        return sum
magic_num=int(input("enter the number:")) # Take input from the user
result=magic_number(magic_num) 
# Store the result returned by the function
if result==1: # Check whether the final result is 1
    print("magic number")# Print if it is a magic number
else:   
    print("not a magic number")    # Print if it is not a magic number       

    
  