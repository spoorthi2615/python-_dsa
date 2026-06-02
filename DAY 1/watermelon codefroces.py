w=int(input("enter:")) #input the weight of the watermelon
if w%2==0 and w>2: #check if the weight is even and greater than 2
    x=w//2 #divide the weight into 2 parts 
    if x%2==0: #check if the first part is even 
        print(x,x) #both parties can be equal
    else:
        print(x-1,x+1) #adjust the parts to make both even
else:
    print("impossible")
