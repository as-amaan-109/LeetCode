class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            leftMax1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            rightMin1 = float('inf') if partition1 == m else nums1[partition1]
            
            leftMax2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            rightMin2 = float('inf') if partition2 == n else nums2[partition2]
            
            if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                # Valid partition found!
                if (m + n) % 2 == 0:
                    return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2.0
                else:
                    return float(max(leftMax1, leftMax2))
            elif leftMax1 > rightMin2:
                right = partition1 - 1
            else:
                left = partition1 + 1
        
        return -1  