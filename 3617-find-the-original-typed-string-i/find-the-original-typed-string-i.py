class Solution:
    def possibleStringCount(self, word: str) -> int:
        can_poss = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                can_poss+=1
        return can_poss
