public class BSTree<Key extends Comparable<Key>, Value> {
    private Node root;
    public class Node{
        private Key key;
        private Value value;
        private Node left;
        private Node right;
        private int size;
        public Node(){
            key = null;
            value = null;
            left = null;
            right = null;
            size = 0;
        }

        public Node(Key key, Value value, int size){
            this.key = key;
            this.value = value;
            this.size = size;
            left = null;
            right = null;
        }
    } //Node Class Ends

    public Node inorder(){
        return inorder(root);
    }

    private Node inorder(Node search){
        if (search != null) {
            inorder(search.left);
            System.out.println(search.key);
            inorder(search.right);
        }
        return search;
    }

    public Node preorder(){
        return preorder(root);
    }

    private Node preorder(Node search){

    }

    public Node search(Key key){
        return search(key, root);
    }

    private Node search(Key key, Node x){
        if (key == null)
            throw new IllegalArgumentException("key is null");
        if (x == null || x.key.compareTo(key) == 0)
            return x;
        int compare = key.compareTo(x.key);
        if (compare < 0)
            return search(key, x.left);
        else
            return search(key, x.right);
    }

    public void insert(Key key, Value value){
        if(key == null || value == null)
            throw new IllegalArgumentException("Insert: Key/Value is null!");
        root = insert(root, key, value);
    }

    private Node insert(Node x, Key key, Value value){
        if (x == null || x.key.compareTo(key) == 0)
            x = new Node(key, value, 1);
        int compare = key.compareTo(x.key);
        if (compare < 0)
            x.left = insert(x.left, key, value);
        else
            x.right = insert(x.right, key, value);
        return x;
    }

    public Node min(Node x) {

    }

    public Node successor(Key key){
        if(key == null)
            throw new IllegalArgumentException("Successor: Key null!");
        return successor(root, key);
    }

    private Node successor(Node node, Key key){

    }

    public int size() {
        return size(root);
    }

    public int size(Node x) {

    }

    public void deleteMin(){
        root = deleteMin(root);
    }

    private Node deleteMin(Node x){

    }

    public void delete(Key key){
        if(key == null)
            throw new IllegalArgumentException("Delete: Key is null");
        root = delete(root, key);
    }

    private Node delete(Node x, Key key){
        
    }


    public static void main(String[] args) {
        BSTree<Integer, Integer> btree = new BSTree<Integer, Integer>();
        int value = 1;
        btree.insert(22, value);
        btree.insert(10, value);
        btree.insert(30, value);
        btree.insert(3, value);
        btree.insert(12, value);
        btree.insert(5, value);
        btree.insert(28, value);
        btree.insert(34, value);
        btree.insert(25, value);
        btree.insert(29, value);

        System.out.println("In order Traversal Called:");
        btree.inorder();

        System.out.println("Btree root before successor: "+btree.root.key);

        BSTree.Node successor = btree.successor(btree.root, 25);
        System.out.println("Successor: "+successor.key);

        System.out.println("Btree root after successor: "+btree.root.key);

        System.out.println("Delete 22 in the tree");
        btree.delete(22);
        btree.inorder();
    }


}