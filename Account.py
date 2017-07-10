from datetime import datetime

codes = {
    "checking": "c",
    "savings": "s",
    "money market": "m"
}

overdraft_fee = 33

class Account:
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.code = codes[account_type]
        self.balance = balance
        self.history = []

    def execute_transactions(self):
        instructions = ("To make a withdrawal, press w. \n"
            "To make a deposit, press d. \n"
            "To cancel, press x. \n")
        retry_instructions = "You must enter w, d or x. Try again: "
        # What if the user presses a number, instead?
        transaction_decision = raw_input(instructions).strip().lower()
        attempts = 0
        while transaction_decision not in ["w", "d", "x"]:
            transaction_decision = raw_input(retry_instructions)
            attempts += 1
            if attempts >= 3:
                print "Canceling transaction after three attempts."
                break
                return
        if transaction_decision == "w":
            self.withdraw()
        elif transaction_decision == "d":
            self.deposit()
        elif transaction_decision == "x":
            print "Canceling transaction."
            return
        else:
            message = "Input must be w, d, or x. Canceling transaction."
            # TO-DO: Return to home screen
            raise ValueError(message)
            return

    def log(self, transaction_type, amount):
        log_entry = {
            "transaction_type": transaction_type,
            "amount": amount,
            "time": datetime.now()
        }
        self.history.append(log_entry)

    def report_transaction_success(self, amount):
        report = "Successfully deposited {}. New balance: {}".format(amount,
            self.balance)
        return report

    def deposit(self):
        # Can deposit any amount
        question = "How much will you be depositing today? "
        deposit_amount = float(raw_input(question))
        # How about reading check images and confirming the amount?
        # How about depositing cash?
        self.balance += deposit_amount
        print self.report_transaction_success(deposit_amount)
        self.log("deposit", deposit_amount)

    def withdraw(self):
        # Can only withdraw in multiples of 20.
        instructions = ("Enter the amount you wish to withdraw. "
            "It must be a multiple of 20. You may withdraw up to $200. "
            "To cancel this transaction, press x: ")
        response = raw_input(instructions)
        if type(response) == str and response.strip().lower() == "x":
            print "Transaction canceled."
            return
        else:
            withdrawal_amount = float(response)
            if withdrawal_amount > 200:
                raise ValueError("You may not withdraw more than $200 in one session.")
                # But how do I enforce this?
            elif withdrawal_amount % 20 != 0:
                raise ValueError("You must enter a multiple of 20")
            # Handle overdrafts. Continue or don't?
            elif self.balance - withdrawal_amount < 0:
                warning = ("This will overdraw your account. "
                    "Please withdraw a smaller amount.")
                raise ValueError(warning)
            else:
                self.balance -= withdrawal_amount
                print self.report_transaction_success(withdrawal_amount)
                self.log("withdrawal", withdrawal_amount)
