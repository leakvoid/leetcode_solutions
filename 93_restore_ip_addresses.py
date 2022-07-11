class Solution:
    def restore_rec(self, digit_str, shift, ip_str, filled_pos, res):
        if filled_pos == 4:
            res.append(ip_str)
            return
        
        rem_len = len(digit_str) - shift
        rem_subaddr_n = 3 - filled_pos
        
        min_subaddr_len = max(1, rem_len - rem_subaddr_n * 3)
        max_subaddr_len = min(3, rem_len - rem_subaddr_n)
        
        for sa_len in range(min_subaddr_len, max_subaddr_len + 1):
            subaddr_s = digit_str[shift:shift + sa_len]
            if subaddr_s[0] == "0" and sa_len > 1:
                break
            
            if int(subaddr_s) > 255:
                break
            
            new_ip_str = subaddr_s if ip_str == "" else ip_str + "." + subaddr_s
            self.restore_rec(digit_str, shift + sa_len, new_ip_str, filled_pos + 1, res)
    
    def restoreIpAddresses(self, s: str) -> [str]:
        res = []
        self.restore_rec(s, 0, "", 0, res)
        return res

s = Solution()
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("101023"))
