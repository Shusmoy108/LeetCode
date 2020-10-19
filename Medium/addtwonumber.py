class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(l):
    if(l.next==None):
        return l.val
    return reverseList(l.next)*10+l.val
def reverseNum(s):
    m=s%10
    s=int(s/10)
    if(s==0):
        l= ListNode(m,None)
        return l
    l=ListNode(m,reverseNum(s))
    return l
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        x=reverseList(l1)
        y=reverseList(l2)
        s=x+y
        return reverseNum(s)
