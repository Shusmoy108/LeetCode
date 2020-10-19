#O(n*n) solution
   def lengthOfLongestSubstring(self, s):
        l=0
        for i in range(0,len(s)):
            re=s[i]
            j=0
            for j in range(i+1,len(s)):
                if s[j] not in re:
                    re=re+s[j]
                else:
                    break
            l=max(l,len(re))
            if(j==len(s)):
                break
        return l
    #O(n) solution
    def lengthOfLongestSubstring(self, s):
        ans=0;
        i=0;
        j=0;
        st=""
        while(i<len(s) and j<len(s)):
            if(s[j] not in st):
                st= st + s[j]
                j=j+1
                ans=max(ans,j-i)
            else:
                st=st.strip(s[i])
                i=i+1
