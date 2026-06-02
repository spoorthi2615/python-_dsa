#bear and big brother codefroces
brother1,brother2=map(int,input("enter the ages of brothers:").split())
year=0 # Initialize year counter to 0
while brother1<=brother2: # Loop until brother1 becomes greater than brother2
    brother1=brother1*3 # Increase brother1's age (or value) by 3 times each year
    brother2=brother2*2 # Increase brother2's age (or value) by 2 times each yea
    year+=1 # Increment year count after each loop
print("years taken:",year)
