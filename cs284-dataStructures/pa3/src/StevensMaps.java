package pa3;
import java.io.File;
import java.util.*;

public class StevensMaps {
    /**
     * Takes a file of locations and connections and returns a list of locations with their connections
     * @param file file from which locations/connections are extracted
     * @return list of locations all containing appropriate connections
     */
    public static List<Location> parseFile(File file) {

        try (Scanner scr = new Scanner(file)) {

            // read number of locations
            if (!scr.hasNextInt()) { return null; }
            int numLoc = scr.nextInt();
            if (numLoc <= 0) { return null; }
            scr.nextLine();

            // creates list of locations (to be returned)
            List<Location> map = new ArrayList<Location>(numLoc);

            // read location names + add to location list
            for (int i = 0; i < numLoc; i++) {
                if (!scr.hasNextLine()) { return null; }
                map.add(new Location(scr.nextLine().trim()));
                }

            // read number of connections
            if (!scr.hasNextInt()) { return null; }
            int numConn = scr.nextInt();
            if (numConn < 0) { return null; }
            scr.nextLine();

            // read connections + add them to locations
            for (int j = 0; j < numConn; j++) {
                if(!scr.hasNextLine()) { return null; }
                if(!scr.hasNextInt()) { return null; }
                int s = scr.nextInt();
                if(!scr.hasNextInt()) { return null; }
                int e = scr.nextInt();
                if(!scr.hasNextDouble()) { return null; }
                double len = scr.nextDouble();

                // check if locations are valid in map
                if (s < 0 || s >= numLoc || e < 0 || e >= numLoc || len <= 0) { return null; }

                // find locations in map
                Location start = map.get(s);
                Location end = map.get(e);

                // add connections to locations
                start.addConnection(new Connection(start, end, len));
                end.addConnection(new Connection(end, start, len));

            }

            // return the map of locations
            return map;

        } catch (Exception e) { return null; }
    }


    /**
     * Finds the shortest path between two locations
     * @param start the start of the path
     * @param target the end of the path
     * @return the shortest path between the two locations start and target
     */
    public static Path shortestPath(Location start, Location target) {
        PriorityQueue<Path> frontier = new PriorityQueue<>(new Path.PathComparator());
        frontier.add(new Path(start));

        Set<Location> visited = new HashSet<>();

        while (!frontier.isEmpty()) {

            Path current = frontier.poll();
            Location end = current.getEnd();

            // target is found
            if (end == target) { return current; }


            if (visited.contains(end)) { continue; }

            // marks a location as visited and extends path
            visited.add(end);
            for (Connection con : end.getOutgoingConnections()) {
                if (!visited.contains(con.getEnd())) { frontier.add(current.extend(con)); }
            }

        }

        // no paths exist
        return null;
    }

    /**
     * Searches for a Location in a list of Locations using just its name as a String
     * @param locations list of locations
     * @param locationName the name of the location
     * @return the location object with the corresponding name
     */
    public static Location nametoLocation(List<Location> locations, String locationName) {
        for (Location loc : locations) {
            if (loc.getName().equals(locationName)) {
                return loc;
            }
        }
        return null;
    }

    /**
     * Takes in a taskfile, parses it, and returns all the completed tasks as shortest paths
     * @param args args[0] is taskfile
     */
    public static void main(String[] args) {
        // ensures only a single argument (file) is provided
        if (args.length != 1) {
            System.out.println("Error: Only one argument may be used.");
            return; }

        String fileName = args[0];
        File taskFile = new File(fileName);

        // ensures file exists
        if (!taskFile.exists()) {
            System.out.println("Error: File " + fileName + " does not exist.");
            return; }

        try (Scanner scr = new Scanner(taskFile)) {

            // ensures file contains information
            if (!scr.hasNextLine()) {
                System.out.println("Error: File " + fileName + " is empty.");
                return; }

            String mapFileName = scr.nextLine().trim();

            File mapFile = new File(mapFileName);

            // parses files to retrieve locations if able
            List<Location> locations = parseFile(mapFile);
            if (locations == null) {
                System.out.println("Error: Locations in file " + mapFileName + " unable to be read.");
                return; }

            // takes number of tasks from file
            if (!scr.hasNextInt()) {
                System.out.println("Error: File " + fileName + " missing task count.");
                return; }
            int numTasks = scr.nextInt();
            scr.nextLine();

            // process each task
            for (int i = 0; i < numTasks; i++) {

                // ensures start location is in file
                if (!scr.hasNextLine()) {
                    System.out.println("Error: File missing start location for task " + (i + 1));
                    continue; }

                String startStr = scr.nextLine().trim();

                // ensures end location is in file
                if (!scr.hasNextLine()) {
                    System.out.println("Error: File missing end location for task " + (i + 1));
                    continue; }

                String endStr = scr.nextLine().trim();

                // finds both locations from their name
                Location start = nametoLocation(locations, startStr);
                Location end = nametoLocation(locations, endStr);

                // checks if start location could be retrieved
                if (start == null) {
                    System.out.println("Error: Start location " + startStr + " not found in map.");
                    continue; }

                if (end == null) {
                    System.out.println("Error: End location " + endStr + " not found in map.");
                    continue; }

                Path path = shortestPath(start, end);

                // checks if path could be found between start and end
                if (path == null) {
                    System.out.println("Error: Path between " + startStr + " and " + endStr + " locations does not exist.");
                    continue; }

                // prints out distances and locations along the shortest path
                System.out.printf("Distance from %s to %s: %f%n", startStr, endStr, path.getLength());
                System.out.println("Locations Along Path:");
                for (Location loc : path) {
                    System.out.println("\t" + loc.getName());
                }

            }


        } catch (Exception e) {
            System.out.println("Error: Unable to read file " + fileName + ".");
            return; }
    }
}
