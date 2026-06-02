#strong number 
def strong(n):
    sum=0 #Stores the sum of factorials
    temp=n # Keeps a backup of the original number
    while temp>0: # Loop to process each digit of the number
        digit=temp%10 # Extracts the last digit
        fact=1 # Calculate the factorial of the extracted digit
        for i in range(1,digit+1):
            fact=fact*i
        sum=sum+fact  # Add the factorial to the total sum
        temp=temp//10 # Remove the last digit from the number
    if sum==n: # Check if the calculated sum matches the original number
        print("strong number")
    else:
        print("not a strong number")
          