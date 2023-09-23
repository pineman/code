# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
def mergeLists(head1, head2):
    head = SinglyLinkedListNode(-1)
    cur = head
    while head1 and head2:
        if head1.data < head2.data:
            cur.next = SinglyLinkedListNode(head1.data)
            head1 = head1.next
        else:
            cur.next = SinglyLinkedListNode(head2.data)
            head2 = head2.next
        cur = cur.next
    if head1:
        cur.next = head1
    else:
        cur.next = head2
    return head.next


