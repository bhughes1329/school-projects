import java.util.NoSuchElementException;

public class QueueLL<E>{
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
    private Node<E> front;
    private Node<E> rear;
    private int size=0;

    public E peek(){
        if(size == 0) //front == null
            return null;
        return front.data;
    }

    public boolean offer(E item){
        if(item == null)
            return false;
        if(front == null){
            rear = new Node<>(item);
            front = rear;
        }else{
            rear.next = new Node<E>(item);
            rear = rear.next;
        }
        size++;
        return true;
    }


    /**
     * Removes an entry from the front of the queue, if queue is not empty.
     * If queue is empty, throws NoSuchElementException
     * @return data at the front of the queue.
     */
    public E remove(){
        if (front == null) {
            throw new NoSuchElementException();
        }
        E returnVal = front.data;
        if (size == 1) {
            front = null;
            rear = null;
        } else {
            front = front.next;
        }

        size--;
        return returnVal;
    }

    public int size(){ return size;}

    public static void main(String[] args){
        QueueLL<String> queue = new QueueLL<>();
        queue.offer("Test");
        queue.offer("Rest");
        queue.offer("Fast");
        System.out.println(queue.remove()); // Must return Test
        System.out.println(queue.remove()); // Must return Rest
        System.out.println(queue.remove()); // Must return Fast
        System.out.println(queue.remove()); // Throws an exception
    }
}
