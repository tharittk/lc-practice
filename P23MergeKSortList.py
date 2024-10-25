# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_nodes(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            if node1.val <= node2.val:
                head = node1
            else:
                head = node2

            node1_prev = node1
            node2_prev = node2   
            while node1 and node2:

                if node1.val <= node2.val:
                    while node1 and node1.val <= node2.val:
                        node1_prev = node1
                        node1 = node1.next
                    node1_prev.next = node2
                else:
                    while node2 and node2.val < node1.val:
                        node2_prev = node2
                        node2 = node2.next
                    node2_prev.next = node1

            return head
        
        def aux(sub_list):
            if not sub_list:
                return
            if len(sub_list) == 1:
                return sub_list[0]
            
            elif len(sub_list) == 2:
                node1 = sub_list[0]
                node2 = sub_list[1]
                return merge_two_nodes(node1, node2)

            else:
                n = len(sub_list)
                n1 = aux(sub_list[:n//2])
                n2 = aux(sub_list[n//2:])
                return aux([n1,n2])


        return aux(lists)
                    


        