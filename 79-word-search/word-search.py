class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        def dfs(r, c, cn):
            if cn == len(word):
                return True
            if r < 0 or c < 0 or r >= R or c >= C or board[r][c] != word[cn]:
                return False
            temp = board[r][c]
            board[r][c] = "#"  
            found = (
                dfs(r + 1, c, cn + 1) or
                dfs(r - 1, c, cn + 1) or
                dfs(r, c + 1, cn + 1) or
                dfs(r, c - 1, cn + 1)
            )
            board[r][c] = temp  
            return found
        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):  
                    return True
        return False
        