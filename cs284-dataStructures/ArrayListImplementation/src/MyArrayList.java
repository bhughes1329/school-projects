import java.util.Arrays;

public class MyArrayList<E> {
    private static final int INITIAL_CAPACITY = 10;
    private E[] data;
    private int size = 0;
    private int capacity = 0;

    public MyArrayList() {
        capacity = INITIAL_CAPACITY;
        data = (E[]) new Object[INITIAL_CAPACITY];
    }

    public MyArrayList(int initialCapacity) {
        capacity = initialCapacity;
        data = (E[]) new Object[capacity];
    }

    public void reallocate() {
        capacity *= 2;
        data = Arrays.copyOf(data, capacity);
    }

    public boolean add(E element) {
        if (size == capacity) {
            reallocate();
        }
        data[size] = element;
        size++;
        return true;
    }

    public E get(int index) {
        if (index >= size || index < 0) {
            throw new ArrayIndexOutOfBoundsException(index);
        }
        return data[index];
    }

    public void add(int index, E element) {
        if (index >= size || index < 0) {
            throw new ArrayIndexOutOfBoundsException(index);
        }
        if (size == capacity) {
            reallocate();
        }

        for (int i = size; i > index; i--) {
            data[i] = data[i - 1];
        }
        data[index] = element;
        size++;
    }

    public E set(int index, E element) {
        if (index >= size || index < 0) {
            throw new ArrayIndexOutOfBoundsException(index);
        }
        E old = data[index];
        data[index] = element;
        return old;
    }

    public E remove(int index) {
        // base case
        if (index >= size || index < 0) {
            throw new ArrayIndexOutOfBoundsException(index);
        }

        //get value at index
        E returnVal = data[index];

        // shift values down
        for (int i = index + 1; i < size; i++) {
            data[i-1] = data[i];
        }

        // decrement size + return removed value
        size--;
        return returnVal;
    }

}
