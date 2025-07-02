class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        
        def backtrack(start, path, target):  # 'target' now tracks remaining sum
            if target == 0:
                ans.append(path[:])
                return
            if target < 0:
                return 
            
            for i in range(start, n):
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])  # subtract from target
                path.pop()  
        backtrack(0, [], target)
        return ans
        