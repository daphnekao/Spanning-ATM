import json

from Customer import Customer

def get_customer(pin):
    """Retrieve customer information by PIN.
    """
    if len(pin) != 4:
        raise ValueError("PIN should have exactly 4 digits.")
    else:
        return CUSTOMERS.get(pin, "That is not a valid PIN. Please try again.")


def transact(account, transaction_type, amount):
    if transaction_type == "withdraw":
        account.balance -= amount
    elif transaction_type == "deposit":
        account.balance += amount
    else:
        error_message = ("The only available transactions at this time are"
            " 'withdraw' and 'deposit'.")
        raise ValueError(error_message)

    account.history.append(log_entry)
    print "New balance is {} dollars.".format(account.balance)

def main():
    translator = {
        "y": True,
        "n": False,
        "c": "checking",
        "s": "savings",
        "m": "money market",
        "w": "withdraw",
        "d": "deposit"
    }

    pin = str(raw_input("Please type your PIN and hit Enter: "))
    current_customer = customers[pin]
    print "Hello, {}!".format(current_customer.name)
    print current_customer.display_account_summary()

    first_transaction_question = ("Would you like to perform a "
        "transaction? (y/n) ")
    subsesquent_transaction_question = ("Would you like to perform another "
        "transaction? (y/n) ")

    decision = raw_input(first_transaction_question).strip().lower()
    if decision in translator:
        want_to_transact = translator[decision]
    else:
        print "You must enter y or n."
    while want_to_transact:
        account_choice = raw_input(current_customer.display_account_choices()).strip().lower()
        current_account = current_customer.accounts[translator[account_choice]]
        current_account.execute_transactions()
        want_to_transact = raw_input(subsesquent_transaction_question).strip().lower()
    print "Thank you, good bye!"

if __name__ == "__main__":
    # Initialize list of customers.
    customers = {}
    # Read in customer information.
    # TO-DO: Provide option of reading in any data file, not just the DS9 one.
    with open('DS9_data.json') as data:
        customer_list = json.load(data)
        # Store customers by PIN for easy lookup.
        for item in customer_list:
            customers[item["pin"]] = Customer(item["pin"],
                item["name"], item["accounts"])
        for customer in customers.values():
            customer.update_account_summary()
    main()


