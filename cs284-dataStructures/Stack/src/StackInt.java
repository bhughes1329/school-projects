public interface StackInt<E> {
    public E push(E item);
    public E pop();
    public E peek();

    public boolean isEmpty();
}
