import json
from datetime import datetime

from Customer import Customer

def get_customer(pin):
    """Retrieve customer information by PIN.
    """
    if len(pin) != 4:
        raise ValueError("PIN should have exactly 4 digits.")
    else:
        return CUSTOMERS.get(pin, "That is not a valid PIN. Please try again.")

def get_balance(account):
    return account.balance

def transact(account, transaction_type, amount):
    if transaction_type == "withdraw":
        account.balance -= amount
    elif transaction_type == "deposit":
        account.balance += amount
    else:
        error_message = ("The only available transactions at this time are"
            " 'withdraw' and 'deposit'.")
        raise ValueError(error_message)
    log_entry = {
        "transaction_type": transaction_type,
        "amount": amount,
        "time": datetime.now()
    }
    account.history.append(log_entry)
    print "New balance is {} dollars.".format(account.balance)

def main():
    pin = str(raw_input("Please type your PIN and hit Enter: "))
    current_customer = customers[pin]
    print "Hello, {}!".format(customer.name)
    print current_customer.display_account_summary()
    decision = raw_input("Would you like to perform a transaction? (y/n) ")
    if decision.lower() == "y":
        want_to_transact = True
    elif decision.lower() == "n":
        want_to_transact = False
    else:
        print "You must enter y or n."
    if want_to_transact:
        current_customer.display_account_choices()
        account_choice = raw_input(current_customer.display_account_choices())
        if account_choice.lower() == "c":
            current_account = customer.accounts["checking"]
        elif account_choice.lower() == "s":
            current_account = customer.accounts["savings"]
        elif account_choice.lower() == "m":
            current_account = customer.accounts["money market"]
    print current_account.balance


if __name__ == "__main__":
    # Initialize list of customers.
    customers = {}
    # Read in customer information.
    with open('DS9_data.json') as data:
        customer_list = json.load(data)
        # Store customers by PIN for easy lookup.
        for item in customer_list:
            customers[item["pin"]] = Customer(item["pin"],
                item["name"], item["accounts"])
        for customer in customers.values():
            customer.update_account_summary()
    main()


