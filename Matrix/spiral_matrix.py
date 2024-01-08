"""
Problem 54 From Top 150 Interview: Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        have = 0  # number of values we currently have
        need = len(matrix) * len(matrix[0]) # number of values we need
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns
        i, j = 0, 0
        matrix_ele = []
        # initial positions of the first and last row, and of the first and last columns
        last_row, first_row, last_column, first_column = m - 1, 0, n - 1, 0 
        # directions to know where to iterate in the matrix
        directions = [[1,0],[0,1],[-1,0],[0,-1]] # down, right, up, left
        cur_dir = [0,1] # the current direction we iterate, initially set to the right direction
        while have < need: # while we don't have the necessary number of elements
            if cur_dir == [0,1]: # If we are currently moving right
                if j == last_column: # If we are at the last column
                    matrix_ele.append(matrix[i][j]) # Append current element to the matrix
                    have += 1  # we increment the have counter
                    cur_dir = [1,0] # we set the new direction to iterate, which is down.
                    i += cur_dir[0] # update i
                    j += cur_dir[1] # update j
                    first_row += 1 # since the entire row has already been visited, we set the bound to be the row below it
                else: # If we are not at the last column
                    matrix_ele.append(matrix[i][j]) # Append current element to the matrix
                    have += 1 # we increment the have counter
                    i += cur_dir[0] # update i
                    j += cur_dir[1] # update j
        # We repeat the same process for the down, left and up directions
            elif cur_dir == [1,0]: # down
                if i == last_row:
                    matrix_ele.append(matrix[i][j])
                    have += 1
                    cur_dir = [0,-1] # we set the new direction to iterate, which is left.
                    i += cur_dir[0]
                    j += cur_dir[1]
            # since the entire column has already been visited, we set the bound to be the column before it
                    last_column -= 1 
                else:
                    matrix_ele.append(matrix[i][j])
                    have += 1
                    i += cur_dir[0]
                    j += cur_dir[1]
            elif cur_dir == [0,-1]: # left
                if j == first_column:
                    matrix_ele.append(matrix[i][j])
                    have += 1
                    cur_dir = [-1,0] # we set the new direction to iterate, which is up.
                    i += cur_dir[0]
                    j += cur_dir[1]
                    # since the entire row has already been visited, we set the bound to be the row above it
                    last_row -= 1
                else:
                    matrix_ele.append(matrix[i][j])
                    have += 1
                    i += cur_dir[0]
                    j += cur_dir[1]
            elif cur_dir == [-1,0]: # up
                if i == first_row:
                    matrix_ele.append(matrix[i][j])
                    have += 1
                    cur_dir = [0,1] # we set the new direction to iterate, which is right.
                    i += cur_dir[0]
                    j += cur_dir[1]
                    # since the entire column has already been visited, we set the bound to be the column in front of it
                    first_column += 1
                else:
                    matrix_ele.append(matrix[i][j])
                    have += 1
                    i += cur_dir[0]
                    j += cur_dir[1]
        
        return matrix_ele