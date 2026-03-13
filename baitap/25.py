class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            tail = prev
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            nxt = tail.next
            head_sub = prev.next
            prev.next = self.reverse(head_sub, tail)
            head_sub.next = nxt
            prev = head_sub

    def reverse(self, head, tail):
        prev = tail.next
        cur = head
        while prev != tail:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return tail