class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res=[]
        for i in range (0,len(nums)):
            s=0
            for j in range (0,len(nums)):
                if nums[i]>nums[j]:
                    s=s+1
            res.append(s)    
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return res
        
