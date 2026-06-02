def power_of_two():
    n=int(input("enter the number:"))
    if n & (n-1) == 0: # Check if n is a power of two by verifying that it has only one set bit
        print("power of two")
    else:
        print("not a power of two")
power_of_two()