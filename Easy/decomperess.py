class Solution(object):
    def decompressRLElist(self, nums):
        res=[]
        for i in range(0,len(nums),2):
            freq=nums[i]
            val=nums[i+1]
            while freq!=0:
                res.append(val)
                freq=freq-1
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return res
        
        
