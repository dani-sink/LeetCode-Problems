"""
Problem 383 From Top 150 Interview: Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote 
can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}

        # Create magazine dictionary
        for char in magazine:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1

        # Create ransomNote dictionary
        for char in ransomNote:
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1
        
        # Iterate ransomNote dictionary
        for key, value in dict2.items():
            if key in dict1: # if the character in ransomNote is in magazine
                if value > dict1[key]: # If its count is more than its count in magazine
                    return False # There is not enough chracters in magazine, so return false
            else: # if the character in ransomNote is not in magazine
                return False # The character can't be built from the characters of magazine, so return false

        # If all those tests pass, then there is enough of each character in magazine to build ransomNote
        # so return True
        return True