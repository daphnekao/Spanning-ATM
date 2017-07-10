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


first_transaction_question = "Would you like to perform a transaction? (y/n) "
subsesquent_transaction_question = ("Would you like to perform another "
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

    def login(self):
        # In real life, this would be a credit card number, and we would
        # confirm via PIN
        pin = str(raw_input("To get started, please enter your PIN: "))
        self.current_customer = self.get_customer(pin)
        print "Hello, {}!".format(self.current_customer.name)
        print self.current_customer.display_account_summary()
        self.current_customer = self.get_customer()

    def logout(self):
        pass

