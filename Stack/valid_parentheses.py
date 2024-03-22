"""
Problem 20 from Top Interview 150: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) <= 0:
                    return False
                popped_ele = stack.pop()
                if popped_ele !=  '(' and s[i] == ')':
                    return False
                if popped_ele !=  '[' and s[i] == ']':
                    return False
                if popped_ele !=  '{' and s[i] == '}':
                    return False

        return len(stack) == 0
    