class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans=0
        freq=Counter(nums)
        n=len(nums)
        for i in freq:
            if i+1 in freq:
                ans = max(ans, freq[i] + freq[i+1])
        return ans

            
