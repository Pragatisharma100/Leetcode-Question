class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr=0
        for i in range(len(nums)):
            maxOr=maxOr | nums[i]
        count=0
        def recursive(index,currentOr):
            nonlocal count
            if index ==len(nums):
                if currentOr ==maxOr:
                    count +=1
                return
            recursive(index+1,currentOr |nums[index])
            recursive(index+1,currentOr )
        recursive(0, 0)
        return count