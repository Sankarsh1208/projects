class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        prev = intervals[0][1]
        count = 1
        for s, e in intervals[1:]:
            if s>=prev:
                count+=1
                prev = e
        return n-count