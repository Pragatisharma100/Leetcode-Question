class Solution:
    def kthCharacter(self, k: int) -> str:
        def dfs(length, k, ch):
            if length == 1:
                return ch
            mid = length // 2
            if k <= mid:
                return dfs(mid, k, ch)
            else:
                next_ch = chr((ord(ch) - ord("a") + 1) % 26 + ord("a"))
                return dfs(mid, k - mid, next_ch)

        length = 1
        while length < k:
            length *= 2  

        return dfs(length, k, "a")
        


