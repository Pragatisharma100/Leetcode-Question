class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Get the k-th largest value threshold
        sorted_nums = sorted(nums, reverse=True)
        threshold = sorted_nums[k - 1]
        # Count how many times each number in top k appears
        from collections import Counter
        top_k_counts = Counter(sorted_nums[:k])
# Build the answer by scanning nums and including allowed values
        ans = []
        for num in nums:
            if top_k_counts[num] > 0:
                ans.append(num)
                top_k_counts[num] -= 1
        return ans
