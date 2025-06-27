class Solution(object):
    def __init__(self):
        self.result = [-1,-1]
    def searchRange(self, nums, target):
        def bs(l,r):
            print(l,r,self.result)
            if l >= r:
                if l == r and nums[l] == target:
                    if self.result[0] == -1 or l < self.result[0]:
                        self.result[0] = l
                    if l > self.result[1]:
                        self.result[1] = l    
                return
            mid = (l + r) / 2
            if nums[mid] == target:
                if self.result[0] == -1 or mid < self.result[0]:
                    self.result[0] = mid
                if mid > self.result[1]:
                    self.result[1] = mid              
            
            if nums[mid] == target or target > nums[mid]:
                bs(mid + 1, r)
            if nums[mid] == target or target < nums[mid]:
                bs(l, mid - 1)
            
        bs(0, len(nums) - 1)
        return self.result
        