class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        s=0
        for i in range(0, len(stones)):
            if stones[i] in jewels:
                s=s+1;
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        return s
