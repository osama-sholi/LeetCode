class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in dic:
                return [dic[rem],i]
            else:
                dic[nums[i]] = i

        