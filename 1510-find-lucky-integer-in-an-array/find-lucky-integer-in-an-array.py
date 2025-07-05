class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=Counter(arr)
        max_lucky = -1
        for num in freq:
            if freq[num] == num:
                max_lucky = max(max_lucky, num)
        return max_lucky
        
        