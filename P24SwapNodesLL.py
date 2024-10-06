class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        nxt = head.next
        if not nxt:
            return head
        head = nxt
        prev = None

        while True:
            curr.next = nxt.next # 1 points 3
            nxt.next = curr # 2 poins 1
            if prev: # prevent first iter
                prev.next = nxt
            prev = curr # prev is 1
            if not curr.next:
                break
            else:
                curr = curr.next # curr points 3

            if not curr.next: 
                break
            else:
                nxt = curr.next # nxt points 4
        return head