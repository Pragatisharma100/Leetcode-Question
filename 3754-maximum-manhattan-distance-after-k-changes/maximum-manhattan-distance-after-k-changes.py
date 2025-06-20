class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans=0
        h=0
        v=0
        for i in range(len(s)):
            if s[i]=="N":
                v+=1
            elif s[i]=="S":
                v-=1  
            elif s[i]=="W":
                h+=1
            else:
                h-=1
            md = abs(v)+abs(h)
            md=min(md+2*k,i+1) 
            ans=max(ans,md)
        return ans


            






