class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        res = []
        d = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        def bactrack(i, current):
            if i == len(digits):
                res.append(current)
                return
            for ch in d[int(digits[i])]:
                bactrack(i+1, current+ch)
                
        bactrack(0, "")
        return res