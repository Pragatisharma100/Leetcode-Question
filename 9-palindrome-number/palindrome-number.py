class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans=True
        if str(x)==str(x)[::-1]:
            return ans
        return False