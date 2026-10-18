#Method 1(dynamic programing):
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        maxl = -sys.maxsize - 1
        dp = [1]*(len(nums))
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

#method 2(using recursion):
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def sol(i,prev):
            if i<0 or i>=len(nums):
                return 0
            skip = sol(i+1, prev)
            take = 0
            if nums[i]>prev:
                prev = nums[i]
                take = 1 + sol(i+1, prev)
            return max(skip, take)
        return sol(0, float("-inf"))

#method 3(using bisect):
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = []
        for num in nums:
            i = bisect_left(lis, num)
            if i == len(lis):
                lis.append(num)
            else:
                lis[i] = num
        return len(lis)