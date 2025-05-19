class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        longest = 1
        left = 0
        right = 1
        while right < len(s):
            index = s[left:].index(s[right]) + left
            print(left,right)
            print('index',index)
            if index < right:
                length = right - left
                longest = max(length,longest)
                left = index + 1
            right += 1

        longest = max(right-left,longest)

        return longest
        