"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

 

Constraints:

    1 <= s.length <= 3 * 105
    s consists of digits, '+', '-', '(', ')', and ' '.
    s represents a valid expression.
    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.

"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0 # what we have computed so far
        cur_num = 0 # what we are currently computing
        sign = 1 # the sign of what we are currently computing
        stack = [] # stack to store both what we have computed so far along with its sign
        for c in s:
            if c.isdigit(): # char is digit
                cur_num = cur_num * 10 + int(c) # add to what we are currently computing
            elif c in '+-': # char is + or -
                output += (cur_num * sign) # take whatever we what we are currently computing and add it what we have computed so far
                cur_num = 0 # reset what we are currently computing to 0
                if c =='-': # in the case where the char is -
                    sign = -1 # the sign of what we are currently computing should be negative
                else: # otherwise
                    sign = 1 # the sign should be positive
            elif c == '(': # char is an open parenthesis
                stack.append(output) # push what we have computed so far to the stack
                stack.append(sign) # along with the sign of what we are currently computing
                output = 0 # reset what we have computed so far to 0
                sign = 1 # reset the sign as well
            elif c == ')': # char is a closed parenthesis
                output += (cur_num * sign) # take whatever we are currently computing, multiply it by the current sign
                                           # and add it to the final result
                output *= stack.pop() # multiply the final result by the sign on top of the stack 
                                      # that we pushed when opening the parenthesis
                output += stack.pop() # add the result that we pushed earlier when we opened the parenthesis to our final result
                cur_num = 0 # reset whatever we are currently computing to zero
                
        # since we either finalize the output with ')' or '+-', 
        # we have to incomporate any result we were currently computing in the final result
        return output + (cur_num * sign) 
            

""" 
Credits: Timothy H Chang

https://youtu.be/A3noAzWZ9f4

"""