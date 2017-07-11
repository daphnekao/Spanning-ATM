from Account import Account
from Format import clean, dollar

class Customer:
    def __init__(self, pin, name, account_list):
        self.pin = pin
        self.name = name
        self.accounts = {}
        self.summary = []
        self.num_transactions = 0

        # De-serialize account information.
        for item in account_list:
            self.accounts[item["account_type"]] = Account(item["account_type"],
                item["balance"])

    def display_account_choices(self):
        message = ""
        for key, value in self.accounts.iteritems():
            instruction = "To access your {} account, enter {}.\n".format(key,
                value.code)
            message += instruction
        return message

    def update_account_summary(self):
        for account in self.accounts.values():
            funds_available_statement = "{}: {} available".format(
                account.account_type, dollar(account.balance))
            self.summary.append(funds_available_statement)

    def display_account_summary(self):
        message = "Here is your account summary: \n"
        for statement in self.summary:
            message = message + statement + "\n"
        return message



