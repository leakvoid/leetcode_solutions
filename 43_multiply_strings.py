class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mult_arr = []
        for i in range(len(num1) - 1, -1, -1):
            mult_s = "0" * (len(num1) - 1 - i)
            rem = 0
            for j in range(len(num2) - 1, -1, -1):
                m = int(num1[i]) * int(num2[j])
                m += rem
                mult_s += str(m % 10)
                rem = int(m / 10)
            if rem > 0:
                mult_s += str(rem)
            mult_arr.append(mult_s) # numbers in reverse order
        
        full_rem = 0
        res = ""
        for i in range(len(mult_arr[-1])):
            for j in range(len(mult_arr)):
                if i >= len(mult_arr[j]):
                    continue
                full_rem += int(mult_arr[j][i])
            res += str(full_rem % 10)
            full_rem = int(full_rem / 10)
            
        if full_rem > 0:
            res += str(full_rem)
            
        res = res.rstrip("0")
        if res == "":
            return "0"
        
        return res[::-1]

s = Solution()
print("123 * 456:", s.multiply("123", "456"))
print("45644444 * 23145667645645:", s.multiply("45644444", "23145667645645"))
