from Customer import Customer
from Utils import BOOLEAN_LOOKUP, ACCOUNT_LOOKUP, clean


class Session:
    """Represents an ATM session.

    Every session boots up with a specific data set and the name of a
    specific bank.
    """
    def __init__(self, customer_list, bank_name):
        """
        :param customer_list: A list of dictionaries (likely decoded
            from a raw JSON file) describing each customer at the bank and
            and their starting account balances.
        :type customer_list: ``list`` of ``dict``
        :param bank_name: The name of the bank operating the ATM.
        :type bank_name: ``str``
        """
        self.customers = {}
        self.current_customer = None
        self.bank_name = bank_name
        self.running = True
        for item in customer_list:
            self.customers[item["pin"]] = Customer(
                item["pin"], item["name"], item["accounts"])
        # Store customers by PIN for easy lookup.
        for customer in self.customers.values():
            customer.update_account_summary()

    def display_homescreen(self):
        """The interface returns to this screen between users' turns at
        the ATM.

        :returns: None
        """
        print "Welcome to {}!".format(self.bank_name)

    def get_customer(self, max_attempts=3):
        """"Retrieve a customer object by PIN.

        The secret admin code for shutting down the session is 'xxxx'.

        :param max_attempts: The maximum number of times a user gets to try
            logging in via PIN. Set to 3 by default.
        :type max_attempts: ``int``
        :returns: None
        """
        pin = str(raw_input("To get started, please enter your PIN: "))
        attempts = 0
        while len(pin) != 4:
            warning = "A PIN contains exactly 4 digits. Please try again: "
            pin = str(raw_input(warning))
            attempts += 1
            if attempts >= max_attempts:
                print "Canceling after {} attempts.".format(max_attempts)
                break
        if pin == "xxxx":
            self.running = False
        else:
            # TO-DO: Gracefully handle invalid PIN entries.
            self.current_customer = self.customers.get(pin)

    def receipt(self):
        """Generates a message about the user's banking activities today.

        :returns: A screen-friendly message that states how many transactions
            were executed and displays the updated account balances.
        :return type: ``str``
        """
        # Pull the latest information.
        self.current_customer.update_account_summary()

        # Avoid saying "You made 1 transactions today."
        if self.current_customer.num_transactions == 1:
            message = "You made {} transaction today. \n".format(
            self.current_customer.num_transactions)
        else:
            message = "You made {} transactions today. \n".format(
            self.current_customer.num_transactions)

        # TO-DO: Consider using the accounts' logs to provide a more detailed
        # transaction record.
        message += self.current_customer.display_account_summary()
        return message

    def greet_customer(self):
        """Greets the customer by name after they log in.

        :returns: None
        """
        print "Hello, {}!".format(self.current_customer.name)
        print self.current_customer.display_account_summary()

    def proceed(self, first_time=False):
        """Determines whether the customer wants to perform a transaction.

        :param first_time: Whether or not this is the first time the customer
            is being asked this question.
        :type first_time: ``Boolean``
        :returns: Whether or not the customer indeed wishes to initiate
            a transaction.
        :return type: ``Boolean``
        """
        if first_time:
            question = "Would you like to perform a transaction? (y/n) "
        else:
            question = "Would you like to perform another transaction? (y/n) "
        retry_instructions = "You must enter y or n: "
        answer = clean(raw_input(question))
        attempts = 0

        # A maximum of 3 attempts are allowed.
        while answer not in BOOLEAN_LOOKUP:
            answer = clean(raw_input(retry_instructions))
            attempts += 1
            if attempts >= 3:
                print "Canceling transaction after three attempts."
                break
        if answer in BOOLEAN_LOOKUP:
            return BOOLEAN_LOOKUP[answer]
        else:
            # If the response is nonsense, then assume no.
            print "Not a valid response. Starting over."
            return False

    def serve(self):
        """Guides the customer through the 'meat' of the banking experience
        that follows log in and precedes log out:

            - selecting an account to manage
            - executing transactions in that account (or not)
            - repeating as desired
            - viewing a receipt at the end.

        :returns: None
        """
        wish_to_proceed = self.proceed(first_time=True)
        while wish_to_proceed:
            account_choice = clean(raw_input(
                self.current_customer.display_account_choices()))
            current_account = (self.current_customer.accounts
                [ACCOUNT_LOOKUP[account_choice]])
            current_account.execute_transactions()
            self.current_customer.num_transactions += 1
            wish_to_proceed = self.proceed()
        print self.receipt()

    def logout(self):
        """This is displayed at the end of a customer's turn at the ATM.

        :returns: None
        """
        print "Thank you for banking with {}. Good bye!".format(self.bank_name)
