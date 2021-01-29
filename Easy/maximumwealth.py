class Solution(object):
         def maximumWealth(self, accounts):
             mx=0
             for i in range (0,len(accounts)):
                 s=0
                 for j in range (0, len(accounts[i])):
                     s=s+accounts[i][j]
                 if s>mx:
                     mx=s
             return mx
        
