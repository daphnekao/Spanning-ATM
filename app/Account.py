from datetime import datetime

from Format import clean, dollar
from Utils import BOOLEAN_LOOKUP

CODES = {
    "checking": "c",
    "savings": "s",
    "money market": "m"
}

OVERDRAFT_FEE = 33

class Account:
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.code = CODES[account_type]
        self.balance = balance
        self.history = []

    def execute_transactions(self):
        instructions = ("To make a withdrawal, press w. \n"
            "To make a deposit, press d. \n"
            "To cancel, press x. \n")
        retry_instructions = "You must enter w, d or x. Try again: "
        # What if the user presses a number, instead?
        answer = clean(raw_input(instructions))
        attempts = 0
        while answer not in ["w", "d", "x"]:
            answer = clean(raw_input(retry_instructions))
            attempts += 1
            if attempts >= 3:
                print "Canceling transaction after three attempts."
                break
                return
        if answer == "w":
            self.withdraw()
        elif answer == "d":
            self.deposit()
        elif answer == "x":
            print "Canceling transaction."
            return
        else:
            message = "Not a valid response. Canceling transaction."
            # TO-DO: Return to home screen
            print message
            return

    def log(self, transaction_type, amount):
        log_entry = {
            "transaction_type": transaction_type,
            "amount": dollar(amount),
            "time": str(datetime.now())
        }
        self.history.append(log_entry)

    def report_transaction_success(self, transaction_type, amount):
        if transaction_type == "deposit":
            report = "Successfully deposited {}. New balance: {}".format(
                dollar(amount), dollar(self.balance))
        elif transaction_type == "withdrawal":
            report = "Successfully withdrew {}. New balance: {}".format(
                dollar(amount), dollar(self.balance))
        else:
            warning = ("The only transaction types available at this time "
                "are 'deposit' and 'withdrawal'.")
            raise ValueError(warning)
        return report

    def deposit(self):
        # Can deposit any amount
        question = "How much will you be depositing today? "
        deposit_amount = float(raw_input(question))
        # How about reading check images and confirming the amount?
        # How about depositing cash?
        self.balance += deposit_amount
        print self.report_transaction_success("deposit", deposit_amount)
        self.log("deposit", deposit_amount)

    def withdraw(self):
        # Can only withdraw in multiples of 20.
        instructions = ("Enter the amount you wish to withdraw. \n"
            "It must be a multiple of $20. You may withdraw up to $200. \n"
            "To cancel this transaction, press x: \n")
        response = raw_input(instructions)
        if type(response) == str and clean(response) == "x":
            print "Transaction canceled."
            return
        else:
            withdrawal_amount = float(response)
            difference = self.balance - withdrawal_amount
            # TO-DO: Wrap this in a while loop with opportunities to try again.
            # Can I use try-except clauses here?
            if withdrawal_amount > 200:
                # TO-DO: But how do I enforce this?
                print "You may not withdraw more than $200 in one session."
            elif withdrawal_amount % 20 != 0:
                print "You must enter a multiple of $20"
            # Handle overdrafts. Ask customer if they want to continue or not.
            elif difference < 0:
                warning = ("This would overdraw your account by {} and "
                    "incur an overdraft fee of {}. Are you sure you want to continue? (y/n) ".format(dollar(abs(difference)), dollar(OVERDRAFT_FEE)))
                answer = clean(raw_input(warning))
                proceed_anyway = BOOLEAN_LOOKUP[answer]
                if proceed_anyway:
                    self.balance -= withdrawal_amount
                    print self.report_transaction_success("withdrawal", withdrawal_amount)
                    self.log("withdrawal", withdrawal_amount)
            else:
                # TO-DO: eliminate redundancy.
                self.balance -= withdrawal_amount
                print self.report_transaction_success("withdrawal", withdrawal_amount)
                self.log("withdrawal", withdrawal_amount)
