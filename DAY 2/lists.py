#2) lists
#2.1) remove the duplicates 
# l=list(map(int,input("enter the elements").split()))
# l1=[]
# for i in l:
#     if i not in l1:
#        l1.append(i)
# print(l1)

#***************************************************************************************

#2.2) find the no. which got repeated for odd no. of times [1,2,1,2,2,3,5,6,6]
# ls=list(map(int,input("enter the elements").split()))
def odd_repeat_count(ls):
    l1=[]
    for i in ls: #for i in ls:
        if ls.count(i)>2 and i not in l1: # if ls.count(i)>2 and i not in l1: #for i in ls:
            l1.append(i)#            print(i) #print(i)
    print(l1)
#odd_repeat_count(ls)

#****************************************************************************************

#2.3)sort the list in unique way
#>first even no.s in descending to ascending 
#>then odd no.s in ascending to descending
ls=list(map(int,input("enter the elements").split()))
def sorting(ls):
    ls.sort(reverse=True) #for i in ls:
    for i in ls[::-1]: 
        if i%2!=0: 
            ls.append(i) 
            ls.remove(i)
    print(ls)
#sorting(ls)

#****************************************************************************************

#2.4) police recruites codeforces 
def police_recruite(ls):
    police=0
    count=0
    for i in ls:
        if i<0:
            if (police>i):
                police=police-1
            else:
                count+=1
        police+=i
    print(count)
#police_recruite(ls)

#****************************************************************************************

#2.5) nums=[1,2,3,4]
#output= [1,3,6,10]
#leatcode question

def num_sum(ls):
    out=[]
    sum=0
    i=0
    while i!=len(ls):
        for j in range (i,-1,-1):
            sum=sum+ls[j]
        out.append(sum)
        sum=0
        i=i+1
    print(out)
# num_sum(ls)
            

#2.6) lemonade change (leetcode 860)
# At a lemonade stand, each lemonade costs $5.
# Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
# Note that you do not have any change in hand at first.
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

def lemonade_change(ls):
    five=0
    ten=0
    for i in ls:
        if i==5:
            five+=1
        elif i==10:
            if five>0:
                five-=1
                ten+=1
            else:
                return False
        elif i==20:
            if ten>0 and five>0:
                ten-=1
                five-=1
            elif five>=3:
                five-=3
            else:
                return False
    return True

