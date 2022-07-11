class Solution:
    def available_path(self, coord, travel_arr):
        return False if coord in travel_arr else True
    
    def exist_rec(self, board, word, l_pos, travel_arr):
        if l_pos == len(word) - 1:
            return True
        l_pos += 1
        
        l_row = travel_arr[-1][0]
        l_col = travel_arr[-1][1]
        coord = []
        if l_row < len(board) - 1:
            coord.append([l_row + 1, l_col])
        if l_row > 0:
            coord.append([l_row - 1, l_col])
        if l_col < len(board[0]) - 1:
            coord.append([l_row, l_col + 1])
        if l_col > 0:
            coord.append([l_row, l_col - 1])
        
        for i in range(len(coord)):
            if word[l_pos] == board[coord[i][0]][coord[i][1]] and self.available_path(coord[i], travel_arr):
                new_travel_arr = travel_arr.copy() # boolean matrix can be alternatively used with travel_matrix[l_row][l_col] = True before 'for' loop and travel_matrix[l_row][l_col] = False after; see 79_tmp
                new_travel_arr.append(coord[i])
                if self.exist_rec(board, word, l_pos, new_travel_arr):
                    return True
        return False

    def check_word(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and self.exist_rec(board, word, 0, [[row, col]]):
                    return True
        return False

    def check_substring(self, board, word, memory):
        if word in memory:
            return True

        if len(word) > 1:
            mid = len(word) // 2
            if self.check_substring(board, word[:mid], memory) == False:
                return False
            if self.check_substring(board, word[mid:], memory) == False:
                return False

        if self.check_word(board, word):
            memory.add(word)
            return True
        else:
            return False

    def exist(self, board: [[str]], word: str) -> bool:
        memory = set()
        return self.check_substring(board, word, memory)

s = Solution()
print(s.exist([["a","a"]], "aaa"))
print(s.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB"))
print(s.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], "AAAAAAAAAAAAABB"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(s.exist([["C"]], "D"))
print(s.exist([["C"]], "C"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "CEZ"))
