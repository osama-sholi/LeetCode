class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = sum(nums[:k])/k
        avg = max_avg
        for i in range(k,len(nums)):
            new_sum = avg*k + nums[i] - nums[i-k]
            avg = new_sum/k
            if avg > max_avg:
                max_avg = avg
        return max_avg
        