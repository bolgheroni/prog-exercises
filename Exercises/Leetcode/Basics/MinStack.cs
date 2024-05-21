public class MinStack {

    private class Node {
        public int val;
        public Node? next;

        public Node? minAtPushTime;
    }

    private Node _StackHead;

    private Node? _MinNode;

    public MinStack() {
        this._StackHead = new Node {
            val = -1,
            next = null,
            minAtPushTime = null,
        };
        this._MinNode = null;
    }
    
    // create new Node, update _StackHead and _MinNode 
    public void Push(int val) {
        var newNode = new Node{
            val = val,
            next = this._StackHead.next,
            minAtPushTime = this._MinNode
        };

        if (this._MinNode == null || this._MinNode.val > val) {
            this._MinNode = newNode;
        } 
        this._StackHead.next = newNode;

    }
    
    // update _StackHead and _MinNode
    public void Pop() {
        if (this._StackHead.next == null) {
            throw new InvalidOperationException("Can't pop empty stack");
        }
        this._MinNode = this._StackHead.next.minAtPushTime;
        this._StackHead.next = this._StackHead.next.next;
    }
    
    // return _Head.next
    public int Top() {
        if (this._StackHead.next != null) {
            return this._StackHead.next.val;
        }
        throw new InvalidOperationException("Can't get top of empty stack");
    }
    
    // return _MinNode
    public int GetMin() {
        if (this._MinNode != null) {
            return this._MinNode.val;
        }
        throw new InvalidOperationException("Can't get min of empty stack");
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */