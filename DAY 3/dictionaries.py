# # Dictionary

# d = {
#     1: "hello",
#     2: 100,
#     3: "apple",
#     4: [1, 2, 3]
# }

# # Accessing a value using key
# print(d[1])          # hello
# # Using get() method
# print(d.get(2))      # 100
# # If key doesn't exist
# print(d.get(6))      # None
# # Print entire dictionary
# print(d)
# # Print all keys
# print(d.keys())
# # Print all values
# print(d.values())
# # Print all key-value pairs
# print(d.items())
# # Remove a specific key
# print(d.pop(4))      # [1, 2, 3]
# print(d)
# # Remove the last inserted item
# print(d.popitem())
# print(d)
# # Clear the dictionary
# d.clear()
# print(d)

# #*************************************************************************************************************

# # to print the names and grades of the students using dictionary
# d = {
#     "neha": 80,
#     "priya": 90,
#     "sneha": 85,
#     "nisha": 95,
#     "ananya": 88
# }
# grades = {}  # this is the new dictionary
# for name in d:
#     marks = d[name]  # marks is the value of the key name
#     if marks > 90:
#         grades[name] = "A+"
#     elif marks > 80:
#         grades[name] = "B+"
#     elif marks > 70:
#         grades[name] = "C+"
#     elif marks > 60:
#         grades[name] = "D+"
#     else:
#         grades[name] = "F"
# print(grades)

# #*************************************************************************************************************

# # to find the frequency of the numbers in the list using dictionary
# arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# d = {}
# for i in arr:
#     d[i] = d.get(i, 0) + 1
# print(d)

# #*************************************************************************************************************

# # to find the most frequent element in the list using dictionary
# arr = [1, 2, 2, 1, 3, 1, 4, 3, 4, 2]
# d = {}
# for i in arr:
#     d[i] = d.get(i, 0) + 1
# freq = 1
# res = -1
# for i in d:
#     if d[i] > freq:
#         freq = d[i]
#         res = i
# print("most frequent element is:", res)

#*************************************************************************************************************

#Hash Map / Dictionary (Hashing)
#Longest Harmonious Subsequence (LeetCode 594)
def findLHS(nums):
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    longest = 0
    for num in d:
        if num + 1 in d:
            longest = max(longest, d[num] + d[num + 1])
    return longest
nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print("Length of the longest harmonious subsequence is:", result)

#*************************************************************************************************************