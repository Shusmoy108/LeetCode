class Solution(object):
    def xorOperation(self, n, start):
        res= start
        for i in range(n-1):
            res= res^(start+2)
            start=start+2
           
        return res
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        
