class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        p = 0

        # skip white spaces
        while p < len(s) and s[p] == ' ':
            p += 1
        print('p',p)

        if p == len(s):
            return 0

        res = ''

        if s[p] == '-':
            res += '-'
            p += 1
        elif s[p] == '+':
            p += 1

        

        while p < len(s) and s[p].isnumeric():
            print('p',p)
            res += s[p]
            print('res',res)
            p += 1
        
        if not res or res == '-':
            return 0
        
        int_res = int(res)

        if int_res > 2**31 - 1:
            return 2**31 - 1 

        if int_res < -2**31:
            return -2**31

        return int_res
        
