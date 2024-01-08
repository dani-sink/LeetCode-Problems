"""
Problem 289 From Top 150 Interview: Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a 
cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an 
initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):

    1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
    
    2. Any live cell with two or three live neighbors lives on to the next generation.
    
    3. Any live cell with more than three live neighbors dies, as if by over-population.
    
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the 
current state, where births and deaths occur simultaneously. Given the current state of the 
m x n grid board, return the next state.
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        m = len(board) # number of rows
        n = len(board[0]) # number of columns
        
        directions = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]] # all directions to get all neighbors
        board_copy = []

        # We create a copy of the board
        for i in range(m):
            row = []
            for j in range(n):
                row.append(board[i][j])
            board_copy.append(row)

        # We iterate over the copy
        for i in range(m):
            for j in range(n):
                live = 0 # stores the number of live neighbors of the current cell
                valid_neighbor_pos = [] # stores the positions of the neighbors of the current cell
                for direction in directions: # for each direction
                    neighbor_i = i + direction[0] # compute x coordinate of neighbor position
                    neighbor_j = j + direction[1] # compute y coordinate of neighbor position
                    # if the position is valid
                    if (0 <= neighbor_i and neighbor_i < m) and (0 <= neighbor_j and neighbor_j < n):
                        valid_neighbor_pos.append([neighbor_i, neighbor_j]) # add neighbor position to the list
                for pos in valid_neighbor_pos: # for each position in the list
                    if board_copy[pos[0]][pos[1]] == 1: # if the neighbor at that position is alive
                        live += 1 # increment the number of live neighbors
                if board_copy[i][j] == 1: # If the current cell is alive
                    if live < 2: # If it has fewer than two live neighbors
                        board[i][j] = 0 # it dies in the next generation, so set the entry on the real board to 0
                    elif live == 2 or live == 3: # else if it has two or three live neighbors
                        board[i][j] = 1 # it lives on to the next generation, so set the entry on the real board to 1
                    else: # otherwise
                        board[i][j] = 0 # it dies in the next generation, so set the entry on the real board to 0
                else: # If the current cell is dead
                    if live == 3: # If it has exactly 3 neighbors that are alive
                        board[i][j] = 1 # the cell becomes a live cell, so set the entry on the real board to 1