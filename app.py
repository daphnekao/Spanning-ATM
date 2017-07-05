import json

from Customer import Customer

# Initialize list of customers.
CUSTOMERS = {}

# Read in customer information.
with open('customer_list.json') as customer_file:
    customers = json.load(customer_file)
    # Store customers by PIN for easy lookup.
    for customer in customers:
        CUSTOMERS[customer["pin"]] = Customer(customer["pin"],
            customer["name"], customer["balance"])

def get_customer(pin):
    """Retrieve customer information by PIN.
    """
    if len(pin) != 4:
        raise ValueError("PIN should have exactly 4 digits.")
    else:
        return CUSTOMERS.get(pin, "That is not a valid PIN. Please try again.")

def get_balance(customer):
    return customer.balance

def withdraw(customer, amount):
    customer.balance -= amount
    print "New balance is {} dollars.".format(customer.balance)

def deposit(customer, amount):
    customer.balance += amount
    print "New balance is {} dollars.".format(customer.balance)

# Test
current_customer = CUSTOMERS["0121"]
print get_balance(current_customer)
deposit(current_customer, 325)


