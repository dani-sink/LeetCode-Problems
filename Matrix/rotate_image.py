"""
Problem 48 From Top 150 Interview: Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D 
matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 1. Find the matrix transpose
        for i in range(n):
            for j in range(i+1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # 2. Reverse each row of the matrix
        for row in matrix:
            start = 0
            end = n - 1
            while start < end:
                temp = row[start]
                row[start] = row[end]
                row[end] = temp
                start += 1
                end -= 1
