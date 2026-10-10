class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        sum = 0
        piles = sorted(piles)
        left, right = 1, piles[n-1]
        while left<right:
            mid = (left+right)//2
            for pile in piles:
                sum+=(-(-pile//mid))
            print(sum)
            if sum<=h:
                right = mid
            else:
                left = mid+1
            sum = 0
        return right