class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        count = 0
        maxs = 0
        for i in s:
            if i not in temp:
                count+=1
                temp.append(i)
            else:
                maxs = max(maxs, count)
                while temp[0]!=i:
                    temp.pop(0)
                temp.pop(0)
                temp.append(i)
                count = len(temp)
        maxs = max(maxs, count)
        return maxs