class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        mod = 10
        div = 1
        res = ''
        if x < 0:
            res += '-'
        x = abs(x)
        while mod <= abs(x) * 10:
            print('v', mod, div)
            digit = x % mod // div
            print('digit',digit)
            res += f'{digit}'
            print(res)
            mod *= 10
            div *= 10
        int_res = int(res)
        if int_res > 2 ** 31 - 1 or int_res < -2 ** 31:
            return 0
        return int_res
        