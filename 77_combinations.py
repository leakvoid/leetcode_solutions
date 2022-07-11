class Solution:
    def combine_rec(self, res, start, end, head, tail_len):
        tail_len -= 1
        for e in range(start, end - tail_len + 1):
            new_head = head.copy()
            new_head.append(e)
            if tail_len > 0:
                self.combine_rec(res, e + 1, end, new_head, tail_len)
            else:
                res.append(new_head)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.combine_rec(res, 1, n, [], k)
        return res
