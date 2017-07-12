from Account import Account
from Utils import dollar


class Customer:
    """Represents a customer."""
    def __init__(self, pin, name, account_list):
        """
        :param pin: The customer's unique PIN
        :type pin: ``str``
        :param name: The customer's full name
        :type name: ``str``
        :param account_list: A list of small dictionaries specifying the type
            (checking, savings, money market) and balance of each account under
            the customer's name. This is has already been decoded from the
            raw JSON.
        :type account_list: ``list`` of ``dict``
        """
        self.pin = pin
        self.name = name
        self.accounts = {}  # A list of dictionaries
        self.summary = []  # A list of dictionaries
        self.num_transactions = 0

        # Instantiate `Account.Account` objects with the balance information
        # attached to the customer's name in the raw data.
        for item in account_list:
            self.accounts[item["account_type"]] = Account(
                item["account_type"], item["balance"])

    def display_account_choices(self):
        """Generates a prompt so the customer can choose which account to
        work in.

        :returns: A multiple choice set that gets fed to a `raw_input()`
            function later.
        :return type: ``str``
        """
        message = ""
        for key, value in self.accounts.iteritems():
            instruction = "To access your {} account, enter {}.\n".format(
                key, value.code)
            message += instruction
        return message

    def update_account_summary(self):
        """For each account, adds a line stating the balance to the
        `Customer`'s summary list for later processing.

        :returns: None
        """
        # First clear out any outdated information before proceeding.
        self.summary = []
        for account in self.accounts.values():
            funds_available_statement = "{}: {} available".format(
                account.account_type, dollar(account.balance))
            self.summary.append(funds_available_statement)

    def display_account_summary(self):
        """Prints every line in the `Customer`'s summary list.

        :returns: A screen-ready summary of all account balances.
        :return type: ``str``
        """
        message = "Here is your account summary: \n"
        for statement in self.summary:
            message = message + statement + "\n"
        return message
