from datetime import datetime

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

# TO-DO: Provide option of canceling a transaction or going back.

    def deposit(self):
        # Can deposit any amount
        question = "How much will you be depositing today? "
        deposit_amount = float(raw_input(question))
        # How about reading check images and confirming the amount?
        # How about depositing cash?
        self.balance += deposit_amount
        log_entry = {
            "transaction_type": "deposit",
            "amount": deposit_amount,
            "time": datetime.now()
        }
        self.history.append(log_entry)
        print self.history

    def withdraw(self):
        # Can only withdraw in multiples of 20.
        instructions = ("Enter the amount you wish to withdraw. "
            "It must be a multiple of 20. You may withdraw up to $200: ")
        withdrawal_amount = float(raw_input(instructions))
        if withdrawal_amount > 200:
            raise ValueError("You may not withdraw more than $200 in one session.")
            # But how do I enforce this?
        elif withdrawal_amount % 20 != 0:
            raise ValueError("You must enter a multiple of 20")
        elif self.balance - withdrawal_amount < 0:
            warning = ("This will overdraw your account. "
                "Please withdraw a smaller amount.")
            raise ValueError(warning)
        else:
            self.balance -= withdrawal_amount
            log_entry = {
                "transaction_type": "withdrawal",
                "amount": withdrawal_amount,
                "time": datetime.now()
            }
            self.history.append(log_entry)
            print self.history
