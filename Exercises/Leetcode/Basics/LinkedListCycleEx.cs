namespace LinkedListCycle;
/**
 * Definition for singly-linked list.
 */
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) {
        val = x;
        next = null;
    }
}

public class LinkedListCycleEx {
    public bool HasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        var current = head;
        // the idea is to point all nexts to the head
        // if at any point we get a node that points to the head, either it actually points to the head (forms a loop),
        // or we are in a node that we already visited (traversed a loop)
        while (current.next != null) {
            if (current.next.Equals(head)) {
                return true;
            }
            // all of this logic is just me saving up an aux variable to perform the exchange
            head.next = current.next;
            if (!current.Equals(head)){
                // handling when we're in the head
                current.next = head;    
            }
            current = head.next;
            head.next = head;
        }

        return false;
    }
}