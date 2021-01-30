class Solution(object):
    def numberOfSteps (self, num):
        s=0
        while num!=0:
            if num%2==0:
                num= int(num/2)
            else:
                num= num-1
            s=s+1
        """
        :type num: int
        :rtype: int
        """
        return s
        
