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
        
        HashSet<ListNode> nodeSet = new HashSet<ListNode>();
        ListNode currentNode = head;

        while (currentNode.next != null) {
            if (nodeSet.Contains(currentNode)) {
                return true;
            } 
            nodeSet.Add(currentNode);
            currentNode = currentNode.next;
        }

        return false;
    }
}