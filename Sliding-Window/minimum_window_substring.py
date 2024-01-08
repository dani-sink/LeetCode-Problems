"""
Problem 76 from Top Interview 150: Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s) # length of s
        n = len(t) # length of t
        if m < n: # if the length of s is less t's length
            return "" # there is no minimum window substring, so return ""
        left, right = 0, 0 # set left and right pointers to 0
        window = ""  # window is initially empty
        result = ""  # where we will store the minimum window substring 
        window_len = 10**6 # set the window length to a very high value inially

        # dictionaries to keep track of the count of characters for t and the current
        # window
        main_dict, cur_dict = {}, {} 
        for string in t: 
            if string in main_dict:
                main_dict[string] += 1
            else:
                main_dict[string] = 1
        # 'have' stores the number of characters we have so far and 'need' 
        # stores the number of characters we need in total
        have, need = 0, sum(main_dict.values())
        
        for i in range(m): # iterate over s
            right += 1 # move right pointer to the right at each iteration
            if s[i] in main_dict: # if current character is in the string t
                if s[i] in cur_dict: # if current character is already in the current dictionary
                    if main_dict[s[i]] > cur_dict[s[i]]: # check if we need this character to build the substring
                        have += 1  # if we do need it, we increment have by 1
                    # otherwise, we don't need it and we don't increment have
                    cur_dict[s[i]] += 1 # we increment the count of the character in the current dictionary
                else: # if current character is not in the current dictionary
                    cur_dict[s[i]] = 1 # add it
                    have += 1 # increment 'have' by 1
            if have == need: # if the current window has all the characters we need
                window = s[left:right] # get the window
                if len(window) < window_len: # if the length of the window is lower than the current window length
                    result = window # update the minimum window substring
                    window_len = len(window) # update the length
                for element in window: # for each character of the window
                    if have < need: # check if the current window doesn't have all the characters we need
                        break # if so, exit the loop
                    if element in main_dict: # otherwise, check if the current window character is in t
                        # if it is but we already have enough of this character to build the substring
                        if cur_dict[element] > main_dict[element] : 
                            cur_dict[element] -= 1 # simply decrement its count in the current dictionary
                        else: # otherwise, we do need this window character
                            have -= 1 # thus, decrease 'have' since we are moving the left pointer
                            cur_dict[element] -= 1 # also decrement its count in the current dictionary
                    left += 1 # we move left pointer until window is no longer valid, at which point we will exit the loop

                # if the loop exited during execution, it means the last character we checked was needed to build the 
                # mininum window substring.
                window = s[left-1:right] # following that logic, we decrease left pointer by 1 to include it in the window
                if len(window) < window_len: # we check if the length of the window is lower than the current window length
                    result = window # update the minimum window substring
                    window_len = len(window) # update the length
                    
        return result