class Solution(object):
    def subtractProductAndSum(self, n):
        s=0
        m=1
        while(n!=0):
            x=n%10
            s=s+x
            m=m*x
            n=int(n/10)
        """
        :type n: int
        :rtype: int
        """
        return m-s
