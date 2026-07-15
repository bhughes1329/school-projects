

public class Main {
    public static void main(String[] args) {

        System.out.println("Hello World!");

        // creating an instance of an object
        Rectangle rect1 = new Rectangle(3, 4); // left hand of statement performed first (new rectangle, not creating object variable)

        // instance methods
        double ar1 = rect1.area();

        // declares an array of size 5 (first item @ index 0)
        // initializes as five zeros
        int[] nums = new int[5];

        // length is a parameter of array data type
        int nums_length = nums.length;

        // also initializes an array [fixed size]
        String[] names = {"brooke", "kelly"};

        // loop
        // will iterate 5 times (0, 1, 2, 3, 4)
        for (int i=0; i<5; i++) {
            System.out.println(nums[i]);
        }

        for (int i : nums) {
            System.out.println(nums[i]);
        }

    }
}


/*
access modifiers:
public - accesible by everyone
private - only accesible within the class
protected -
*/

/*
data fields + types:
byte
short
int
long
float
double
char
boolean
String (separate from primitive but behaves same)
 */