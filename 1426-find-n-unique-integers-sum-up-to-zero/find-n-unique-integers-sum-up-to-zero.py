class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[0]*n
        k=1
        for i in range(n//2):
            ans[i] =k
            ans[n-1-i]=-k
            k+=1
        return ans

        