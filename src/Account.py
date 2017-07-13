"""This module contains data about accounts and methods for updating them.
"""

from datetime import datetime

from Utils import BOOLEAN_LOOKUP, clean, dollar

# Maps account types to one-word abbreviations for easy user input.
CODES = {
    "checking": "c",
    "savings": "s",
    "money market": "m"
}

# These are used below in the `execute_transactions()` method.
TRANSACTION_INSTRUCTIONS = (
    "To make a withdrawal, press w. \n"
    "To make a deposit, press d. \n"
    "To cancel, press x. \n"
    )
TRANSACTION_RETRY_INSTRUCTIONS = "You must enter w, d or x. Try again: "

# This is used below in the `report_transaction_success()` method.
VERBS = {
    "deposit": "deposited",
    "withdrawal": "withdrew"
}

# As we introduce more fees, we may wish to store them in a dictionary.
OVERDRAFT_FEE = 33


class Account:
    """Represents a customer's account."""
    def __init__(self, account_type, balance):
        """
        :param account_type: The supported types at this time are 'checking',
            'savings', and 'money market'.
        :type account_type: ``str``
        :param balance: The amount of money sitting in the account.
        :type balance: ``float``
        """
        self.account_type = account_type

        # Lowercase letter that a customer would enter to access the account.
        self.code = CODES[account_type]
        self.balance = balance
        self.history = []  # A list of dictionaries

    def execute_transactions(self):
        """Guides a customer through the process of making transactions.
        **Note**: The only transactions available at this time are deposits
        and withdrawals.

        :returns: None
        """
        # TO-DO: What if the user presses a number or other weird character?
        # Handle these errors gracefully.
        answer = clean(raw_input(TRANSACTION_INSTRUCTIONS))
        attempts = 0
        while answer not in ["w", "d", "x"]:
            answer = clean(raw_input(TRANSACTION_RETRY_INSTRUCTIONS))
            attempts += 1
            if attempts >= 3:
                print "Canceling transaction after 3 attempts."
                break
        if answer == "w":
            self.withdraw()
        elif answer == "d":
            self.deposit()
        elif answer == "x":
            print "Canceling transaction."
        else:
            print "Not a valid response. Canceling transaction."

    def log(self, transaction_type, amount):
        """Adds an entry to the account's activity log.

        One log entry is a small dictionary describing the transaction and
        its time stamp.

        :param transaction_type: 'withdrawal' or 'deposit'
        :type transaction_type: ``str``
        :param amount: The amount deposited or withdrawn.
        :type amount: ``float``

        :returns: None
        """
        log_entry = {
            "transaction_type": transaction_type,
            "amount": dollar(amount),
            "time": str(datetime.now())
        }
        self.history.append(log_entry)

    def report_transaction_success(self, transaction_type, amount):
        """Generates a sentence confirming that the transaction went through.

        :param transaction_type: 'withdrawal' or 'deposit'
        :type transaction_type: ``str``
        :param amount: The amount deposited or withdrawn.
        :type amount: ``float``

        :returns: A message confirming that the balance was adjusted correctly.
        :return type: ``str``
        """
        if transaction_type in VERBS:
            report = "Successfully {} {}. New balance: {}".format(
                VERBS[transaction_type], dollar(amount), dollar(self.balance))
        else:
            warning = (
                "The only transaction types available at this time "
                "are 'deposit' and 'withdrawal'."
                )
            raise ValueError(warning)
        return report

    def deposit(self):
        """Guides the customer through depositing any amount into the account.

        This activity is logged.
        TO-DO: May wish to prevent customer from deposit extremely large
        amounts, zero amounts, and negative amounts.

        :returns: None
        """
        question = "How much will you be depositing today? "
        deposit_amount = float(raw_input(question))
        self.balance += deposit_amount
        print self.report_transaction_success("deposit", deposit_amount)
        self.log("deposit", deposit_amount)

    def withdraw(self):
        """Guides the customer through withdrawing money from the account.

        Some restrictions:
            - Can only withdraw in multiples of 20.
            - Withdrawal amount must be between $20 and $200, inclusive.
            - Overdrafts are allowed, but they incur a fixed fee.

        :returns: None
        """
        instructions = (
            "Enter the amount you wish to withdraw. \n"
            "It must be a multiple of $20. You may withdraw up to $200. \n"
            "To cancel this transaction, press x: \n"
            )
        response = raw_input(instructions)
        if type(response) == str and clean(response) == "x":
            print "Transaction canceled."
            return
        else:
            withdrawal_amount = float(response)
            difference = self.balance - withdrawal_amount
            # TO-DO (Bug Fix): The program shuts down if the customer does not
            # comply with the $200 limit or the multiple of $20 rule. Add a
            # while loop to allow them to continue banking in other ways.
            if withdrawal_amount > 200:
                print "You may not withdraw more than $200 in one session."
            elif withdrawal_amount % 20 != 0:
                print "You must enter a multiple of $20"
            elif difference < 0:
                # TO-DO: What if the account is overdrawn to begin with?
                warning = (
                    "This would overdraw your account by {} and "
                    "incur an overdraft fee of {}. "
                    "Are you sure you want to continue? (y/n) ".format(
                        dollar(abs(difference)), dollar(OVERDRAFT_FEE))
                    )
                answer = clean(raw_input(warning))
                proceed_anyway = BOOLEAN_LOOKUP[answer]
                if proceed_anyway:
                    self.balance -= withdrawal_amount
                    print self.report_transaction_success("withdrawal",
                        withdrawal_amount)
                    self.log("withdrawal", withdrawal_amount)
                    self.balance -= OVERDRAFT_FEE
                    overdraft_warning = (
                        "Deducted additional $33. "
                        "Your account is overdrawn please make a "
                        "deposit soon."
                        )
                    print overdraft_warning
                    self.log("overdraft fee", OVERDRAFT_FEE)
            else:
                self.balance -= withdrawal_amount
                print self.report_transaction_success("withdrawal",
                    withdrawal_amount)
                self.log("withdrawal", withdrawal_amount)
