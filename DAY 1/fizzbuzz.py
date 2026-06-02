#fizzbuzz 
#if number is div by 3 then print fizz,
#if number is div by 5 print buzz
#if div by both 3 and 5 print fizzbuzz
def fizzbuzz(): # Define a function called fizzbuzz
    num=int(input("enter the number:")) # Take input from user and convert it to integer
    if (num%3==0 %num%5==0):# Check if number is divisible by BOTH 3 and 5  # fixed condition using 'and'
        print("fizzbuzz")
    elif (num%3==0): # Check if number is divisible by 3 only
        print ("frizz")
    elif (num%5==0):# Check if number is divisible by 5 only
        print ("buzz")
    else:    # If none of the above conditions are true
        print("nothing")
fizzbuzz()
        