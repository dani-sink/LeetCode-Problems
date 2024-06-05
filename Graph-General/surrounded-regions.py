"""
Problem 130 from Top 150 Interview: Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.

"""

class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board: # if there is no board
            return # return
        ROWS, COLS = len(board), len(board[0]) # record the number of rows and columns

        # Utility function to traverse a cell of the board in a depth-first search manner
        def boundaryDFS(grid, i, j):
            if i >= ROWS or i < 0 or j >= COLS or j < 0: # if we went beyond the boundaries of the grid
                return # return
            
            if grid[i][j] == 'O': # if the current cell is a O
                grid[i][j] = '*' # mark it as *
            
            if i > 0 and grid[i - 1][j] == 'O': # if the left neighbor of the current cell is a O and the current cell is not at the first row
                boundaryDFS(grid, i - 1, j) # recursively go through that neighbor 

            if i < ROWS - 1 and grid[i + 1][j] == 'O': # if the right neighbor of the current cell is a O and the current cell is not at the last row
                boundaryDFS(grid, i + 1, j) # recursively go through that neighbor

            if j > 0 and grid[i][j - 1] == 'O': # if the top neighbor of the current cell is a O and the current cell is not at the first column
                boundaryDFS(grid, i, j - 1) # recursively go through that neighbor

            if j < COLS - 1 and grid[i][j + 1] == 'O': # if the bottom neighbor of the current cell is a O and the current cell is not at the last column
                boundaryDFS(grid, i, j + 1) #  recursively go through that neighbor

        for i in range(ROWS): # we go though each row
            if board[i][0] == 'O': # if the cell is a O and it is on the first column
                boundaryDFS(board, i, 0) # start DFS from that cell
            if board[i][COLS-1] == 'O': # if the cell is a O and it is the last column
                boundaryDFS(board, i, COLS-1) # start DFS from that cell
            
        for j in range(COLS): # we go though each column
            if board[0][j] == 'O': # if the cell is a O and it is on the first row
                boundaryDFS(board, 0, j) # start DFS from that cell
            if board[ROWS-1][j] == 'O': # if the cell is a O and it is the last row
                boundaryDFS(board, ROWS-1, j)  # start DFS from that cell

        for i in range(ROWS): # iterate through each cell
            for j in range(COLS):
                if board[i][j] == 'O': # if the cell is a O
                    board[i][j] = 'X' # turn it into a X
                elif board[i][j] == '*': # else if the cell is a *, then it was a previous O that was marked because it was connected to an invalid O
                    board[i][j] = 'O' # return it into a O

                # Otherwise, leave the cell as is