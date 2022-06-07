class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            found_digits = set()
            for e in row:
                if e in found_digits:
                    return False
                elif e != '.':
                    found_digits.add(e)
                    
        for column_idx in range(9):
            found_digits = set()
            for row_idx in range(9):
                e = board[row_idx][column_idx]
                if e in found_digits:
                    return False
                elif e != '.':
                    found_digits.add(e)
        
        for r_box_idx in range(0, 9, 3):
            for c_box_idx in range(0, 9, 3):
                found_digits = set()
                for r_box_shift in range(3):
                    for c_box_shift in range(3):
                        e = board[r_box_idx + r_box_shift][c_box_idx + c_box_shift]
                        if e in found_digits:
                            return False
                        elif e != '.':
                            found_digits.add(e)
                            
        return True
