class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for i in range(n):
            prod=1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]

            res[i] = prod
        return res
sol = Solution()
print(sol.productExceptSelf(nums = [1,2,4,6]))