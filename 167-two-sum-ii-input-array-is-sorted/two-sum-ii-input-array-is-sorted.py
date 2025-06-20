class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left=0
        right=n-1
        while left < right:
            current=numbers[left] +numbers[right]
            if current == target:
                return [left+1,right+1]
            if current <= target:
                left+=1
            else:
                right-=1
        