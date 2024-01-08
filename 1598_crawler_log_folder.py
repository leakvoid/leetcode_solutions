class Solution:
    def minOperations(self, logs) -> int:
        depth = 0
        for l in logs:
            if l == "../":
                depth -= 1
                depth = max(0, depth)
            elif l == "./":
                pass
            else:
                depth += 1
        return depth