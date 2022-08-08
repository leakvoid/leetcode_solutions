class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = []
        for i in range(len(gas)):
            diffs.append(gas[i] - cost[i])
        
        if sum(diffs) < 0:
            return -1
        
        total = 0
        start = 0
        i = 0
        while i < len(diffs):
            total += diffs[i]
            if total < 0:
                start = i + 1
                total = 0
            i += 1
        
        return start
