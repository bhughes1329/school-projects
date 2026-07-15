package BankAccount;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;

public class BankAccountUnitTests {
    BankAccount account;
    @BeforeEach
    void setUp() {
        account = new BankAccount();
    }

    @Test
    @DisplayName("Tests if deposit returns new balance")
    void deposit_test() {
        double result = account.deposit(32.33);
        assertEquals(132.33, result);
        result = account.deposit(12.50);
        assertEquals(144.83, result);
    }


    @Test
    @DisplayName("Tests if withdraw returns new balance")
    void withdraw_test() {
        double result = account.withdraw(12.50);
        assertEquals(132.33, result);
        result = account.withdraw(32.33);
        assertEquals(100.00, result);
    }

}
