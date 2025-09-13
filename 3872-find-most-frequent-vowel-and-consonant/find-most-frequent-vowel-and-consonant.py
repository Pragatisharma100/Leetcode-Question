class Solution:
    def maxFreqSum(self, s: str) -> int:
        # s=Counter(s)
        freq1={}
        freq2={}
        ans=0
        for ch in s:
            if ch in "aeiou":
                if ch not in freq1:
                    freq1[ch] =1
                else:
                    freq1[ch]+=1
            else:
                if ch not in freq2:
                    freq2[ch] =1
                else:
                    freq2[ch]+=1
        if freq1:
            ans=max(freq1.values()) 
        if freq2:
            ans+=max(freq2.values()) 
        return ans
