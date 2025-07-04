class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def findChar(k, level):
            if level < 0:
                return 'a'
            op = operations[level]
            prev_len = lengths[level]
            if op == 0:
                if k <= prev_len:
                    return findChar(k, level - 1)
                else:
                    return findChar(k - prev_len, level - 1)
            else:
                if k <= prev_len:
                    return findChar(k, level - 1)
                else:
                    ch = findChar(k - prev_len, level - 1)
                    return chr(((ord(ch) - ord('a') + 1) % 26) + ord('a'))        
        lengths = [1] 
        max_level = 0
        for op in operations:
            curr_len = lengths[-1]
            new_len = curr_len * 2
            lengths.append(new_len)
            max_level += 1
            if new_len >= k:
                break
        return findChar(k, min(max_level, len(operations) - 1))