public interface ShapeInterface {
    /**
     * This method sets up the coordinate for the shape.
     * @param offset
     */
    public void setOffset(int offset);

    /**
     * This method returns the coordinates for the shape.
     * @return
     */
    public int getOffset();

    /**
     * This method sets the color of the shape.
     * @param color
     */
    public void colorShape(String color);
}