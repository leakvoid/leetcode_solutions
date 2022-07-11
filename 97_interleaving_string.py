class Solution:
    def interleave_rec(self, s1, s2, s3, s1_i, s2_i):
        if s2_i in self.memory[s1_i]:
            return False
        self.memory[s1_i].add(s2_i)
        
        while s1_i < len(s1) and s2_i < len(s2):
            s3_i = s1_i + s2_i
            if s1[s1_i] == s3[s3_i]:
                if s1[s1_i] == s2[s2_i]:
                    res = self.interleave_rec(s1, s2, s3, s1_i + 1, s2_i) or self.interleave_rec(s1, s2, s3, s1_i, s2_i + 1)
                    return res
                else:
                    s1_i += 1
            elif s2[s2_i] == s3[s3_i]:
                s2_i += 1
            else:
                return False

        while s1_i < len(s1):
            if s1[s1_i] != s3[s1_i + s2_i]:
                return False
            s1_i += 1

        while s2_i < len(s2):
            if s2[s2_i] != s3[s1_i + s2_i]:
                return False
            s2_i += 1
        
        return True
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        self.memory = {}
        for i in range(len(s1) + 1):
            self.memory[i] = set()
        
        res = self.interleave_rec(s1, s2, s3, 0, 0)
        return res

s = Solution()
print(s.isInterleave("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(s.isInterleave("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(s.isInterleave("xyxya", "xyxyxyb", "xyxyxyxyaxyb"))
print(s.isInterleave("xyxyb", "xyxyxya", "xyxyxyxyaxyb"))
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(s.isInterleave("c", "ca", "cac"))
print(s.isInterleave("aabccaabcc", "aabcc", "aabccaabccaabcc"))
print(s.isInterleave("ab", "aa", "abaa"))
print(s.isInterleave("ab", "aa", "aaba"))
print(s.isInterleave("aabc", "abad", "aabacbad"))
print(s.isInterleave("aabaac", "aadaaeaaf", "aadaaeaabaafaac"))
print(s.isInterleave("aacaac", "aacaaeaac", "aacaacaaeaacaac"))
print(s.isInterleave("abababababababababababababababababababababababababababababababababababababababababababababababababbb", "babababababababababababababababababababababababababababababababababababababababababababababababaaaba", "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababbb"))
