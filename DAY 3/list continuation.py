#list continuation
#1.1) running sum of 1d array (leeetcode question)
#Given an array nums. We define a running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]). 
# Return the running sum of nums.

class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)): # start from 1 because the first element is already the sum of itself
            nums[i] += nums[i - 1] # add the previous element to the current element to get the running sum
        return nums


nums = [1, 2, 3, 4]

sol = Solution()          # Create object
print(sol.runningSum(nums))  # Call method

#*************************************************************************************************************

#1.2) moves zeros (283-leetcode question)
#Given an integer array nums, move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array 

class Solution:
    def moveZeroes(self, nums):
        j = 0 # j will keep track of the position of the next non-zero element
        for i in range(len(nums)): # iterate through the array
            if nums[i] != 0: # if the current element is not zero, swap it with the element at index j
                nums[i], nums[j] = nums[j], nums[i] # 
                j += 1 # increment j to point to the next position for the next non-zero element

nums = [0, 1, 0, 3, 12]

sol = Solution() 
sol.moveZeroes(nums) # Call method

print(nums)

#*************************************************************************************************************

#1.3)  no of matchesticks
l=[6,2,5,5,4,5,6,3,7,6]
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
sum=a+b
total=0 # this will keep track of the total number of matchsticks needed to represent the sum of the two numbers
while sum>0: # while sum is greater than 0, we will keep extracting the last digit and adding the corresponding matchsticks to the total
    d=sum%10 # extract the last digit of the sum
    total+=l[d] # add the number of matchsticks needed to represent the digit d to the total
    sum//=10 # remove the last digit from the sum by performing integer division by 10
print("No. of matchsticks:",total)

# *************************************************************************************************************

# 1.4) remove element (leetcode question-27)
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.      
def removeElement(nums, val):
    j = 0
    for i in range(len(nums)): # iterate through the array
        if nums[i] != val: # if the current element is not equal to val, swap it with the element at index j
            nums[i], nums[j] = nums[j], nums[i] # swap the current element with the element at index j to move it to the front of the array
            j += 1# increment j to point to the next position for the next non-val element
    return j

nums = [3, 2, 2, 3]
val = 3

result = removeElement(nums, val)

print("Number of elements not equal to val:", result)
print("Modified list:", nums)

#*************************************************************************************************************

# 1.5)find the second largest element in a list without linked list,slicing
arr=[1,2,3,4,5]
m1=arr[0] # m1 will keep track of the largest element
m2=arr[0] # m2 will keep track of the second largest element
for i in range(1,len(arr)): # iterate through the array starting from the second element
    if arr[i]>m1: # if the current element is greater than m1, update m2 to be m1 and m1 to be the current element
        m2=m1
        m1=arr[i]
    elif arr[i]>m2 and arr[i]!=m1: # if the current element is greater than m2 and not equal to m1, update m2 to be the current element
        m2=arr[i]
print("Second largest element:", m2)    

# *************************************************************************************************************

# 1.6) Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
def removeDuplicates(nums):
    if not nums: # if the input list is empty, return 0 because there are no unique elements
        return 0
    j = 0 # j will keep track of the position of the last unique element found
    for i in range(1, len(nums)): # iterate through the array starting from the second element
        if nums[i] != nums[j]: # if the current element is not equal to the last unique element found, it means we have found a new unique element
            j += 1 # increment j to point to the next position for the new unique element
            nums[i], nums[j] = nums[j], nums[i] # swap the current element with the element at index j to move the new unique element to the front of the array
    return j + 1
nums = [1, 1, 2, 2, 3, 4, 4]
k = removeDuplicates(nums)

print(k)          # 4
print(nums[:k])   # [1, 2, 3, 4]

# *************************************************************************************************************



