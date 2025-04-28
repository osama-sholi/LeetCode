class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)

        i = 0
        left = 1
        while i < len(nums):
            answer[i] *= left
            left *= nums[i]
            i += 1
        i -= 1
        right = 1
        while i >= 0:
            answer[i] *= right
            right *= nums[i]
            i-=1

        return answer

        
            
        