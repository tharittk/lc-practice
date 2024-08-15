class Solution { // clean version 
  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    // Handle empty lists
    if (list1 == null) return list2;
    if (list2 == null) return list1;

    // Choose the smaller head as the new head
    ListNode head = list1.val < list2.val ? list1 : list2;

    // Iterate through both lists, keeping track of the current node in the merged list
    ListNode current = head;
    while (list1 != null && list2 != null) {
      if (list1.val < list2.val) {
        current.next = list1;
        list1 = list1.next;
      } else {
        current.next = list2;
        list2 = list2.next;
      }
      current = current.next;   

    }

    // Append the remaining nodes from the non-empty list   

    current.next = list1 != null ? list1 : list2;

    return head;
  }
}