    def isPalindrome(self, x):
        if(x<0):
            return 0==1
        y=x
        s=0
        while(y!=0):
            s=(s*10) + (y%10)
            y=int(y/10)
        return x==s
