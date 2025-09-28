class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans=0
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1] +nums[i+2]:
                ans=max(ans,nums[i]+nums[i+1]+nums[i+2])
        return ans



