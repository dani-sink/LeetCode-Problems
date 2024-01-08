"""
Problem 125 from Top Interview 150: Valid Palindrome

A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        all_alpha = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                if char.isupper():
                    all_alpha += char.lower()
                else:
                    all_alpha += char
        n = len(all_alpha)
        pointer1 = 0
        pointer2 = n - 1
        while pointer1 <= pointer2:
            if all_alpha[pointer1] != all_alpha[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1
        return True