class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost=0
        maxlen=0
        l=0
        for r in range(len(s)):
            diff = abs(ord(s[r]) - ord(t[r]))
            cost += diff
            while maxCost<cost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1   
            maxlen = max(maxlen, r - l + 1)
        return maxlen