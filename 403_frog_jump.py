class Solution:
    def bin_search(self, stones, start, end, target):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        if target == stones[mid]:
            return mid
        if target > stones[mid]:
            return self.bin_search(stones, mid + 1, end, target)
        return self.bin_search(stones, start, mid - 1, target)
    
    def can_jump(self, stones, pos, r):
        if r == 0:
            return -1
        return self.bin_search(stones, pos, len(stones) - 1, stones[pos] + r)
    
    def jump_stone(self, stones, pos, r):
        if pos == len(stones) - 1:
            return True
        
        if r in self.memory[pos]:
            return False
        
        new_pos = self.can_jump(stones, pos, r - 1)
        if new_pos != -1:
            if self.jump_stone(stones, new_pos, r - 1):
                return True
        
        new_pos = self.can_jump(stones, pos, r)
        if new_pos != -1:
            if self.jump_stone(stones, new_pos, r):
                return True
        
        new_pos = self.can_jump(stones, pos, r + 1)
        if new_pos != -1:
            if self.jump_stone(stones, new_pos, r + 1):
                return True
        
        self.memory[pos].add(r)
        return False
    
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != stones[0] + 1:
            return False
        
        self.memory = {}
        for i in range(1, len(stones) - 1):
            self.memory[i] = set()
        
        return self.jump_stone(stones, 1, 1)

s = Solution()
print( s.canCross([0,1,3,5,6,8,12,17]) )
