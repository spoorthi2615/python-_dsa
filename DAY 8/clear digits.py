#You are given a string s.
# Your task is to remove all digits by doing this operation repeatedly:
# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.
# Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.
def clearDigits(s):
    stack = []
    
    for char in s:
        if char.isdigit():
            if stack:
                stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)
