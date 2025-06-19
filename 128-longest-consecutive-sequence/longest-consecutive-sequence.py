class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        ans=0
        for num in a:
            if num - 1 not in a:
                length=1
                while num + length in a: 
                    length += 1
                ans = max(ans, length)
        return ans