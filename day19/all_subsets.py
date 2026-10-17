class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        temp = []
        res = []
        n=len(nums)
        c = 0
        while c<pow(2, n):
            temp = []
            ans = list(f"{c:0{n}b}")
            for i in range(n):
                if ans[i] == '1':
                    temp.append(nums[i])
            res.append(temp)
            c+=1
        return res