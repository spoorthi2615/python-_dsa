#845

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        longest = 0

        for i in range(1, n - 1):
            # Check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:

                left = i
                right = i

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                longest = max(longest, right - left + 1)

        return longest