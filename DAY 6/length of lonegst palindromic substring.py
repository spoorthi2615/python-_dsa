#length of longest palindromic substring
def longestPalindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = 0
    max_length = 1

    for i in range(len(s)):
        len1 = expand_around_center(i, i)      # Odd length palindrome
        len2 = expand_around_center(i, i + 1)  # Even length palindrome
        length = max(len1, len2)

        if length > max_length:
            max_length = length
            start = i - (length - 1) // 2

    return s[start:start + max_length]
