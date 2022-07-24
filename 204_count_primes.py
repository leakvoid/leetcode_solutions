class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        is_prime_arr = [True] * n
        is_prime_arr[0] = False
        is_prime_arr[1] = False
        
        last_prime = 2
        while last_prime ** 2 < n:
            for i in range(last_prime * 2, n, last_prime):
                is_prime_arr[i] = False
                
            for i in range(last_prime + 1, n):
                if is_prime_arr[i]:
                    last_prime = i
                    break
        
        res = 0
        for i in range(2, n):
            if is_prime_arr[i]:
                res += 1
                
        return res
