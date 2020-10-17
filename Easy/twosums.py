#primary approach O(n*n)
class Solution(object):
    def twoSum(self, nums, target):
        result=[]
        for i in range(0,len(nums)):
            for j in range (i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    result=[i,j]
                    return result
#improved approach O(n)
class Solution(object):
    def twoSum(self, nums, target):
        result=[]
        for i in range(0,len(nums)):
            n=target-nums[i]
            if( n in nums and nums.index(n)!=i):
                result=[i,nums.index(n)]
                return result
