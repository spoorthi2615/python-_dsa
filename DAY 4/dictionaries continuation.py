# # dictionaries continuation
# #1.1) roman to integer
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_numerals = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
#         total = 0
#         prev_value = 0
        
#         for char in s:
#             value = roman_numerals[char]
#             if prev_value < value:
#                 total += value - 2 * prev_value
#             else:
#                 total += value
#             prev_value = value
        
#         return total
# # Example usage:
# solution = Solution()
# print(solution.romanToInt("III"))  
# print(solution.romanToInt("IV"))    

# #********************************************************************************************

# #1.2) majority element
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {}
#         for num in nums:
#             if num in count:
#                 count[num] += 1
#             else:
#                 count[num] = 1
        
#         majority_count = len(nums) // 2
#         for num, freq in count.items():
#             if freq > majority_count:
#                 return num
# # Example usage:
# solution = Solution()
# print(solution.majorityElement([3, 2, 3]))

# #********************************************************************************************

# #1.3) unique occurences
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         count = {}
#         for num in arr:
#             if num in count:
#                 count[num] += 1
#             else:
#                 count[num] = 1
        
#         occurrences = set()
#         for freq in count.values():
#             if freq in occurrences:
#                 return False
#             occurrences.add(freq)
        
#         return True
# # Example usage:
# solution = Solution()
# print(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))

# #********************************************************************************************

# #1.4)k-diff pairs in an array
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         if k < 0:
#             return 0
        
#         count = {}
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
        
#         pairs = 0
#         for num in count:
#             if k == 0:
#                 if count[num] > 1:
#                     pairs += 1
#             else:
#                 if num + k in count:
#                     pairs += 1
        
#         return pairs
# # Example usage:
# solution = Solution()
# print(solution.findPairs([3, 1, 4, 1, 5], 2))

# #********************************************************************************************

# #1.5)find pairs in an array 
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         if k < 0:
#             return 0
        
#         count = {}
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
        
#         pairs = 0
#         for num in count:
#             if k == 0:
#                 if count[num] > 1:
#                     pairs += 1
#             else:
#                 if num + k in count:
#                     pairs += 1
        
#         return pairs
# # Example usage:
# solution = Solution()
# print(solution.findPairs([3, 1, 4, 1, 5], 2))

#********************************************************************************************

#1.6)number of good pairs
def numIdenticalPairs(nums):
    count = {}
    good_pairs = 0
    
    for num in nums:
        if num in count:
            good_pairs += count[num]  # Each existing occurrence of num forms a good pair with the current num
            count[num] += 1
        else:
            count[num] = 1
    
    return good_pairs


#********************************************************************************************

#1.7) find the maximu distance between the same elements in an array
class Solution:
    def max_distance(self, nums):
        index_map = {}
        max_dist = 0
        
        for i, num in enumerate(nums):
            if num in index_map:
                dist = i - index_map[num]
                max_dist = max(max_dist, dist)
            else:
                index_map[num] = i
        
        return max_dist

#********************************************************************************************

#1.8) degree of an array
class Solution:
    def find_shortest_sub_array(self, nums):
        count = {}
        first_index = {}
        last_index = {}
        
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = 0
                first_index[num] = i
            count[num] += 1
            last_index[num] = i
        
        degree = max(count.values())
        min_length = float('inf')
        
        for num, freq in count.items():
            if freq == degree:
                length = last_index[num] - first_index[num] + 1
                min_length = min(min_length, length)
        
        return min_length
    
        

