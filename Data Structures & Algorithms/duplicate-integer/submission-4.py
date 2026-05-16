class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        target = set()
        for i in nums:
            if i in target:
                return True
            target.add(i)
        return False
   

sol = Solution()
print(sol.hasDuplicate([1,2,3,3]))
print(sol.hasDuplicate([1,2,3,4]))