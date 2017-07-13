"""Unit tests for the application.

TO-DOs:

- There are broken unit tests for cases that should be handled in
the future. These are marked as expected failures for now.

- There are also methods that have the user interact with the program; I think
that testing these fully would require some combination of mocking out the
`raw_input()` function and exploiting the `doctest
<https://docs.python.org/2/library/doctest.html>`_ library, which tests
interactive Python examples. These tests are skipped for now and marked for
code review feedback.

- Finally, there are unit tests which are still in progress. These are skipped
for now with the "In progress" message and will be updated in the next pull
request.
"""

import StringIO
import sys
import unittest
from datetime import datetime

import Utils
from Account import Account
from Customer import Customer
from Session import Session

REQUEST_CODE_REVIEW = ("Function is too complex; should refactor and/or "
    "discuss with others before proceeding.")

class TestAccount(unittest.TestCase):
    """Tests the `Account.Account` class."""
    def setUp(self):
        self.account = Account("savings", 35.25)

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_execute_transactions_answer_is_w(self):
        # Assert that `account.withdraw()` was called.
        pass

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_execute_transactions_answer_is_d(self):
        # Assert that `account.deposit()` was called.
        # Can re-use the `confirmPrintStatement()` function I wrote below.
        pass

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_execute_transactions_answer_is_x(self):
        # Assert that 'Canceling transaction.' was printed.
        pass

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_execute_transactions_make_3_attempts(self):
        # Move through the while loop 3 times and assert that
        # 'Canceling transaction after 3 attempts' was printed.
        # Again, can re-use `confirmPrintStatement()`.
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

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_deposit(self):
        # Assert that the balance gets decremented.
        # Assert that `account.report_transaction_success()` gets called with
        # the right arguments.
        # Assert that `log()` gets called with the right arguments.
        pass

    @unittest.expectedFailure
    def test_deposit_negative_number(self):
        pass

    @unittest.expectedFailure
    def test_deposit_not_a_number(self):
        pass

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_withdraw(self):
        # Assert that balance was decremented.
        # Assert that `account.report_transaction_success()` was called.
        # Assert that `account.log()` was called.
        pass

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_withdraw_input_x(self):
        # Assert that 'Transaction canceled.' was printed.
        pass

    @unittest.expectedFailure
    def test_withdraw_over_200(self):
        # Assert that 'You may not withdraw more than $200 in one session.'
        # was printed.
        # Assert that user is asked to try another amount.
        pass

    @unittest.expectedFailure
    def test_withdraw_not_a_multiple_of_20(self):
        # Assert that 'You must enter a multiple of $20.' was printed.
        # Assert that user is asked to try another amount.
        pass

    @unittest.expectedFailure
    def test_withdraw_negative_number(self):
        pass

    @unittest.expectedFailure
    def test_withdraw_not_a_number(self):
        pass

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_withdraw_overdraft(self):
        # Assert that overdraft warning was printed.
        # Assert that account.balance was decremented twice.
        # Assert that `account.log()` was called twice.
        pass

class TestCustomer(unittest.TestCase):
    """Tests the `Customer.Customer` class."""
    def setUp(self):
        accounts = [
            {
                "account_type": "checking",
                "balance": 256.45
            },
            {
                "account_type": "savings",
                "balance": 100467.21
            }
        ]
        self.customer = Customer("0121", "Worf", accounts)

    def test_display_account_choices(self):
        expected_output = (
            "To access your checking account, enter c.\n"
            "To access your savings account, enter s.\n"
            )
        actual_output = self.customer.display_account_choices()
        self.assertEqual(actual_output, expected_output)

    def test_update_account_summary(self):
        expected_summary = [
            "checking: $256.45 available",
            "savings: $100,467.21 available"
        ]
        self.customer.update_account_summary()
        self.assertEqual(self.customer.summary, expected_summary)

    def test_display_account_summary(self):
        self.customer.summary = [
            "Pity the warrior who slays all his foes!",
            "Revenge is a dish best served cold."
        ]
        expected_summary = (
            "Here is your account summary: \n"
            "Pity the warrior who slays all his foes!\n"
            "Revenge is a dish best served cold.\n"
            )
        actual_summary = self.customer.display_account_summary()
        self.assertEqual(actual_summary, expected_summary)


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

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_get_customer_with_short_pin_for_3_attemps(self):
        # Assert that `raw_input` is called 3 additional times and
        # that 'Canceling after 3 attempts' is printed.
        pass

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_get_customer_with_secret_code_xxxx(self):
        # Assert that self.running equals False.
        pass

    @unittest.skip("In progress")
    def test_receipt_1_transaction(self):
        # Stub out `current_customer.update_account_summary()` and confirm it
        # was called.
        pass

    @unittest.skip("In progress")
    def test_receipt_1_transaction(self):
        # Stub out `current_customer.update_account_summary()` and confirm it
        # was called.
        # Assert that 'You made 1 transaction today' was in the final output.
        # Stub out current_customer.display_account_summary() and confirm it
        # was called.
        pass

    @unittest.skip("In progress")
    def test_receipt_multiple_transaction(self):
        # Same as above but check for the plural version.
        pass

    def test_greet_customer(self):
        expected_greeting = (
            "Hello, Worf!\n"
            "Here is your account summary: \n"
            "You fought well today\n"
            "You will continue to fight well tomorrow\n"
            )
        self.confirmPrintStatement(self.session.greet_customer,
            expected_greeting)

    @unittest.skip(REQUEST_CODE_REVIEW)
    def test_proceed(self):
        pass

    @unittest.skip(REQUEST_CODE_REVIEW)
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
