class Solution:
    def candy(self, ratings: List[int]) -> int:
        ltr_candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                ltr_candy[i] = ltr_candy[i - 1] + 1
                
        rtl_candy = [1] * len(ratings)
        for i in range(len(ratings) - 2, -1, - 1):
            if ratings[i] > ratings[i + 1]:
                rtl_candy[i] = rtl_candy[i + 1] + 1
        
        total_candy = 0
        for i in range(len(ratings)):
            total_candy += max(ltr_candy[i], rtl_candy[i])
        return total_candy

# one array
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ltr_candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                ltr_candy[i] = ltr_candy[i - 1] + 1
        
        prev = 1
        total_candy = ltr_candy[len(ratings) - 1]
        for i in range(len(ratings) - 2, -1, - 1):
            if ratings[i] > ratings[i + 1]:
                prev += 1
            else:
                prev = 1
            total_candy += max(ltr_candy[i], prev)
        return total_candy
