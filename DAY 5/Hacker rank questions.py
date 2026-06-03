#1.1) First Element With Unique Frequency    
#Given a list of integers, determine the first element whose frequency is unique.
#A frequency is considered unique if no other element in the list has the same frequency.
#If multiple elements have unique frequencies, print the one that appears first in the list.
#If no such element exists, print -1.
def first_unique_frequency(arr):
    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    freq_count = {}

    for freq in frequency.values():
        freq_count[freq] = freq_count.get(freq, 0) + 1

    for num in arr:
        if freq_count[frequency[num]] == 1:
            return num

    return -1


arr = [1, 2, 2, 3, 3, 3, 4]
print(first_unique_frequency(arr))

#*******************************************************************************************************

# 1.2) Given a list of integers, find the first element such that: frequency(current_element) > sum of frequencies of all DISTINCT elements appearing after it
# Input Format
# A Python list of integers.
# Constraints
# 1 <= len(nums) <= 10^5
# Output Format
# Print the required element. If none exists, print -1
def first_element_with_greater_frequency(nums):
    from collections import Counter
    
    frequency = Counter(nums)
    total_distinct = len(set(nums))
    
    for i, num in enumerate(nums):
        current_freq = frequency[num]
        remaining_distinct = total_distinct - 1
        
        if current_freq > remaining_distinct:
            return num
        
        frequency[num] -= 1
        if frequency[num] == 0:
            total_distinct -= 1
    
    return -1
nums = [1, 2, 2, 3, 3, 3, 4]
print(first_element_with_greater_frequency(nums))

#*******************************************************************************************************




