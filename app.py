import json
from datetime import datetime

from Customer import Customer

# Initialize list of customers.
CUSTOMERS = {}

# Read in customer information.
with open('customer_list.json') as customer_file:
    customers = json.load(customer_file)
    # Store customers by PIN for easy lookup.
    for customer in customers:
        CUSTOMERS[customer["pin"]] = Customer(customer["pin"],
            customer["name"], customer["accounts"])

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

# Test
current_customer = CUSTOMERS["0333"]
savings_account = current_customer.accounts["savings"]
money_market_account = current_customer.accounts["money market"]
checking_account = current_customer.accounts["checking"]
print get_balance(money_market_account)
transact(money_market_account, "withdraw", 300.25)
transact(money_market_account, "deposit", 1000.56)


