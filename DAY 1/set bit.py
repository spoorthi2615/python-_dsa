def count_i_segment():
    n=int(input("enter the number"))
    key=int(input("enter where to find the key"))
    if (n & (1<<key)!=0):# Check if the bit at position 'key' in 'n' is set (1) by performing a bitwise AND with a mask that has only the 'key'-th bit set
        print("set bit")
    else:
        print("not set bit")
count_i_segment()      