class Solution(object):
    def runningSum(nums):
        result = [];
        s=0;
        for i in range (0,len(nums)):
            s=s+nums[i]
            result.append(s)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return result
    r=runningSum([1,2,3,4])
    print(r)
