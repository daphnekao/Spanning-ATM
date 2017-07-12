"""A collection of helper methods and dictionaries.
"""

BOOLEAN_LOOKUP = {
    "y": True,
    "n": False
}

ACCOUNT_LOOKUP = {
    "c": "checking",
    "s": "savings",
    "m": "money market"
}

def clean(string):
    return string.strip().lower()

def dollar(amount):
    return "$" + format(amount, '0,.2f')
