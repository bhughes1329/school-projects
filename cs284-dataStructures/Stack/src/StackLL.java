
import java.util.NoSuchElementException;

public class StackLL<E> {
    private static class Node<E>{
        private E data;
        private Node<E> next;

        private Node(E dataItem){
            data = dataItem;
            next = null;
        }

        private Node(E dataItem, Node<E> nodeRef){
            data = dataItem;
            next = nodeRef;
        }
    }

    private Node<E> topOfStackRef;
    int size = 0;

    public StackLL(){
        topOfStackRef = null;
    }

    public StackLL(E[] data){
        topOfStackRef = null;
        for(E item: data){
            push(item);
        }
    }


    public E push(E obj){
        if(obj == null)
            throw new IllegalArgumentException("You cannot add null element to a stack!");
        topOfStackRef = new Node(obj, topOfStackRef);
        size++;
        return obj;
    }


    public E peek(){
        if(topOfStackRef == null)
            throw new NoSuchElementException();
        return topOfStackRef.data;
    }

    /**
     * Returns the entry at the top of the stack, when stack is not empty.
     * Otherwise, throws NoSuchElement Exception
     * @return data in the top of the stack
     */
    public E pop(){
        if (topOfStackRef == null) {
            throw new NoSuchElementException();
        }
        E returnVal = topOfStackRef.data;
        topOfStackRef = topOfStackRef.next;
        size--;
        return returnVal;
    }

    public int size(){ return size;}

    public static void main(String[] args){
        StackLL<String> stack = new StackLL<>();
        stack.push("Test");
        stack.push("Rest");
        stack.push("Fast");
        System.out.println(stack.pop()); // Must return Fast
        System.out.println(stack.pop()); // Must return Rest
        System.out.println(stack.pop()); // Must return Test
        System.out.println(stack.pop()); // Throws an exception
    }

}
