class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans=0
        count=0
        power=1
        for i in reversed(s):
            if i == '0':
                count += 1
            elif power <= k and ans + power <= k:
                ans += power
                count += 1
            power <<= 1
            if power > k:
                break  
        remaining_zeros = s[:len(s)-count].count('0')
        return count + remaining_zeros
