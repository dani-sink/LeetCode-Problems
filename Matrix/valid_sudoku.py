"""
Problem 36 From Top 150 Interview: Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    
    2. Each column must contain the digits 1-9 without repetition.
    
    3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_sets = [] # hash sets for each row
        column_sets = [] # hash sets for each column
        flipped_board = [list(row) for row in zip(*board)] # flip the board to get the columns
        all_3x3_sub_boards = [] # where we store all the 3x3 sub-boards
        all_3x3_sub_boards_sets = [] # hash sets for each 3x3 sub-board

        # get all the 3x3 sub-boards
        for i in range(0, 9, 3): 
            for j in range(0,9,3):
                sub_board = [row[j:j+3] for row in board[i:i+3]]
                all_3x3_sub_boards.append(sub_board)

        # get the hash sets for each 3x3 sub-board
        for sub_board in all_3x3_sub_boards: 
            cur_dict = {}
            for row in sub_board:
                for num in row:
                    if num in cur_dict:
                        cur_dict[num] += 1
                    else:
                        cur_dict[num] = 1
            all_3x3_sub_boards_sets.append(cur_dict)

        # get the hash sets for each row of the board
        for row in board:
            cur_dict = {}
            for num in row:
                if num in cur_dict:
                    cur_dict[num] += 1
                else:
                    cur_dict[num] = 1
            row_sets.append(cur_dict)
        
        # get the hash sets for each column of the board
        for row in flipped_board:
            cur_dict = {}
            for num in row:
                if num in cur_dict:
                    cur_dict[num] += 1
                else:
                    cur_dict[num] = 1
            column_sets.append(cur_dict)
        
        # iterate over each key, value pair of the row hash sets
        for dict_set in row_sets:
            for key, value in dict_set.items():
                if key == '.': # skip the empty keys
                    continue
                if value > 1: # check if the value of the key is greater than 1
                    return False # if it is, then there is repetition of at lest one value, thus return False

        # iterate over each key, value pair of the column hash sets           
        for dict_set in column_sets: 
            for key, value in dict_set.items():
                if key == '.': # skip the empty keys
                    continue
                if value > 1: # check if the value of the key is greater than 1
                    return False # if it is, then there is repetition of at lest one value, thus return False

        # iterate over each key, value pair of the 3x3 sub-boards hash sets 
        for dict_set in all_3x3_sub_boards_sets:
            for key, value in dict_set.items():
                if key == '.':  # skip the empty keys
                    continue
                if value > 1:  # check if the value of the key is greater than 1
                    return False # if it is, then there is repetition of at lest one value, thus return False

        # If board passed all the checks, then it is valid, thus return True
        return True