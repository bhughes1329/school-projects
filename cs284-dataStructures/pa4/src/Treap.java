// Brooke Hughes
// I pledge my honor that I have abided by the Stevens Honor System.
import java.util.Random;
import java.util.Stack;

public class Treap<E extends Comparable<E>> {

private Random priorityGenerator;
private Node<E> root;

private static class Node<E> {
    public E data;
    public int priority;
    public Node<E> left;
    public Node<E> right;

    /**
     * Constructor to create a new node
     * @param data the key for the node
     * @param priority the random heap priority of the node
     */
    public Node(E data, int priority) {
        if (data == null) { throw new IllegalArgumentException("Data cannot be null!"); }
        this.data = data;
        this.priority = priority;
        left = null;
        right = null;
    }

    /**
     * Performs a right rotation about a node, and returns a reference to the
     * resulting root.
     * @return the root node that results after rotation
     */
    public Node<E> rotateRight() {
        Node<E> newNode = this.left;
        this.left = newNode.right;
        newNode.right = this;
        return newNode;
    }

    /**
     * Performs a left rotation about a node, and returns a reference to the
     * resulting root.
     * @return the root node that results after rotation
     */
    public Node<E> rotateLeft() {
        Node<E> newNode = this.right;
        this.right = newNode.left;
        newNode.left = this;
        return newNode;
    }

    /**
     * Returns a string representation of a node
     * @return string representation of a node
     */
    public String toString() {
        String string = "(key=" + this.data + ", priority=" + this.priority + ")";
        return string;
    }

}

    /**
     * Constructor to create a new treap
     */
    public Treap() {
        priorityGenerator = new Random();
        root = null;
    }

    /**
     * Constructor to constructor a new treap using a specific seed
     * @param seed seed used for random seed priorities
     */
    public Treap(long seed) {
        priorityGenerator = new Random(seed);
        root = null;
    }


    /**
     * Adds node into the treap using the given key, and a randomly
     * generated priority.
     * @param key given key for node to be added
     * @return true or false depending on whether or not the addition
     * to the treap was successful
     */
    public boolean add(E key) {
        if (key == null) { throw new IllegalArgumentException("Key cannot be null!"); }
        return add(key, priorityGenerator.nextInt()); }

    /**
     * Adds node into the treap using the given key and the given priority.
     * @param key given key for node to be added
     * @param priority given priority for node to be added
     * @return true or false depending on whether or not the addition to the
     * treap was successful
     */
    public boolean add(E key, int priority) {
        if (key == null) { throw new IllegalArgumentException("Key cannot be null!"); }
        if (root == null) {
            root = new Node<E>(key, priority);
            return true; }

        Stack<Node<E>> stack = new Stack<>();
        Node<E> current = root;

        while (true) {
            int compare = key.compareTo(current.data);
            if (compare == 0) { return false; }

            stack.push(current);

            if (compare < 0) {
                if (current.left == null) {
                    current.left = new Node<E>(key, priority);
                    stack.push(current.left);
                    break; }
                current = current.left;
            } else {
                if (current.right == null) {
                    current.right = new Node<E>(key, priority);
                    stack.push(current.right);
                    break;
                }
                current = current.right;
            }
        }
        reheap(stack);
        return true;
    }

    /**
     * Restores the heap invariant after node is added to the treap.
     * @param stack contains the nodes along path from root to parent of
     *              the newly inserted node.
     */
    private void reheap(Stack<Node<E>> stack) {
        Node<E> child = stack.pop();

        while (!stack.isEmpty()) {
            Node<E> parent = stack.pop();

            if (parent.priority >= child.priority) { break; }

            Node<E> subRoot;

            if(child.data.compareTo(parent.data) < 0) {
                subRoot = parent.rotateRight();
            } else {
                subRoot = parent.rotateLeft();
            }

            if (stack.isEmpty()) {
                root = subRoot;
            } else {
                Node<E> gParent = stack.peek();
                if (gParent.left == parent) { gParent.left = subRoot; }
                else { gParent.right = subRoot; }
            }
            child = subRoot;
        }
    }

    /**
     * Deletes the node with the given key from the treap if it exists.
     * If node with given key doesn't exist, treap is not modified.
     * @param key key to be deleted from treap
     * @return true or false for whether or not key was successfully deleted from
     * the treap
     */
    public boolean delete(E key) {
        if (key == null) { throw new IllegalArgumentException("Key cannot be null!"); }

        // key is not in treap, cannot remove it
        if (!find(key)) { return false; }

        this.root = delete(this.root, key);
        return true;
    }

    /**
     * Recursively deletes the node with the given from the subtree rooted
     * in the given node. If node with given key doesn't exist, treap subtree
     * will not be modified.
     * @param node node in which subtree is rooted
     * @param key key to be deleted from treap subtree
     * @return the root of the updated subtree
     */
    private Node<E> delete(Node<E> node, E key) {
        if (key == null) { throw new IllegalArgumentException("Key cannot be null!"); }
        if (node == null) { return null; }

        int compare = key.compareTo(node.data);

        if (compare < 0) {
            node.left = delete(node.left, key); }
        else if (compare > 0) {
            node.right = delete(node.right, key); }
        else {
            if (node.left == null) { return node.right; }
            if (node.right == null) { return node.left; }

            if (node.left.priority > node.right.priority) {
                node = node.rotateRight();
                node.right = delete(node.right, key);
            } else {
                node = node.rotateLeft();
                node.left = delete(node.left, key);
            }
        }
        return node;
    }


    /**
     * Searches for a node that contains the given key in a treap.
     * @param key key being searched for
     * @return true or false for whether or not a node with the given key is found
     */
    public boolean find(E key) {
        if (key == null) { throw new IllegalArgumentException("Key cannot be null!"); }
        return find(this.root, key);
    }

    /**
     * Recursively searches for a node with the given key in a treap subtree rooted
     * at the given node
     * @param root root of the subtree being searched
     * @param key key being searched for
     * @return true or false for whether or not a node with the given key is found
     */
    private boolean find(Node<E> root, E key) {
        if (key == null) { throw new IllegalArgumentException("Key cannot be null!"); }
        if (root == null) { return false; }

        int compare = key.compareTo(root.data);

        if (compare == 0) { return true; }
        else if (compare < 0) { return find(root.left, key); }
        else { return find(root.right, key); }
    }

    /**
     * Returns a string representation of the given treap
     * @return string representation of the treap
     */
    public String toString() {
        StringBuilder sb = new StringBuilder();
        toString(this.root, sb, 0);
        return sb.toString();
    }

    /**
     * Performs a preorder traversal of a subtree of a treap rooted at the given
     * node, appending the string representation of each node to StringBuilder
     * as it goes.
     * @param node node in which subtree is rooted
     * @param sb StringBuilder object
     * @param depth depth of the current node in the subtree
     */
    private void toString(Node<E> node, StringBuilder sb, int depth) {
        for (int i = 0; i < depth; i++) { sb.append("  "); }

        if (node == null) {
            sb.append("null\n");
            return;
        }

        sb.append(node.toString() + "\n");
        toString(node.left, sb, depth + 1);
        toString(node.right, sb, depth + 1);
    }


}