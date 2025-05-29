# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Boolean}
def hasCycle(head)
    s = head
    f = s&.next&.next
    while s
        return true if s == f
        s = s.next
        f = f&.next&.next
    end
    false
end
