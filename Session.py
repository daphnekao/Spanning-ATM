from Utils import BOOLEAN_LOOKUP, ACCOUNT_LOOKUP
from Customer import Customer
from Format import clean, dollar
# Should Utils and Format be combined?

class Session:
    def __init__(self, customer_list):
        """
        :param customer_list:
        :type customer_list: ``list``
        """
        self.customers = {}
        self.current_customer = None
        for item in customer_list:
            self.customers[item["pin"]] = Customer(item["pin"],
                item["name"], item["accounts"])
        # Store customers by PIN for easy lookup.
        for customer in self.customers.values():
            customer.update_account_summary()

    def display_homescreen(self):
        print "Welcome to Austin Community Bank!"

    def get_customer(self, pin):
        """Retrieve customer information by PIN."""
        if len(pin) != 4:
            raise ValueError("PIN should have exactly 4 digits.")
        else:
            return self.customers.get(pin,
                "That is not a valid PIN. Please try again.")

    def receipt(self):
        if self.current_customer.num_transactions == 1:
            message = "You made {} transaction today. \n".format(
            self.current_customer.num_transactions)
        else:
            message = "You made {} transactions today. \n".format(
            self.current_customer.num_transactions)
        message += self.current_customer.display_account_summary()
        return message

    def login(self):
        # In real life, this would be a credit card number, and we would
        # confirm via PIN
        pin = str(raw_input("To get started, please enter your PIN: "))
        self.current_customer = self.get_customer(pin)
        print "Hello, {}!".format(self.current_customer.name)
        print self.current_customer.display_account_summary()

    def proceed(self, first_time=False):
        """:rtype: ``Boolean``
        """
        if first_time:
            question = "Would you like to perform a transaction? (y/n) "
        else:
            question = "Would you like to perform another transaction? (y/n) "
        retry_instructions = "You must enter y or n: "
        # TO-DO: Eliminate overlap with Account.execute_transactions()
        answer = clean(raw_input(question))
        attempts = 0
        while answer not in BOOLEAN_LOOKUP:
            answer = clean(raw_input(retry_instructions))
            attempts +=1
            if attempts >= 3:
                print "Canceling transaction after three attempts."
                break
                return
        if answer in BOOLEAN_LOOKUP:
            return BOOLEAN_LOOKUP[answer]
        else:
            print "Not a valid response. Canceling transaction."
            return
    def serve(self):
        # Count number of transactions. (Do I need this?)
        decision = self.proceed(first_time=True)
        while decision is True:
            account_choice = clean(raw_input(self.current_customer.display_account_choices()))
            current_account = self.current_customer.accounts[ACCOUNT_LOOKUP[account_choice]]
            current_account.execute_transactions()
            decision = self.proceed()
            self.current_customer.num_transactions += 1
        print self.receipt()

    def logout(self):
        print "Thank you for banking with Austin Community Bank. Good bye!"

