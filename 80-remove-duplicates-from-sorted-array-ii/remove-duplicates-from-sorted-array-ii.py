class Solution(object):
    def removeDuplicates(self, nums):
        k = len(nums)
        replacer = 0
        traverser = 0

        counter = 0
        current = nums[0]
        while traverser < len(nums):
            if current != nums[traverser]:
                counter = 0
                current = nums[traverser]
            
            if counter < 2:
                nums[replacer] = nums[traverser]
                replacer += 1
                counter += 1
            else:
                k -= 1
                
            traverser += 1

        return k

