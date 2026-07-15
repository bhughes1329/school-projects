public class Triangle extends Shape implements ShapeInterface {

    private String name;
    public Triangle (int code, String description, int offset, String color) {
        super(code, description, offset, color);
        this.name = "Triangle";
    }

    @Override
    public void setOffset(int offset) {
        this.offset = offset;
    }

    // override shoes if method was correctly overridden
    @Override
    public int getOffset() {
        return 0;
    }

    @Override
    public void colorShape(String color) {

    }

    @Override
    public String toString() {
        return name;
    }
}
