class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestCon = 0
        for num in nums:
            if num + 1 not in numSet:
                length = 1
                while num - length in numSet:
                    length += 1
                longestCon = max(longestCon, length)
        return longestCon

# Time complexity : O(n)
# Space complexity : O(n)