class Solution:
    def kInversePairs_failed(self, n: int, k: int) -> int:
        prev = {0: 1}
        for r in range(2, n + 1):
            cur = {}
            for n in range(r):
                for key in prev:
                    new_n = n + key
                    if new_n > k:
                        break
                    if new_n in cur:
                        cur[new_n] += prev[key]
                    else:
                        cur[new_n] = prev[key]
            prev = cur
        
        if k not in cur:
            return 0
        return cur[k] % (pow(10,9) + 7)
    
    def kInversePairs(self, n: int, k: int) -> int:
        dp, mod = [1] + [0] * k, pow(10, 9) + 7
        
        for i in range(n):
            tmp, sm = [], 0
            for j in range(k + 1):
                sm += dp[j]
                if j - i - 1 >= 0:
                    sm-= dp[j - i - 1]
                sm %= mod
                tmp.append(sm)
            dp = tmp

        return dp[k]
