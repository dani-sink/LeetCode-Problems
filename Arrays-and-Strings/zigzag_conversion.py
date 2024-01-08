"""
Problem 6 from Top Interview 150: Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        dictionary = {}
        for i in range(1, numRows+1):
            dictionary[i] = ""
        cur_row = 1
        n = len(s)
        increment = True
        for i in range(n):
            if cur_row == 1:
                dictionary[cur_row] += s[i]
                cur_row += 1
                increment = True
            elif cur_row == numRows:
                dictionary[cur_row] += s[i]
                cur_row -= 1
                increment = False
            else:
                if cur_row > numRows:
                    cur_row -= 1
                    dictionary[cur_row] += s[i]
                    cur_row -= 1 
                elif cur_row < 1:
                    cur_row += 1
                    dictionary[cur_row] += s[i]
                    cur_row += 1 
                elif increment is True:
                    dictionary[cur_row] += s[i]
                    cur_row += 1
                elif increment is False:
                    dictionary[cur_row] += s[i]
                    cur_row -= 1
        str_to_build = ''.join(dictionary.values())
        return str_to_build