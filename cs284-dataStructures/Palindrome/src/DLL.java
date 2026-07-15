public class DLL {
    private char data;
    private Node next;
    private Node prev;
    private Node head;
    private Node tail;
    private int size;


    private static class Node {
        private char data;
        private Node next;
        private Node prev;

        public Node(char data) {
            this.data = data;
        }


        public Node(char data, Node next, Node prev) {
            this.data = data;
            this.next = next;
            this.prev = prev;
        }
    }
    public boolean isPalindrome() {
        Node front = head;
        Node back = tail;
        if (front == null || tail == null) {
            return true;
        }
        while (front != back && front.next != back) {
            if (front.data == back.data) {
                front = front.next;
                back = back.prev;
            } else {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        DLL dll = new DLL();
        Node h = new Node('k', null, null);
        Node x = new Node('a', h, null);
        Node y = new Node('y', x, null);
        Node z = new Node('a', y, null);
        Node t = new Node('k', z , null);
        dll.head = h;
        dll.tail = t;
        dll.size = 5;
        h.next = x;
        x.next = y;
        y.next = z;
        z.next = t;
        if(dll.isPalindrome()) {
            System.out.println("it is a palindrome!");
        } else {
            System.out.println("not a palindrome!!!");
        }
    }



}
