class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ten_dict = {}
        
        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            if seq in ten_dict:
                ten_dict[seq] += 1
            else:
                ten_dict[seq] = 1
                
        res = []
        for seq in ten_dict:
            if ten_dict[seq] > 1:
                res.append(seq)
        return res
