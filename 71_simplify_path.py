class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list = list(filter(lambda e: e != '', path.split('/')))
        dynamic_len = len(dir_list)
        
        i = 0
        while i < dynamic_len:
            if dir_list[i] == '.':
                del dir_list[i]
                dynamic_len -= 1
            elif dir_list[i] == '..':
                del dir_list[i]
                dynamic_len -= 1
                if i - 1 >= 0:
                    del dir_list[i - 1]
                    dynamic_len -= 1
                    i -= 1
            else:
                i += 1

        return '/' + '/'.join(dir_list)

s = Solution()
print(s.simplifyPath("/home////foo bar/"))
