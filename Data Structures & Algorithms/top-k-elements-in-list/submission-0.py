class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return[i for i, count in freq.most_common(k)]


sol = Solution()
print(sol.topKFrequent(nums = [1,2,2,3,3,3], k = 2))    