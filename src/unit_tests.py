"""
"""

import unittest
import Utils
# from Account import Account
# from Customer import Customer
# from Session import Session

class TestAccount(unittest.TestCase):
    def test_execute_transactions(self):
        pass

    def test_log(self):
        pass

    def test_report_transaction_success(self):
        pass

    def test_deposit(self):
        pass

    def test_withdraw(self):
        pass

class TestCustomer(unittest.TestCase):
    def test_display_account_choices(self):
        pass

    def test_update_account_summary(self):
        pass

    def test_display_account_summary(self):
        pass

class TestSession(unittest.TestCase):
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
    def test_clean(self):
        self.assertEqual(Utils.clean(" Black Power "), "black power")

    def test_dollar(self):
        self.assertEqual(Utils.dollar(54602.3), "$54,602.30")

if __name__ == "__main__":
    unittest.main()
