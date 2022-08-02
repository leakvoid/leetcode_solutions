class Solution:
    def combination_rec(self, start, k, tail, target, res):
        if target <= 0:
            return
        
        if k == 1:
            if target >= start and target <= 9:
                new_tail = list(tail)
                new_tail.append(target)
                res.append(new_tail)
            return
        
        for n in range(start, 11 - k):
            tail.append(n)
            self.combination_rec(n + 1, k - 1, tail, target - n, res)
            tail.pop()
            
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.combination_rec(1, k, list(), n, res)
        return res
