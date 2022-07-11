class Solution:
    def decode(self, s, start):
        if start in self.memory:
            return self.memory[start]
        
        if start == len(s):
            return 1
        
        count = 0
        if s[start] == "0":
            return 0
        elif (s[start] == "1" or s[start] == "2") and start + 1 < len(s):
            if s[start + 1] == "0":
                count += self.decode(s, start + 2)
            else:
                d = int(s[start + 1])
                if s[start] == "1" or (s[start] == "2" and d <= 6):
                    count += self.decode(s, start + 1)
                    count += self.decode(s, start + 2)
                else:
                    count += self.decode(s, start + 1)
        else:
            count += self.decode(s, start + 1)

        self.memory[start] = count
        return count
    
    def numDecodings(self, s: str) -> int:
        # check validity
        if s[0] == "0":
            return 0
        for i in range(1, len(s)):
            if s[i] == "0" and (s[i - 1] != "1" and s[i - 1] != "2"):
                return 0

        self.memory = {}
        return self.decode(s, 0)

s = Solution()
print(s.numDecodings("27"))
print(s.numDecodings("20110622"))
print(s.numDecodings("2611055971756562"))
print(s.numDecodings("1"))
print(s.numDecodings("11"))
print(s.numDecodings("111"))
print(s.numDecodings("1111"))
print(s.numDecodings("11111"))
print(s.numDecodings("111111"))
print(s.numDecodings("1111111"))
print(s.numDecodings("11111111"))
print(s.numDecodings("111111111"))
print(s.numDecodings("111111111111111111111111111111111111111111111"))
