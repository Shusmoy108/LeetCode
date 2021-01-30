class Solution(object):
    def restoreString(self, s, indices):
        res=""
        for i in range(0,len(indices)):
            res=res+s[indices.index(i)]
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        return res
        
