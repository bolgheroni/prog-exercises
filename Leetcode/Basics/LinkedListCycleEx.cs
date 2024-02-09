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

        while (current.next != null) {
            if (current.next.Equals(head)) {
                return true;
            }
            var oldCurrent = current;
            current = oldCurrent.next;
            oldCurrent.next = head;
        }

        return false;
    }
}