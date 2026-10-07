class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxe = nums[0]
        t=0
        for i in nums:
            if t<0:
                t = 0
            
            t+=i
            maxe = max(maxe, t)
        return maxe