"""Unit tests for the application.

**Note**: There are broken unit tests for cases that should be handled in
the future. These are marked as expected failures for now. There are also
a handful of methods that are very complicated and would require extensive
mocking of the `raw_input()` function to test fully. They are marked for
code review.
"""

import unittest
import StringIO
import sys
from datetime import datetime

import Utils
from Account import Account
from Customer import Customer
from Session import Session

CODE_REVIEW_COMMENT = ("Function is too complex; should refactor and/or "
    "discuss with others before proceeding.")

class TestAccount(unittest.TestCase):
    """Tests the `Account.Account` class."""
    def setUp(self):
        self.account = Account("savings", 35.25)

    def test_execute_transactions(self):
        pass

    def test_log(self):
        """TO-DO: Write a time-freezing decorator or use a 3rd-party
        time-freezing library like Python's `freezegun` to capture the full
        time stamp. Then we can directly compare full log entries instead of
        validating the individual `transaction_type` and `amount` values,
        then confirming that the time stamps match to the nearest minute.
        """
        self.account.log("deposit", 5.25)
        self.assertEqual(len(self.account.history), 1)
        only_entry = self.account.history[0]
        current_time = str(datetime.now())
        self.assertEqual(only_entry["transaction_type"], "deposit")
        self.assertEqual(only_entry["amount"], "$5.25")
        self.assertEqual(only_entry["time"][0:14], current_time[0:14])

    def test_log_multiple_transactions(self):
        self.account.log("deposit", 3.41)
        self.account.log("withdrawal", 2.00)
        self.assertEqual(len(self.account.history), 2)
        self.assertEqual(self.account.history[0]["transaction_type"],
            "deposit")
        self.assertEqual(self.account.history[1]["transaction_type"],
            "withdrawal")

    # For these next 3 tests, the balance will not change until self.balance
    # is incremented or decremented. Perhaps something to think about.
    def test_report_transaction_success_withdrawal(self):
        actual_report = self.account.report_transaction_success("withdrawal",
            7.89)
        expected_report = "Successfully withdrew $7.89. New balance: $35.25"
        self.assertEqual(actual_report, expected_report)

    def test_report_transaction_success_deposit(self):
        actual_report = self.account.report_transaction_success("deposit", 0.11)
        expected_report = "Successfully deposited $0.11. New balance: $35.25"
        self.assertEqual(actual_report, expected_report)

    def test_report_transaction_success_invalid_transaction(self):
        self.assertRaises(ValueError, self.account.report_transaction_success,
            "nonsense", 3.06)

    @unittest.expectedFailure
    def test_report_transaction_success_invalid_amount(self):
        self.assertRaises(TypeError, account.report_transaction_success,
            "deposit", "string where there should be a float or an int")

    @unittest.skip(CODE_REVIEW_COMMENT)
    def test_deposit(self):
        pass

    @unittest.skip(CODE_REVIEW_COMMENT)
    def test_withdraw(self):
        pass


class TestCustomer(unittest.TestCase):
    """Tests the `Customer.Customer` class."""
    # def setUp():
    #     accounts = [
    #         {
    #             "account_type": "checking",
    #             "balance": 256.45
    #         },
    #         {
    #             "account_type": "savings",
    #             "balance": 100467.21
    #         }
    #     ]
    #     self.customer = Customer("0121", "Worf", accounts)

    def test_display_account_choices(self):
        pass

    def test_display_account_choices_no_accounts(self):
        pass

    def test_update_account_summary(self):
        pass

    def test_display_account_summary(self):
        pass


class TestSession(unittest.TestCase):
    """Tests the `Session.Session` class."""
    customer_list = [
        {
            "name": "Jean-Luc Picard",
            "pin": "4145",
            "accounts": [
                {
                    "account_type": "checking",
                    "balance": 53.98
                },
                {
                    "account_type": "money market",
                    "balance": 2000000.00
                },
                {
                    "account_type": "savings",
                    "balance": 650782.24
                }
            ]
        },
        {
            "name": "Worf",
            "pin": "0121",
            "accounts": [
                {
                    "account_type": "checking",
                    "balance": 256.45
                },
                {
                    "account_type": "savings",
                    "balance": 100467.21
                }
            ]
        }
    ]
    def setUp(self):
        self.session = Session(self.customer_list, "UT Credit Union")
        self.session.current_customer = Customer("0121", "Worf",
            self.customer_list[1]["accounts"])
        self.session.current_customer.summary = [
            "You fought well today",
            "You will continue to fight well tomorrow"
            ]

    def confirmPrintStatement(self, func, expected_output):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        func()
        sys.stdout = sys.__stdout__
        # Because Python's `print` automatically appends a newline...
        expected_output += "\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
        captured_output.close()

    def test_display_homescreen(self):
        self.confirmPrintStatement(self.session.display_homescreen,
            "Welcome to UT Credit Union!")

    def test_get_customer(self):
        pass

    def test_receipt(self):
        # Confirm that update_account_summary() was called
        pass

    # Why is this failing?
    def test_greet_customer(self):
        expected_greeting = (
            "Hello, Worf!\n"
            "Here is your account summary: \n"
            "You fought well today\n"
            "You will continue to fight well tomorrow\n"
            )
        self.confirmPrintStatement(self.session.greet_customer,
            expected_greeting)

    def test_proceed(self):
        pass

    @unittest.skip(CODE_REVIEW_COMMENT)
    # Use doctest for this?
    def test_serve(self):
        pass

    def test_logout(self):
        self.confirmPrintStatement(self.session.logout,
            "Thank you for banking with UT Credit Union. Good bye!")


class TestUtils(unittest.TestCase):
    """Tests the `Utils` module."""
    def test_clean(self):
        self.assertEqual(Utils.clean(" Fresh Eggs "), "fresh eggs")

    def test_dollar(self):
        self.assertEqual(Utils.dollar(54602.3), "$54,602.30")


if __name__ == "__main__":
    unittest.main()
