# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr = []
        flag = 0
        while(l1!=None or l2!=None):
            if (l1!=None and l2!=None):
                arr.append((l1.val + l2.val + flag)%10)
                if (l1.val + l2.val + flag > 9):
                    flag = 1
                else:
                    flag = 0
                l1 = l1.next
                l2 = l2.next
            elif (l1!=None and l2==None):
                arr.append((l1.val + flag)%10)
                if (l1.val + flag > 9):
                    flag = 1
                else:
                    flag = 0
                l1 = l1.next
            elif (l2!=None and l1==None):
                arr.append((l2.val + flag)%10)
                if (l2.val + flag > 9):
                    flag = 1
                else:
                    flag = 0
                l2 = l2.next
        if(flag):
            arr.append(1)
        return arr
                
            
            