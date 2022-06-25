class Solution:
    def rec_permute(self, res, tail, head):
        if len(head) == 1:
            tail.append(head[0])
            res.append(tail)
            return
        
        for i in range(len(head)):
            new_tail = tail.copy()
            new_tail.append(head[i])
            
            self.rec_permute(res, new_tail, head[:i] + head[i+1:])
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.rec_permute(res, [], nums)
        return res
