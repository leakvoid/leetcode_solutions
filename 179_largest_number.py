def is_bigger(num1, num2):
    n1_l = 10
    n1 = num1 // 10
    while n1:
        n1 //= 10
        n1_l *= 10
        
    n2_l = 10
    n2 = num2 // 10
    while n2:
        n2 //= 10
        n2_l *= 10

    s1 = num1 * n2_l + num2
    s2 = num2 * n1_l + num1
    if s1 == s2:
        return 0
    elif s1 > s2:
        return -1
    else:
        return 1

def cmp_to_key(mycmp):
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort( key=cmp_to_key(is_bigger) )
        res = ""
        for n in nums:
            res += str(n)
        
        res = res.lstrip('0')
        if res == "":
            return "0"
        else:
            return res
