from Customer import Customer

TRANSLATOR = {
    "y": True,
    "n": False,
    "c": "checking",
    "s": "savings",
    "m": "money market",
    "w": "withdraw",
    "d": "deposit"
}


FIRST_TRANSACTION_QUESTION = "Would you like to perform a transaction? (y/n) "
SUBSEQUENT_TRANSACTION_QUESTION = ("Would you like to perform another "
        "transaction? (y/n) ")
# Need to allow multiple users to log in and log out.

class Session:
    def __init__(self, customer_list):
        self.customers = {}
        self.current_customer = None

        with open(customer_list) as data:
            for item in customer_list:
                self.customers[item["pin"]] = Customer(item["pin"],
                    item["name"], item["accounts"])
            # Store customers by PIN for easy lookup.
            for customer in customers.values():
                customer.update_account_summary()


    def display_homescreen(self):
        print "Welcome to Austin Community Bank!"

    def get_customer(self, pin):
    """Retrieve customer information by PIN.
    """
    if len(pin) != 4:
        raise ValueError("PIN should have exactly 4 digits.")
    else:
        return self.customers.get(pin,
            "That is not a valid PIN. Please try again.")

    def print_receipt(self):
        # TO-DO: Maybe list the transactions that occurred today.
        print "Please take your receipt."

    def login(self):
        # In real life, this would be a credit card number, and we would
        # confirm via PIN
        pin = str(raw_input("To get started, please enter your PIN: "))
        self.current_customer = self.get_customer(pin)
        print "Hello, {}!".format(self.current_customer.name)
        print self.current_customer.display_account_summary()
        self.current_customer = self.get_customer()

    def serve(self):
        decision = raw_input(FIRST_TRANSACTION_QUESTION).strip().lower()
        if decision in TRANSLATOR:
            want_to_transact = TRANSLATOR[decision]
        else:
            print "You must enter y or n."
        while want_to_transact:
            account_choice = raw_input(current_customer.display_account_choices()).strip().lower()
            current_account = current_customer.accounts[TRANSLATOR[account_choice]]
            current_account.execute_transactions()
            want_to_transact = raw_input(SUBSEQUENT_TRANSACTION_QUESTION).strip().lower()

    def logout(self):
        print "Thank you for banking with Austin Community Bank. Good bye!"

