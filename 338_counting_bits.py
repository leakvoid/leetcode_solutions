class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            bin_num = bin(num)
            count = 0
            
            for bit in bin_num:
                if bit == '1':
                    count += 1
            
            res.append(count)
        
        return res
