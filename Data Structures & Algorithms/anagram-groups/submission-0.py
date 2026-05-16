class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            sorted1 = ''.join(sorted(i))
            result[sorted1].append(i)
        return list(result.values())

sol = Solution()
print(sol.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))

