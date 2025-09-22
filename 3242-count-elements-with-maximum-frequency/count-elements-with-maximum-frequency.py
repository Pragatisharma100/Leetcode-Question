class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=Counter(nums)
        ans=0
        high=max(freq.values())
        for count in freq.values():
            if count==high:
                ans+= count
        return ans
        