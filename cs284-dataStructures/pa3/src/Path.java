package pa3;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;

public class Path implements Iterable<Location> {

    // stores locations
    private List<Location> locations;
    //stores length of path
    private double length;

    /**
     * Constructor for Path class, creates new Path and adds a location to the start,
     * with a starting length of 0.0
     * @param start the first location in the path
     */
    public Path(Location start) {
        locations = new ArrayList<Location>();
        locations.add(start);
        length = 0.0;
    }

    /**
     * Constructor for Path class, creates new Path and assigns it a list of locations
     * and a length
     * @param locations list of locations for the path
     * @param length length of the path
     */
    private Path(List<Location> locations, double length) {
        this.locations = locations;
        this.length = length;
    }

    /**
     * Returns a copy of a Path with an added connection
     * @param connection the connection added to the path copy
     * @return copy of the original path with the added location
     */
    public Path extend(Connection connection) {

        if (!connection.getStart().equals(getEnd())){
            throw new EdgeConsistencyException("Connection does not start where Path ends!", connection);
        }

        List<Location> tempLocations = new ArrayList<Location>(this.locations);

        tempLocations.add(connection.getEnd());

        return new Path(tempLocations, this.length + connection.getLength());
    }

    /**
     * Returns the length of a path
     * @return length of path
     */
    public double getLength() {
        return this.length;
    }

    /**
     * Returns the last location in a path
     * @return end of Path
     */
    public Location getEnd() {
        return locations.get(locations.size() - 1);
    }

    /**
     * Returns an iterator over the locations in this path,
     * from the start to the end
     * @return iterator over the locations in this path
     */
    @Override
    public Iterator<Location> iterator() {
        return locations.iterator();
    }

    /**
     * Comparator for Paths that compares them using their total length, from shortest to
     * longest.
     */
    public static class PathComparator implements Comparator<Path> {

        /**
         * Compares two paths using their total length
         * Returns negative if path1 is shorter, positive if path2 is shorter,
         * and 0 if they have equal lengths
         * @param path1 the first path object to be compared.
         * @param path2 the second path object to be compared.
         * @return negative, positive, or 0 integer that is representative of the comparison
         * between the two paths
         */
        @Override
        public int compare(Path path1, Path path2) {
            return Double.compare(path1.getLength(), path2.getLength());
        }
    }

}
