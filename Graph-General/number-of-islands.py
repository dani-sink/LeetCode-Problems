"""
Problem 200 from Top 150 Interview: Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""

from collections import deque

class Solution(object):

    def bfs(self, r, c, visited, grid):
        ROWS, COLS = len(grid), len(grid[0]) # record the number of rows and columns of the grid
        q = deque() # create a Queue data structure
        visited.add((r, c)) # add the current cell in the visited Set
        q.append((r, c)) # add the current cell to the queue as well

        while q: # while the queue is not empty
            row, col = q.popleft() # pop from the queue to get the coordinates of the next cell in the queue
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # potential directions for the neighbor of the above cell
            for drow, dcol in directions: # we look at each direction
                r, c = row + drow, col + dcol # the indexes of the potential neighbors of the current cell
                if (0 <= r < ROWS and 0 <= c < COLS and # if the coordinates of the neighbor are valid, the neighbor is
                 (r, c) not in visited and grid[r][c] == '1'): # not in the visited Set and the neighbor is a piece of land
                    q.append((r, c)) # append the neighbor to the queue
                    visited.add((r, c)) # also add the neighbor to the visited Set


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: # check to see if the grid is empty
            return 0 

        ROWS, COLS = len(grid), len(grid[0]) # record the number of rows and columns of the grid
        visit = set() # keep track of the visited cells in a Set data structure
        islands = 0 # we use it to record the number of islands encountered so far

        for row in range(ROWS): # Iterate over the rows in the outer loop
            for col in range(COLS): # Iterate over the columns in the inner loop
                if grid[row][col] == '1' and (row, col) not in visit: # if the grid cell is a land cell and has not yet been visited
                    self.bfs(row, col, visit, grid) # start a breadth first search from this cell
                    islands += 1 # increment the number of islands
                    # The bfs updates the visited cells set such that we don't perform bfs again on an already visited cell in the grid
        return islands # Once we checked all nodes, we return the total number of islands we recorded