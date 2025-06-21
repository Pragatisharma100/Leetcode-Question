from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        min_deletions = float('inf')

        for i in range(n):
            base = freq[i]
            deletions = 0
            for j in range(n):
                if freq[j] > base + k:
                    deletions += freq[j] - (base + k)
                elif freq[j] < base:
                    deletions += freq[j]
            min_deletions = min(min_deletions, deletions)

        return min_deletions
