class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cost = {}
        for char, val in zip(chars, vals):
            cost[char] = val
        arr = []
        for char in s:
            if char in cost:
                arr.append(cost[char])
            else:
                arr.append(ord(char)-ord('a')+1)
        total = sum(arr)
        max_sum = cur_max = arr[0]
        for char in arr[1:]:
            cur_max = max(char, cur_max+char)
            max_sum = max(max_sum, cur_max)
        min_sum = cur_min = arr[0]
        for char in arr[1:]:
            car_min = min(char, cur_min + char)
            min_sum = min(min_sum, cur_min)
        if max_sum < 0:
            return max(max_sum,0)
        else:
            return max(max_sum, total-min_sum, 0)