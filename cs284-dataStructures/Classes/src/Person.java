public class Person {
        private String firstName;
        private String lastName;
        private String IDNumber;

    public Person(String first, String last, String ID){
        firstName = first;
        lastName = last;
        IDNumber = ID;
    }

    // set method - sets parameter to a certain value

    /**
     * Sets the lastName field.
     * @param n the last name
     */
    public void setLastName(String n) {
        lastName = n;
    }

    //accessor methods - get values

    // toString method, can just print the object to call
    /**
     * Retrieves the information in a Person object
     * @return the object state as a string
     */
    public String toString() {
        return "Given name: " + firstName + "\n";
    }


    // equals method
    /**
     * Compares two Person objects for equality
     * @param per the second person object
     * @return true if the Person objects have same ID #, false otherwise
     */
    public boolean equals(Person per) {
        if (per == null)
            return false;
        else
            return IDNumber.equals(per.IDNumber);
    }


}
