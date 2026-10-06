class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        end = [None]*len(nums)
        pro = 1
        if 0 in nums:
            end = [0]*len(nums)
            if nums.count(0) == 1:
                inx = nums.index(0)
                nums.remove(0)
                end[inx] = math.prod(nums)
            return end

        else:        
            for i in nums:
                pro = pro*i
            
            for i in range(len(nums)):
                end[i] = pro//nums[i]
            return end