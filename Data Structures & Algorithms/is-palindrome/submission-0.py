class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for i in s:
            if i.isalnum():
                newstr+=i.lower()
        return newstr == newstr[::-1]
sol = Solution()
print(sol.isPalindrome(s = "Was it a car or a cat I saw?"))