codes = {
    "checking": "c",
    "savings": "s",
    "money market": "m"
}

class Account:
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.code = codes[account_type]
        self.balance = balance
        self.history = []
