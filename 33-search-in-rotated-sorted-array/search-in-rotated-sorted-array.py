class Solution(object):
    def __init__(self):
        self.index = -1
    
    def search(self, nums, target):
        # if len(nums) == 1:
        #     return 0 if nums[0] == target else -1
        def binary_search(l, r):
            print(l,r,index)
            if self.index != -1:
                return
            if l == r:
                if nums[l] == target:
                    self.index = l
                    return
                return
            mid = ((r - l) / 2) + l
            if nums[mid] == target:
                self.index = mid
                return
            if nums[l] > nums[mid] or nums[mid] > target:
                binary_search(l, mid)
            if nums[r] < nums[mid] or nums[mid] < target:
                binary_search(mid + 1, r)

        binary_search(0, len(nums) - 1)
        return self.index