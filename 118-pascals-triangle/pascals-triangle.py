class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=numRows*numRows
        traingle=[]
        for i in range(numRows):
            rows=[1] *(i+1)
            for j in range(1,i):
                if i==j or j==0:
                    ans[i][j] =1
                else :
                    rows[j]=traingle[i-1][j-1] + traingle[i-1][j]
            traingle.append(rows)
        return traingle
