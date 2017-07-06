from Account import Account

class Customer:
    def __init__(self, pin, name, account_list):
        self.pin = pin
        self.name = name
        self.accounts = {}

        # De-serialize account information.
        for account in account_list:
            self.accounts[account["type"]] = (Account(account["type"],
                account["balance"]))

