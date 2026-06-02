#A number is called an Automorphic number if and only if its square ends in the same digits as the number itself.
def automorphic():
    n=int(input("enter the  number:"))# Take input from user and convert to integer
    temp=n # Store original number for digit counting
    sq=n*n# Calculate square of the number
    dc=0# Initialize digit count to 0
    while temp>0: # Count number of digits in n
        dc+=1# Increase digit count by 1
        temp//=10# Remove last digit
    po=10**dc# Calculate power of 10 based on digit count
    if n==sq%po:  # Check if last digits of square match the original number
        print("automorphic")
    else:
        print("not automorphic")
automorphic()