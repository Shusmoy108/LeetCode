class Solution(object):
    def decode(self, encoded, first):
        arr=[first]
        s=first
        for i in range (0,len(encoded)):
            s=abs(encoded[i]^s)
            arr.append(s)
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        return arr
