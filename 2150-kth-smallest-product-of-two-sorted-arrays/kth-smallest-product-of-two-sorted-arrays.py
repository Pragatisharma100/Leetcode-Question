class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import bisect
        import math

        def countLE(x):
            count = 0
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        count += len(nums2)
                elif a > 0:
                    # Need b <= x // a
                    r = bisect.bisect_right(nums2, x // a)
                    count += r
                else:  # a < 0
                    # Need b >= ceil(x / a)
                    l = bisect.bisect_left(nums2, math.ceil(x / a))
                    count += len(nums2) - l
            return count

        left, right = -10**10, 10**10
        while left < right:
            mid = (left + right) // 2
            if countLE(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
