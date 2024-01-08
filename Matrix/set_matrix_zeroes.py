"""
Problem 73 From Top 150 Interview: Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, 
set its entire row and column to 0's.

You must do it in place.
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns
        first_row = matrix[0] # first row of the matrix
        first_column = [matrix[j][0] for j in range(m)] # first column of the matrix

        # iterate over the entire matrix
        for i in range(m): 
            for j in range(n):
                if matrix[i][j] == 0: # if the value of this element is 0
                    first_row[j] = 0 # record it in the first row of the matrix
                    first_column[i] = 0 # and also in the first column of the matrix

        # iterate over the first row 
        for i in range(n):
            if first_row[i] == 0: # if the value is zero
                for j in range(m): # set the entire row to zero
                    matrix[j][i] = 0

        # iterate over the first column 
        for i in range(m):
            if first_column[i] == 0: # if the value is zero
                for j in range(n): # set the entire column to zero
                    matrix[i][j] = 0