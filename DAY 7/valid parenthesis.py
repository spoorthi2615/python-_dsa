#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def validParentheses(s: str) -> bool:
    class Solution(object):
        def isValid(self, s):
            stack = []

            for ch in s:
                if ch in "([{":
                    stack.append(ch)

                else:
                    if not stack:
                        return False

                    top = stack.pop()
   
                    if ch == ')' and top != '(':
                        return False
                    if ch == '}' and top != '{':
                        return False
                    if ch == ']' and top != '[':
                        return False

            return len(stack) == 0

