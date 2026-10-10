class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low = 0
        n = len(nums)
        if n==1:
            return 0
        if n==2:
            return 0 if nums[0]>nums[1] else 1
        high = n-1
        while low < high:
            mid = int((low+high)/2)
            if nums[mid] < nums[mid+1]:
                low = mid+1
            elif nums[mid] < nums[mid-1]:
                high = mid-1
            else:
                return mid
        if low == high:
            return low