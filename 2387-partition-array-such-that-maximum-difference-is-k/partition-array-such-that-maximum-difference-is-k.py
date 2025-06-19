class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        ans=1
        start=nums[0]
        i=1
        for i in range(1,n):
            if nums[i] - start > k:
                ans+=1
                start=nums[i]
        return ans