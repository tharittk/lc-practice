class Solution {
    public ListNode oddEvenList(ListNode head) {
        // 0, 1, 2 element
        if (head == null || head.next == null || head.next.next == null) return head;

        ListNode odd_prev = null;
        ListNode odd_curr = head;
        ListNode even_prev = null;
        ListNode even_curr = head.next;

        ListNode odd_og = head;
        ListNode even_og = head.next;

        boolean endInEven = false;

        while (odd_curr.next.next != null && even_curr.next.next != null){
            odd_prev = odd_curr;
            odd_curr = odd_curr.next.next;
            odd_prev.next = odd_curr;

            even_prev = even_curr;
            even_curr = even_curr.next.next;
            even_prev.next = even_curr;

            if (even_curr.next == null){
                endInEven = true;
                break;
            }

        }

        if (endInEven) {
            odd_curr.next = even_og;
        } else { // odd left 1 elem
            odd_prev = odd_curr;
            odd_curr = odd_curr.next.next;
            odd_prev.next = odd_curr;

            even_curr.next = null;
            
            odd_curr.next = even_og;
        }
        // for (int i = 0; i < 9; i++){
        //     System.out.println(odd_og.val);
        //     odd_og = odd_og.next;
        // }

        return odd_og;
    }
}
