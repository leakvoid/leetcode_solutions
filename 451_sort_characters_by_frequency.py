import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}

        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1
        
        h = []
        for key in d:
            heapq.heappush(h, ((-1) * d[key], key))
        
        res = ""
        while h:
            t = heapq.heappop(h)
            res += ((-1) * t[0]) * t[1]
        return res
