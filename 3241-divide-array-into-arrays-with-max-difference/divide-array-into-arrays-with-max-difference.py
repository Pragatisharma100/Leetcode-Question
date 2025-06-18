class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(0,n,3):
            group =nums[i:i+3]
            if len(group)==3 and group[2] -group[0] <=k:
                ans.append(group)
            else:
                return []
        return ans
                    
        