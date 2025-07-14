class Solution(object):
    def __init__(self):
        self.permutes = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def comb(l):
            for i in nums:
                if i not in l:
                    new_list = l[:]
                    new_list.append(i)
                    comb(new_list)
            
            if len(l) == len(nums):
                self.permutes.append(l)
        
        comb([])
        return self.permutes
        