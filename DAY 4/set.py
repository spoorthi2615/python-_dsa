#1.1) contains duplicate values
class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
#*************************************************************************************************************************

#1.2) happy number
class Solution:
    def isHappy(self, n):
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                total_sum += digit ** 2
                number //= 10
            return total_sum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1
    
#*************************************************************************************************************************

#1.3) longest consecutive sequence
class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
