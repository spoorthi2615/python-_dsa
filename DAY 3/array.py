# # 2.1) missing number
# # Given an array nums containing n distinct numbers in the range [0, n],
# #  return the only number in the range that is missing from the array.
# def missingNumber(nums):
#     n = len(nums)
#     total = n * (n + 1) // 2

#     for num in nums:
#         total -= num

#     return total

# nums = [0, 1, 2, 4]      # Define nums first
# missing = missingNumber(nums)

# print(missing)

# #*************************************************************************************************************

# # 2.2)decode XOREd Array
# # Given an array of integers encoded, where encoded[i] = arr[i] XOR arr[i + 1].
# # You are also given an integer first, that is the value of arr[0]. 
# # Return the original array arr. It can be proved that the answer exists and is unique.
# def decode(encoded, first):
#     n = len(encoded)
#     arr = [0] * (n + 1) # Create an array of size n+1 to store the original array
#     arr[0] = first # Set the first element of the original array to the given first value

#     for i in range(n): # Iterate through the encoded array
#         arr[i + 1] = arr[i] ^ encoded[i] # Use XOR to decode the next element of the original array

#     return arr
# encoded = [1, 2, 3]
# first = 1   
# original_array = decode(encoded, first)
# print(original_array)

# #*************************************************************************************************************

# #2.3) plus one
# # Given a non-empty array of decimal digits representing a non-negative integer, 
# # increment one to the integer. 
# # The digits are stored such that the most significant digit is at the head of the list, 
# # and each element in the array contains a single digit.
# #  You may assume the integer does not contain any leading zero, except the number 0 itself.
# def plusOne(digits):
#     n = len(digits)

#     for i in range(n - 1, -1, -1):
#         if digits[i] < 9:
#             digits[i] += 1
#             return digits
#         else:
#             digits[i] = 0

#     return [1] + digits

# digits = [9, 9, 9]
# result = plusOne(digits)

# print(result)

# #*************************************************************************************************************

#2.4) best time to buy and sell stock (leetcode question-121)
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
def maxProfit(prices):
    min_price = float('inf') # Initialize min_price to infinity to ensure any price will be lower
    max_profit = 0 # Initialize max_profit to 0

    for price in prices: # Iterate through the list of prices
        if price < min_price: # If the current price is less than the minimum price found so far, update min_price
            min_price = price
        elif price - min_price > max_profit: # If the profit from selling at the current price is greater than the max_profit found so far, update max_profit
            max_profit = price - min_price

    return max_profit
prices = [7, 1, 5, 3, 6, 4]
profit = maxProfit(prices)
print(profit)

#*************************************************************************************************************






