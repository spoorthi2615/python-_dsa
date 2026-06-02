#check whether a number is even or odd without using % (bitwise operator)
num=int(input("enter the number:"))
result= num & 1 #bitwise operation
if result ==0: #anything which is = 0 is odd 
    print ("even")
else:
    print("odd")
