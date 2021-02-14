class Solution(object):
    def interpret(self, command):
        s=""
        i=0
        while True :
            
            if command[i]=="(" and command[i+1]==")":
                s=s+"o"
                i=i+2
            elif command[i]=="(" and command[i+1]=="a":
                s=s+"al"
                i=i+4
            else:
                s=s+command[i]
                i=i+1
            if i>=len(command):
                break
        """
        :type command: str
        :rtype: str
        """
        return s
        
