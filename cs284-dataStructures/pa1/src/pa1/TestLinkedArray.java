package pa1;
public class TestLinkedArray {


    public static void main(String[] args) {
        LinkedArray list = new LinkedArray();

        System.out.println("append test:");
        for (int i = 1; i <= 10; i++) {
            list.append("A" + i);
            System.out.println(list);
        }

        System.out.println("\nget test:");
        for (int i = 0; i < list.size(); i++) {
            System.out.println("Index " + i + ": " + list.get(i));
        }

        System.out.println("\nset test:");
        list.set(3, "X");
        list.set(7, "Y");
        System.out.println(list);

        System.out.println("\npop test:");
        while (list.size() > 0) {
            System.out.println("Popped: " + list.pop());
            System.out.println(list);
        }

        System.out.println("\nDone!");
    }

}