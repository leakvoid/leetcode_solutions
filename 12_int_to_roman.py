class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman_dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        roman_enum = [1000, 500, 100, 50, 10, 5, 1]

        res = ""
        for d_i in range(0, len(roman_enum), 2):
            d = roman_enum[d_i]
            if d_i != 0:
                d5 = roman_enum[d_i - 1]
                d10 = roman_enum[d_i - 2]
            i_part = num // d
            r_part = num % d
            if i_part <= 3:
                res += i_part * roman_dict[d]
            elif i_part == 4:
                res += roman_dict[d] + roman_dict[d5]
            elif i_part == 5:
                res += roman_dict[d5]
            elif i_part < 9:
                res += roman_dict[d5] + (i_part - 5) * roman_dict[d]
            elif i_part == 9:
                res += roman_dict[d] + roman_dict[d10]
            else:
                print("ERROR")
            
            num = r_part

        return res

s = Solution()
print(s.intToRoman(2996))
