class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        check = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    tuple_t = (nums[i], nums[j], nums[k])

                    if tuple_t not in check:
                        result.append(triplet)
                        check.add(tuple_t)

                    j += 1
        return result