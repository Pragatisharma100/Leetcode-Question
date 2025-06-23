class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def Checkpalindome(x):
            digit = list()
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]
        left, cnt, ans = 1, 0, 0
        while cnt < n:
            right = left * 10
            # op = 0 indicates enumerating odd-length palindromes
            # op = 1 indicates enumerating even-length palindromes
            for op in [0, 1]:
                for i in range(left, right):
                    if cnt == n:
                        break
                    pal_num = i
                    x = i // 10 if op == 0 else i
                    while x:
                        pal_num = pal_num * 10 + x % 10
                        x //= 10
                    if Checkpalindome(pal_num):
                        cnt += 1
                        ans += pal_num
            left = right

        return ans
        
        


        


