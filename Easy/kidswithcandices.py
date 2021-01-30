class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        mx=-1
        res=[]
        for i in range (0,len(candies)):
            if(candies[i]>mx):
                mx=candies[i]
        for i in range (0,len(candies)):
            res.append((candies[i]+extraCandies)>=mx)
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        return res
        
