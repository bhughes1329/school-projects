public class Shape {
    private int code;
    private String description;
    // protected - visibility is within class + its subclasses
    protected int offset;
    private String color;
    public Shape (int code, String description, int offset, String color) {
        this.code = code;
        this.description = description;
        this.offset = offset;
        this.color = color;
    }

    public Shape() {
        this.code = 0;
    }

    public String toString() {
        return description;
    }
}

