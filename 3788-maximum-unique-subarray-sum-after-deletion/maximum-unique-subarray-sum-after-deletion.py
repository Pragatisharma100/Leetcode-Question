class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans=0
        maxelement=float(-inf)
        new=set()
        for num in nums:
            maxelement=max(maxelement,num)
            if num >0 and num not in new:
                ans+=num
                new.add(num)
        if ans>0:
            return ans
        else:
            return maxelement
        

        