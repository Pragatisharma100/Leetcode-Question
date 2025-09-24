class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        ans = []
        if (n > 0 and d <0) or (n < 0 and d > 0):
            ans.append('-')
        n,d = abs(n), abs(d)
        ans.append(str(n//d))
        rem = n%d
        if rem == 0:
            return ''.join(ans)
        ans.append('.')
        dic = {}
        while rem:
            if rem in dic:
                ans.insert(dic[rem], '(')
                ans.append(')')
                return ''.join(ans)
            dic[rem] = len(ans)
            rem *= 10
            ans.append(str(rem//d))
            rem %= d
        return ''.join(ans)