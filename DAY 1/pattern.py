#print square pattern
def square():
    n=int(input("enter the  number:"))
    for i in range(n):
        print("*"*n) # Print n asterisks for each of the n lines to form a square pattern
#square()

#print triangle pattern
def triangle():
    n=int(input("enter the  number:"))
    for i in range(n):
        print("*"*i) # Print i asterisks for each line, where i ranges from 0 to n-1, to form a right-angled triangle pattern
#triangle()

#upside down triangle
def upside_down_traingle():
    n=int(input("enter the  number:"))
    for i in range(n,0,-1):
        print("*"*i) # Print i asterisks for each line, where i starts from n and decreases to 1, to form an upside-down triangle pattern
#upside_down_traingle()  

#number btw square
def outine_square0():
    n=4
    k=1
    for i in range (n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1: # Check if we are on the border of the square (first or last row/column)
                print("*",end="") # Print an asterisk for border positions
            else:
                print(k,end="")# Print the current value of k for inner positions
                k+=1 # Increment k after printing it for inner positions
        print()
#outine_square0()

#space btw square
def outine_triangle():
    n=4
    for i in range (n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ") # Print a space for inner positions to create a hollow effect
        print()
#outline_triangle()

#right to left triangle
def outine_traingle1():
    n=4
    for i in range (1, n+1): # Loop from 1 to n to control the number of lines and asterisks
        for j in range(n-i):
                print(" ",end="") # Print spaces to shift the triangle to the right
        for j in range(i):    
                print("*",end="")# Print asterisks to form the triangle pattern, where the number of asterisks increases with each line
        print()
#outline_triangle1()

#right shifted rectangle
n=4
for i in range (n):
    for j in range(0, i+1):
        print(" ",end=" ") # Print spaces to shift the rectangle to the right, where the number of spaces increases with each line
    for j in range(0, n-1): #   Print n-1 asterisks for each line to form a rectangle pattern, where the number of asterisks remains constant   
        print("*",end=" ")# Print a space after each asterisk for better visibility         
    print()

