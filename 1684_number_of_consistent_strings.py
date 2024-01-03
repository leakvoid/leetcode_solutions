class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        allowed_set = set(allowed)
        
        count = 0
        for word in words:
            for c in word:
                if c not in allowed_set:
                    break
            else:
                count += 1
        
        return count