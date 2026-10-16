class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merge = [intervals[0]]

        for s, e in intervals[1:]:
            if s<=merge[-1][1]:
                merge[-1][1] = max(merge[-1][1], e)
            else:
                merge.append([s, e])
        return merge