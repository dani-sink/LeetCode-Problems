"""
Problem 13 from Top Interview 150: Integer To Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, 
the numeral for four is not IIII. Instead, the number four is written as IV. Because 
the one is before the five we subtract it making four. The same principle applies to 
the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str_to_build = ""
        while num > 0:
            if num - 1000 >= 0:
                str_to_build += "M"
                num -= 1000
            elif num - 900 >= 0:
                str_to_build += "CM"
                num -= 900
            elif num - 500 >= 0:
                str_to_build += "D"
                num -= 500
            elif num - 400 >= 0:
                str_to_build += "CD"
                num -= 400
            elif num - 100 >= 0:
                str_to_build += "C"
                num -= 100
            elif num - 90 >= 0:
                str_to_build += "XC"
                num -= 90
            elif num - 50 >= 0:
                str_to_build += "L"
                num -= 50
            elif num - 40 >= 0:
                str_to_build += "XL"
                num -= 40
            elif num - 10 >= 0:
                str_to_build += "X"
                num -= 10
            elif num - 9 >= 0:
                str_to_build += "IX"
                num -= 9
            elif num - 5 >= 0:
                str_to_build += "V"
                num -= 5
            elif num - 4 >= 0:
                str_to_build += "IV"
                num -= 4
            else:
                str_to_build += "I"
                num -= 1
        return str_to_build