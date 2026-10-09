class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        d = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            d[ss].append(s)
        for sorteds, s in d.items():
            result.extend([s])
        return result