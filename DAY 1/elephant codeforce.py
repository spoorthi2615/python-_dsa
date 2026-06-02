#input the coordinate of friends house 
x=int(input("enter the value:"))
#calculate min num of steps
if x%5==0:
    print(x//5)  # Print exact number of steps
else:
    print((x//5)+1) # Add one extra step for remaining distance