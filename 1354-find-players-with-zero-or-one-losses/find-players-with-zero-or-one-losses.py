class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans1=[]
        ans2=[]
        d={}
        for i,j in matches:
            if i not in d:
                d[i]=0
            if j not in d or d[j]==0:
                d[j]=1
            elif d[j]==1:
                d[j] +=1
        for key,val in d.items():
            if val==0:
                ans1.append(key)
            if val==1:
                ans2.append(key)
        ans1.sort()
        ans2.sort()
        return [ans1,ans2]


