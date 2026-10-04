class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        temp = {}
        stack = []
        for i in nums2:
            while stack and stack[-1]<i:
                temp[stack.pop()] = i
            stack.append(i)
        while stack:
            temp[stack.pop()] = -1
        return [temp[i] for i in nums1]