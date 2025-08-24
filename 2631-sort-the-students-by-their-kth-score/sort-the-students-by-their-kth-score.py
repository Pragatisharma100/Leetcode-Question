class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n=len(score)
        ans= score[:]
        for i in range(n):
            for j in range(0,n-i-1):
                if ans[j][k] <ans[j+1][k]:
                    ans[j],ans[j+1]=ans[j+1],ans[j]
        return ans