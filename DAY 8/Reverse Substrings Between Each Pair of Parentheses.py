#You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any bracketes.
def reverseParentheses(s):
    stack = []
    for char in s:
        if char == ')':
            temp = ""
            while stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()  # Remove the '('
            stack.extend(temp)  # Add the reversed substring back to the stack
        else:
            stack.append(char)
    
    return ''.join(stack)[::-1]

print(reverseParentheses("u(love)i"))
