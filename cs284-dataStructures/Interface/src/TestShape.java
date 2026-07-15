public class TestShape {
    public static void main(String[] args) {
        Shape s = new Shape(2, "a shape", 3, "white");
        System.out.println(s.toString());
        Shape t = new Triangle(1, "a triangle shape" , 2, "black");
        System.out.println(t.toString());
    }
}
