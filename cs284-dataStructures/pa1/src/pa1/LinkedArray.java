package pa1;

/**
 * PUT YOUR INFORMATION BELOW PRIOR TO SUBMISSION
 * Name: Brooke Hughes
 * Pledge: I pledge my honor that I have abided by the Stevens Honor System.
 */

public class LinkedArray {
    public static class ArrayNode {
        public String[] array;
        public ArrayNode next;

        public ArrayNode(int size) {
            this.array = new String[size];
        }
    }

    public ArrayNode head;
    public int size;
    public ArrayNode tail;

    /**
     * Creates an empty LinkedArray object
     */
    public LinkedArray() {
        size = 0;
        head = null;
        tail = null;
    }


    /**
     * Returns the value at the given index in the LinkedArray
     * @param idx index to get value from
     * @return value at index idx
     */
    public String get(int idx) {
        // Checks if index is out of bounds
        if (idx < 0 || idx >= size) {
            throw new IndexOutOfBoundsException("Index " + idx + " is out of bounds.");
        }
        // Assigns helper variables
        ArrayNode current = head;
        int rest = idx;

        // Loops through each node
        while (current != null) {
            // Returns remaining index when on correct node
            if (rest < current.array.length) {
                return current.array[rest];
            }

            rest -= current.array.length;
            current = current.next;
        }
        throw new IndexOutOfBoundsException("Index " + idx + " is out of bounds.");

    }

    /**
     * Updates the value at the given index to the given value in the LinkedArray
     * @param idx index to set
     * @param value new value
     */
    public void set(int idx, String value) {
        // Checks if index is out of bounds
        if (idx < 0 || idx >= size) {
            throw new IndexOutOfBoundsException("Index " + idx + " is out of bounds.");
        }

        // Assigns helper variables
        ArrayNode current = head;
        int rest = idx;

        // Loops through each node
        while (current != null) {
            // Sets remaining index when on correct node
            if (rest < current.array.length) {
                current.array[rest] = value;
                return;
            }

            rest -= current.array.length;
            current = current.next;
        }
        throw new IndexOutOfBoundsException("Index " + idx + " is out of bounds.");

    }

    /**
     * Adds the given value to the end of the LinkedArray
     * @param value value to be appended to end of LinkedArray
     */
    public void append(String value) {
        // Creates head node if list is empty
        if (head == null) {
            head = new ArrayNode(1);
            head.array[0] = value;
            head.next = null;
            tail = head;
            size++;
            return;
        }

        // finds the last index of tail
        int lastIndexTail = size % tail.array.length;

        // Appends value inside of tail at its first empty index
        if (lastIndexTail < tail.array.length - 1) {
            tail.array[lastIndexTail + 1] = value;
        } else {
            // Creates a new node if the tail node is full
            ArrayNode newNode = new ArrayNode(tail.array.length * 2);
            newNode.array[0] = value;
            newNode.next = null;
            tail.next = newNode;
            tail = newNode;
        }
        // Increments size
        size++;

    }

    /**
     * Removes the last value in the LinkedArray and returns it
     * @return last value in LinkedArray
     */
    public String pop() {
        // Checks if list is empty
        if (size == 0) {
            throw new IndexOutOfBoundsException("This list is empty!");
        }

        // finds the last index of tail
        int lastIndexTail = size % tail.array.length;

        // Stores last index value and removes it
        String returnVal = tail.array[lastIndexTail];
        tail.array[lastIndexTail] = null;

        // Decrements size
        size--;

        // Checks if tail node is now empty
        if (lastIndexTail == 0) {
            // Checks if tail node was head node
            if (head == tail) {
                head = null;
                tail = null;
                // Returns last value
                return returnVal;
            }
            // Loops through until node before tail
            ArrayNode current = head;
            while (current.next != tail) {
                current = current.next;
            }
            // Makes the new tail node the node before the old tail node
            current.next = null;
            tail = current;
            // Returns last value
            return returnVal;
        }




        return returnVal;
    }

    /**
     * Returns the number of elements in the LinkedArray
     * @return number of elements in LinkedArray
     */
    public int size() {
        return size;
    }

    public void insert(int idx, String value) {
        throw new UnsupportedOperationException("Method Not Implemented");
        // Delete the above line, and write your implementation here.
        // This method is OPTIONAL and not for credit.
    }

    public String remove(int idx) {
        throw new UnsupportedOperationException("Method Not Implemented");
        // Delete the above line, and write your implementation here.
        // This method is OPTIONAL and not for credit.
    }

    /**
     * Returns a string representation of a LinkedArray
     * @return string representation of LinkedArray
     */
    @Override
    public String toString() {
        // Checks to see if list is empty
        if (size == 0) { return "[]"; }
        // Creates return variable
        String returnString = "[";
        // Loops through all list indices
        for (int i = 0; i < size; i++) {
            // Adds each element of the list to the string
            returnString += get(i);

            if (i + 1 < size) {
                // Adds a comma after each element as long as it's not the last
                returnString += ", ";
            }
        }
        // Finishes string and returns it
        returnString += "]";
        return returnString;


    }
}
