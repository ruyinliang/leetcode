class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
        list = sorted(nums1+nums2, reverse=False)
        print(list)
        if (len(list)%2==0):
            median = int(len(list)/2)
            return ((list[median-1]+list[median])/2)*1.0
        elif (len(list)%2==1):
            median = int(len(list)/2)
            print(median)
            return list[median]*1.0
        