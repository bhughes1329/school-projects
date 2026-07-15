package BankAccount;

public class BankAccount {
    private double balance;
    private String name;
    private int idNumber;

    public BankAccount() {
        balance = 100.00;
        name = "John Doe";
        idNumber = 0;
    }


    public BankAccount(double bal, String nm, int id) {
        balance = bal;
        name = nm;
        idNumber = id;
    }

    public double deposit(double amount) {
        balance += amount;
        return balance;
    }

    public double withdraw(double amount) {
        balance -= amount;
        return balance;
    }

}
