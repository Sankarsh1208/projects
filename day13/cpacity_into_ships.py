class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        n = len(weights)
        low = max(weights)
        high = sum(weights)
        while low<high:
            count, sums = 1, 0
            mid = (low+high)//2
            for w in weights:
                if sums+w>mid:
                    count+=1
                    sums = 0
                sums+=w
            if count<=days:
                high = mid
            elif count>days:
                low = mid+1
        return low
