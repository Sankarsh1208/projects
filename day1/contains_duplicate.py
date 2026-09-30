def containsDuplicate(self, nums: list[int]) -> bool:
        d={}
        for i in range(len(nums)):
            if(nums[i] in d):
                return True
            else:
                d[nums[i]] = i
        return False