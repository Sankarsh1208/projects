class Solution:
    def dailyTemperatures(self, temps):
        answers = [0]*len(temps)
        stack = []
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]]<temp:
                n = stack.pop()
                answers[n] = i - n
            stack.append(i)
        return answers