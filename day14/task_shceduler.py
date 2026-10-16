class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        s = []
        p = []
        count = 0
        maxt = 0
        for i in tasks:
            if i not in p:
                s.append(tasks.count(i))
            p.append(i)
        maxt = max(s)
        t = s.count(maxt)

        return max(len(tasks), (maxt-1)*(n+1) + t)