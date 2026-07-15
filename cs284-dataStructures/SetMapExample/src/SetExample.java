import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class SetExample {
    public static void main(String[] args) {
        String[] listA = {"Ann", "Jill", "Sally"};
        String[] listB = {"Ann", "Jill", "Bill", "Bob"};
        Set<String> setA = new HashSet<String>(Arrays.asList(listA));
        Set<String> setACopy = new HashSet<>(Arrays.asList(listA));
        Set<String> setB = new HashSet<>();

        for (String s: listB) {
            setB.add(s);
        }

        System.out.println("Set A: " + setA);
        System.out.println("Set B: " + setB);
        System.out.println(("Set A union Set B: " + setA.addAll(setB)));
        System.out.println("Set A: " + setA);
        System.out.println("Set A intersection Set B: " + setACopy.retainAll(setB));
        System.out.println("Set A Copy: " + setACopy);
    }
}
