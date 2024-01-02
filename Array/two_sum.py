
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDic = dict()
        n = len(nums)
        for i in range(n):
            diff = target- nums[i]
            if diff in numDic:
                return [numDic[diff], i]
            numDic[nums[i]] = i
        return []
    
# Time complexity : O(n)
# Space complexity : O(n)