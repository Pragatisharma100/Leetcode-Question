class Solution:
    def isValid(self, word: str) -> bool:
        v=False
        c=False
        # word min of 3 character
        for i in range(len(word)):
            if len(word) <3 :
                return False
            
        # 0-9, alphabet
            if not word[i].isalnum():
                return False
            
        # 1 vowel, 1 consonant
            if word[i] in "aeiouAEIOU":
                v=True
            if word[i] not in "aeiouAEIOU0123456789":
                c=True
        if v and c:
            return True
        else:
            return False