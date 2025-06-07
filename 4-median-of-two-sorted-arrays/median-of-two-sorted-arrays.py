class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        length = len(nums1) + len(nums2)
        index = length//2
        if length % 2 == 0:
            index -= 1

        c = 0
        while c < index:
            if i == len(nums1):
                j += 1
            elif j == len(nums2):
                i += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
            c += 1

        val = 0
        if i == len(nums1):
            val = nums2[j]
            j += 1
        elif j == len(nums2):
            val = nums1[i]
            i += 1
        elif nums1[i] < nums2[j]:
            val = nums1[i]
            i += 1
        else:
            val = nums2[j]
            j += 1
        
        if length % 2 == 0:
            if i == len(nums1):
                val = (val + nums2[j])/2
            elif j == len(nums2):
                val = (val + nums1[i])/2
            elif nums1[i] < nums2[j]:
                val = (val + nums1[i])/2
            else:
                val = (val + nums2[j])/2
        
        return val

        