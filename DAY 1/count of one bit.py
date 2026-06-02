def count_of_bit():
    n=int(input("enter the  number:"))
    count=0  # Initialize counter to store number of set bits
    while n>0:  # Loop until number becomes 0
        n=n&(n-1)   # Remove the lowest set bit from n (Brian Kernighan’s algorithm)
        count +=1 # Increment count for each set bit removed
    print(count) # Print the total count of set bits in the original number
count_of_bit()



    
