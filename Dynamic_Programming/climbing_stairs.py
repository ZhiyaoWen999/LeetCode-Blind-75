class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev, cur = 1, 1
        
        for i in range(2, n + 1):
            prev, cur = cur, cur + prev
        return cur

# Time complexity : O(n)
# Space complexity : O(n)