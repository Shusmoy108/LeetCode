class Solution(object):
    def createTargetArray(self, nums, index):
        arr = [] 
        for i in range(len(nums)):
            if len(arr)==index[i]:
                arr.append(nums[i])
            else:
                arr.insert(index[i],nums[i])
            
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        return arr
        
