#dictionaries continuation
#roman to integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        
        for char in s:
            value = roman_numerals[char]
            if prev_value < value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value
        
        return total
# Example usage:
solution = Solution()
print(solution.romanToInt("III"))  
print(solution.romanToInt("IV"))    

#********************************************************************************************

# majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        majority_count = len(nums) // 2
        for num, freq in count.items():
            if freq > majority_count:
                return num
# Example usage:
solution = Solution()
print(solution.majorityElement([3, 2, 3]))

#********************************************************************************************

#unique occurences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        occurrences = set()
        for freq in count.values():
            if freq in occurrences:
                return False
            occurrences.add(freq)
        
        return True
# Example usage:
solution = Solution()
print(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))

#********************************************************************************************
#k-diff pairs in an array
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        pairs = 0
        for num in count:
            if k == 0:
                if count[num] > 1:
                    pairs += 1
            else:
                if num + k in count:
                    pairs += 1
        
        return pairs
# Example usage:
solution = Solution()
print(solution.findPairs([3, 1, 4, 1, 5], 2))

#********************************************************************************************
