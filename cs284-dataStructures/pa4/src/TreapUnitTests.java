import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;


public class TreapUnitTests {

    private Treap<Integer> treap;
    private Treap<Integer> seeded;

    @BeforeEach
    public void setUp() {
        treap = new Treap<>();
        seeded = new Treap<>(13);
    }


    // TESTS for constructors

    @Test
    @DisplayName("Tests that empty default constructor produces empty treap.")
    public void testTreapEmptyDefaultConstructor() {
        assertFalse(treap.find(1));
    }

    @Test
    @DisplayName("Tests that seeded constructor produces empty treap.")
    public void testTreapSeededConstructor() {
        assertFalse(seeded.find(1));
    }


    // TESTS for add(E key)

    @Test
    @DisplayName("Tests that the element was successfully added to the tree.")
    public void testAddSuccessful() {
        assertTrue(treap.add(13));

    }

    @Test
    @DisplayName("Tests that duplicate element was not added to tree.")
    public void testAddDuplicateKey() {
        treap.add(13);
        assertFalse(treap.add(13));
    }

    @Test
    @DisplayName("Tests null entry into add function.")
    public void testAddNullEntry() {
        assertThrows(Exception.class, () -> treap.add(null));
    }

    @ParameterizedTest
    @ValueSource(ints = {Integer.MIN_VALUE, -1, 0, 1, Integer.MAX_VALUE})
    @DisplayName("Tests add with different values.")
    public void testAddParameterized(int key) {
        assertTrue(treap.add(key));
        assertTrue(treap.find(key));
    }


    // TESTS for add(E key, int priority)

    @Test
    @DisplayName("Tests add function with priority.")
    public void testAddWithPriority() {
        treap.add(3, 15);
        treap.add(2, 25);
        treap.add(7, 10);
        treap.add(1, 87);
        treap.add(4, 76);
        assertTrue(treap.find(1));
        assertTrue(treap.find(7));
        assertTrue(treap.toString().startsWith("(key=1, priority=87)"));
    }

    @Test
    @DisplayName("Tests add function with duplicates with priority.")
    public void testAddDuplicatesWithPriority() {
        treap.add(13, 32);
        assertFalse(treap.add(13, 34));
    }

    @Test
    @DisplayName("Tests add with null key.")
    public void testAddNullWithPriority() {
        assertThrows(Exception.class, () -> treap.add(null, 10));
    }

    @Test
    @DisplayName("Tests add function with priority on an empty treap.")
    public void testAddToEmptyTree() {
        treap.add(1, 45);
        assertTrue(treap.find(1));
    }

    @ParameterizedTest
    @ValueSource(ints = {Integer.MIN_VALUE, -1, 0, 1, Integer.MAX_VALUE})
    @DisplayName("Tests add with priority with different values.")
    public void testAddParameterizedWithPriority(int key) {
        assertTrue(treap.add(key, 40));
        assertTrue(treap.find(key));
    }


    // TESTS for delete(E key)

    @Test
    @DisplayName("Tests deletes from tree and unaffects others.")
    public void testDeleteKey() {
        treap.add(8, 30);
        treap.add(4, 50);
        treap.add(9, 20);
        treap.add(2, 70);
        assertTrue(treap.delete(4));
        assertFalse(treap.find(4));
        assertTrue(treap.find(9));
        assertTrue(treap.find(2));
    }

    @Test
    @DisplayName("Tests nonexistent key deletion.")
    public void testDeleteNonexistentKey() {
        treap.add(8, 30);
        assertFalse(treap.delete(5));
    }

    @Test
    @DisplayName("Tests delete with null key.")
    public void testDeleteNullKey() {
        assertThrows(Exception.class, () -> treap.delete(null));
    }

    @Test
    @DisplayName("Tests deletion from an empty tree.")
    public void testDeleteFromEmptyTree() {
        assertFalse(treap.delete(5));
    }

    @Test
    @DisplayName("Tests deleting same key twice.")
    public void testDeleteSameKeyTwice(){
        treap.add(5, 10);
        treap.add(4, 20);
        assertTrue(treap.delete(5));
        assertFalse(treap.delete(5));
    }

    @ParameterizedTest
    @ValueSource(ints = {Integer.MIN_VALUE, -1, 0, 1, Integer.MAX_VALUE})
    @DisplayName("Tests delete with different values.")
    public void testDeleteParameterized(int key) {
        treap.add(key, 30);
        assertTrue(treap.delete(key));
    }

    // TESTS for find(E key)

    @Test
    @DisplayName("Tests that inserted key can be found.")
    public void testFindExistingKey() {
        treap.add(5, 60);
        assertTrue(treap.find(5));
    }

    @Test
    @DisplayName("Tests that nonexistent key is not found.")
    public void testFindNonexistentKey() {
        treap.add(5, 60);
        assertFalse(treap.find(4));
    }

    @Test
    @DisplayName("Tests that finding null key throws exception.")
    public void testFindingNullException() {
        assertThrows(Exception.class, () -> treap.find(null));
    }

    @Test
    @DisplayName("Tests find function on an empty tree.")
    public void testFindEmptyTree() {
        assertFalse(treap.find(1));
    }

    @ParameterizedTest
    @ValueSource(ints = {Integer.MIN_VALUE, -1, 0, 1, Integer.MAX_VALUE})
    @DisplayName("Tests find with different values.")
    public void testFindParameterized(int key) {
        treap.add(key, 20);
        assertTrue(treap.find(key));
    }


    // TESTS for toString()

    @Test
    @DisplayName("Tests toString on empty treap returns null/empty")
    public void testToStringEmpty() {
        String toString = treap.toString();
        assertTrue(toString == null || toString.isEmpty() || toString.equals("null\n"));
    }

    @Test
    @DisplayName("Tests toString contains key after its added.")
    public void testToStringContainsKey() {
        treap.add(5, 10);
        assertTrue(treap.toString().contains("key=5"));
    }

    @Test
    @DisplayName("Tests toString contains priority after its added.")
    public void testToStringContainsPriority() {
        treap.add(5, 10);
        assertTrue(treap.toString().contains("priority=10"));
    }

    @Test
    @DisplayName("Tests toString contains null for missing children.")
    public void testForNullFromMissingChildren() {
        treap.add(5, 10);
        assertTrue(treap.toString().contains("null"));
    }

    @Test
    @DisplayName("Tests toString root is highest priority.")
    public void testtoStringHighestPriorityRoot() {
        treap.add(3, 15);
        treap.add(2, 25);
        treap.add(7, 10);
        treap.add(1, 87);
        treap.add(4, 76);
        assertTrue(treap.find(1));
        assertTrue(treap.find(7));
        assertTrue(treap.toString().startsWith("(key=1, priority=87)"));
    }

    @ParameterizedTest
    @ValueSource(ints = {Integer.MIN_VALUE, -1, 0, 1, Integer.MAX_VALUE})
    @DisplayName("Tests toString with different values.")
    public void testtoStringParameterized(int key) {
        treap.add(key, 20);
        assertTrue(treap.toString().contains("key="+ key));
    }


}
