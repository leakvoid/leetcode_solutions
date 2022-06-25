class Solution:
    def get_awailable_positions(self, n, queen_pos):
        res = [True] * n
        for i in range(len(queen_pos)):
            res[queen_pos[i]] = False
            l_diagonal_col = queen_pos[i] - len(queen_pos) + i
            if l_diagonal_col >= 0:
                res[l_diagonal_col] = False
            r_diagonal_col = queen_pos[i] + len(queen_pos) - i
            if r_diagonal_col < n:
                res[r_diagonal_col] = False
        return res
    
    def solve_rec(self, res, n, queen_pos):
        if len(queen_pos) == n:
            res.append(queen_pos)
        else:
            ap = self.get_awailable_positions(n, queen_pos)
            
            for i in range(len(ap)):
                if ap[i] == True:
                    new_queen_pos = queen_pos.copy()
                    new_queen_pos.append(i)
                    self.solve_rec(res, n, new_queen_pos)
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.solve_rec(res, n, [])
        
        res_format = []
        for qp in res:
            form = []
            for i in qp:
                s = '.' * i + 'Q' + '.' * (n - i - 1)
                form.append(s)
            res_format.append(form)
        return res_format
