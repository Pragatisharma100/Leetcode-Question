class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero=nums.count(0)
        one=nums.count(1)
        two=nums.count(2)
        nums[:]=[0]*zero +[1]*one+[2]*two
