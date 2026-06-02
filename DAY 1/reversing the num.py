#reversing the num
num=int (input("enter the number:"))
rev=0  # Stores the reversed number
while num>0:# Loop to reverse the digits of the number
    remind=num%10  # Get the last digit of the number
    rev=rev*10+remind # Shift existing digits left and add the new digit
    num=num//10# Remove the last digit from the number
print("reversed number is:",rev) # Print the final reversed result
