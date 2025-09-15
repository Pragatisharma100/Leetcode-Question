class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split(" ")
        ans=len(words)
        for word in words:
            for char in word:
                if char in brokenLetters:
                    ans-=1
                    break
        return ans
