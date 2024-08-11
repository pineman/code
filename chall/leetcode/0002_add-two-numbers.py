# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #    s1 = str(l1.val)
    #    s2 = str(l2.val)
    #    while l1.next:
    #        l1 = l1.next
    #        s1 += str(l1.val)
    #    while l2.next:
    #        l2 = l2.next
    #        s2 += str(l2.val)
    #    d1 = int(s1[::-1])
    #    d2 = int(s2[::-1])
    #    s = str(d1 + d2)
    #    h = ListNode(int(s[::-1][0]))
    #    l = h
    #    for d in s[::-1][1:]:
    #        t = ListNode(int(d))
    #        if l:
    #            l.next = t
    #        l = t
    #    return h
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, last_carry = 0) -> ListNode:
        carry, d = divmod(l1.val + l2.val + last_carry, 10)
        result = ListNode(d)
        if l1.next or l2.next or carry:
            l1.next = l1.next or ListNode(0)
            l2.next = l2.next or ListNode(0)
            result.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return result
