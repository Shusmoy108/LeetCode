    def reverse(self, x):
        y=x;
        s=0;
        if(x<- 2**31 or (x>2**31 - 1)):
            return 0
        if(x<0):
            y=-x
        while(y!=0):
            m= y%10
            s=(s*10)+m
            y=int(y/10)
        if(s<- 2**31 or (s>2**31 - 1)):
            return 0
        if(x>=0):
            return s
        else:
            return -s
        
i=reverse(-123)
print(i)
