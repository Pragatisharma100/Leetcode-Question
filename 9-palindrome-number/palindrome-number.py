class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans=False
        if str(x)==str(x)[::-1]:
            ans=True
        return ans