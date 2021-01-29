class Solution(object):
    def shuffle(self, nums, n):
        res=[]
        for i in range (0,n):
            res.append(nums[i])
            res.append(nums[len(nums)-n+i])
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        return res
