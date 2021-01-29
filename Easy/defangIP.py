class Solution(object):
      def defangIPaddr(self, address):
           add= address.split(".")
           res=""
           for i in range(0,len(add)):
               if i==0:
                   res=add[i]
               else:
                   res=res+"[.]"+add[i]
           return res
        
