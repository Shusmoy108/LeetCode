class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        str1=""
        str2=""
        for i in range (0,len(word1)):
            str1=str1+word1[i]
        for i in range (0,len(word2)):
            str2=str2+word2[i]
        return str1==str2
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        
