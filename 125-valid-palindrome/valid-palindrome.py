class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = ''.join(c for c in s.lower() if c.isalnum())
        left=0
        right=len(v)-1
        while left< right:
            if v[left]!=v[right]:
                return False
            left +=1
            right-=1
        return True
