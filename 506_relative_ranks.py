import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        h = []
        for i in range(len(score)):
            heapq.heappush( h, ((-1) * score[i], i) )
        
        res = [""] * len(score)
        place = 1
        while h:
            (score, pos) = heapq.heappop(h)
            if place == 1:
                res[pos] = "Gold Medal"
            elif place == 2:
                res[pos] = "Silver Medal"
            elif place == 3:
                res[pos] = "Bronze Medal"
            else:
                res[pos] = str(place)
            place += 1
        return res


