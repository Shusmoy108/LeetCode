class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if(len(nums1)==0 and len(nums2)==0):
            return 0
        elif(len(nums1)==0):
            num3=nums2
        elif(len(nums2)==0):
            num3=nums1
        else:    
            num3= nums1+ nums2
        num3.sort()
        if(len(num3)==1):
            return num3[0]
        if(len(num3)%2==1):
            n=int(len(num3)/2)
            return num3[n]
        else:
            n=int(len(num3)/2)
            x=n-1
            m=num3[n]+num3[x]
            print(num3[n])
            print(num3[x])
            m=m/2.00
            if(m<0):
                return 0
            return m
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
