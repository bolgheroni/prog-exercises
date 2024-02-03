/**
 * Definition for singly-linked list.
 */
 public class ListNode {
     public int val;
     public ListNode next;
     public ListNode(int val=0, ListNode next=null) {
         this.val = val;
         this.next = next;
     }
 }
public class MergeTwoListsEx {

    private ListNode GetLesserNode(ListNode a, ListNode b) {
        if (a == null) {
            return b;
        }
        if (b == null) {
            return a;
        }

        if (a.val < b.val) {
            return a;
        }
        return b;
    }
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        ListNode mergeFront = new ListNode(-1, null);
        ListNode currentMergeTail = mergeFront;

        ListNode current1Tail = list1;
        ListNode current2Tail = list2;

        while (current1Tail != null || current2Tail != null) {
            ListNode lesser = GetLesserNode(current1Tail, current2Tail);
            
            if (lesser == current1Tail){
                current1Tail = current1Tail.next;
            } else {
                current2Tail = current2Tail.next;
            }
            
            currentMergeTail.next = new ListNode(lesser.val, null);
            currentMergeTail = currentMergeTail.next;            
        }

        return mergeFront.next;   

    }
}