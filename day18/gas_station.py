class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        n = len(gas)
        k =0
        start = 0
        for i in range(n):
            k+=gas[i] - cost[i]
            if k<0:
                start = i+1
                k = 0
        return start