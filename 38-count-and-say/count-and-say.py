class Solution(object):
    def countAndSay(self, n):
        def recur(num):
            if num == 1:
                return '1'
            
            cas = recur(num - 1)

            print(num,cas)

            if len(cas) == 1:
                return '11'

            s = ''
            counter = 1
            old = cas[0]
            for i in range(1, len(cas)):
                if cas[i] != old:
                    s += str(counter) + old
                    old = cas[i]
                    counter = 1
                else:
                    counter += 1
            s += str(counter) + old
            return s
        
        return recur(n)
