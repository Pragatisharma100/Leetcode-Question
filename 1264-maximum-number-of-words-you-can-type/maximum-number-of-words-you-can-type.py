class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split(" ")
        ans=len(words)
        b=set(list(brokenLetters))
        for word in words:
            for char in word:
                if char in b:
                    ans-=1
                    break
        return ans
