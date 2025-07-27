class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            v=len(str(nums[i]))
            if v%2==0:
                ans+=1
        return ans

        