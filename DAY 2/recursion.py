#1.FUNCTIONS
#1.1) set recurrsion limit
#import sys
#sys.setrecursionlimit(3000)#to set recurrsion
#def qwer(x): 2 usages
    #print("hi",x)
    #qwer(x+)
#qwer()

#output: 5 4 3 2 1
def fun(n):
    if n ==0:
        return
    print(n,end=" ")
    fun(n-1)
n=5
#fun(n)

#output: 1 2 3 4 5 
def fun(n):
    if n ==0:
        return
    fun(n-1)
    print(n,end=" ")
    
n=5
#fun(n)

#output: 5 4 3 2 1 1 2 3 4 5
def fun(n):
    if n ==0:
        return
    print(n,end=" ")
    fun(n-1)
    print(n,end=" ") #for reversal
n=5
#fun(n)

#output: 5 4 3 2 1 2 3 4 5
def fun(n):
    if n ==0:
        return
    print(n,end=" ")
    fun(n-1)
    if n!=1:
        print(n,end=" ") #for reversal
n=5
fun(n)

#****************************************************************************************

#1.2) find the factorial 
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

#****************************************************************************************

#1.3) check whether a given no is perfect square or not using recurssion 
def perfect_square(start,n):
    if (start*start==n):
        print("perfect square")
        return
    if (start*start>n):
        print("not a perfect square")
        return
    perfect_square(start+1,n)

perfect_square(2,36) #its a question check it

#****************************************************************************************

#1.4) find power of two 
def power_of_two(a,b):
    if b==0:
        return 1
    if b!=1:
        return a*power_of_two(a,b-1) 
    return a
print(power_of_two(2,3))

#****************************************************************************************

#1.5) geekforgeeks question
def reduce_number(n):
    if(n==1):
        return 0
    elif n%2==0:
        return 1+reduce_number(n//2)
    else:
        return 1+min(reduce_number(n-1),reduce_number(n+1))
n=15
print(reduce_number(n))

#****************************************************************************************