"""Unit tests for the application.

**Note**: There are broken unit tests for cases that should be handled in
the future.
"""

import unittest
from datetime import datetime

import Utils
from Account import Account
from Customer import Customer
from Session import Session


class TestAccount(unittest.TestCase):
    """Tests the `Account.Account` class."""
    def test_execute_transactions(self):
        pass

    def test_log(self):
        """TO-DO: Write a time-freezing decorator or use a 3rd-party
        time-freezing library like Python's `freezegun` to capture the
        full time stamp. Then we can directly compare a full expected
        log entry to the actual entry instead of validating the individual
        `transaction_type` and `amount` values, then confirming that the time
        stamp matches the current time rounded to the nearest minute.
        """
        account = Account("savings", 35.25)
        account.log("deposit", 5.25)
        self.assertEqual(len(account.history), 1)
        only_entry = account.history[0]
        current_time = str(datetime.now())
        self.assertEqual(only_entry["transaction_type"], "deposit")
        self.assertEqual(only_entry["amount"], "$5.25")
        self.assertEqual(only_entry["time"][0:14], current_time[0:14])

    def test_log_multiple_transactions(self):
        account = Account("money market", 57.89)
        account.log("deposit", 3.41)
        account.log("withdrawal", 2.00)
        self.assertEqual(len(account.history), 2)
        self.assertEqual(account.history[0]["transaction_type"], "deposit")
        self.assertEqual(account.history[1]["transaction_type"], "withdrawal")

    # Note that for these next three tests, the balance will not chance until
    # self.balance is incremented or decremented.
    def test_report_transaction_success_withdrawal(self):
        account = Account("money market", 57.89)
        actual_report = account.report_transaction_success("withdrawal", 7.89)
        expected_report = "Successfully withdrew $7.89. New balance: $57.89"
        self.assertEqual(actual_report, expected_report)

    def test_report_transaction_success_deposit(self):
        account = Account("money market", 57.89)
        actual_report = account.report_transaction_success("deposit", 0.11)
        expected_report = "Successfully deposited $0.11. New balance: $57.89"
        self.assertEqual(actual_report, expected_report)

    def test_report_transaction_success_invalid_transaction(self):
        account = Account("money market", 57.89)
        self.assertRaises(ValueError, account.report_transaction_success,
            "nonsense", 3.06)

    def test_deposit(self):
        # account = Account("checking", 100.00)
        # account.deposit()
        # self.assertEqual()
        # Use mocks
        pass

    def test_withdraw(self):
        # Use mocks
        pass


class TestCustomer(unittest.TestCase):
    """Tests the `Customer.Customer` class."""
    def test_display_account_choices(self):
        pass

    def test_update_account_summary(self):
        pass

    def test_display_account_summary(self):
        pass


class TestSession(unittest.TestCase):
    """Tests the `Session.Session` class."""
    def test_display_homescreen(self):
        pass

    def test_get_customer(self):
        pass

    def test_receipt(self):
        pass

    def test_login(self):
        pass

    def test_proceed(self):
        pass

    def test_serve(self):
        pass

    def test_logout(self):
        pass


class TestUtils(unittest.TestCase):
    """Tests the `Utils` module."""
    def test_clean(self):
        self.assertEqual(Utils.clean(" Fresh Eggs "), "fresh eggs")

    def test_dollar(self):
        self.assertEqual(Utils.dollar(54602.3), "$54,602.30")


if __name__ == "__main__":
    unittest.main()
