// class definition in java
public class Rectangle {
    // data fields
    private double width;
    private double height;
    private static int numberOfRectangles = 0;
    private static final double PI = 3.14;

    // constructor
    public Rectangle(double x, double y){
        width = x;
        height = y;
        numberOfRectangles++;
    }

    // methods
    public double area(){
        return width * height;
    }

    // static method - same for all instances
    public static int getNumberOfRectangles() {
        return numberOfRectangles;
    }

}