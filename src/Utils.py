"""A collection of helper methods and dictionaries."""

# These dictionaries interpret user entries.
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
    """Strips leading and trailing white space from a given string and
    converts it entirely to lowercase.

    :return type: ``str``
    """
    return string.strip().lower()

def dollar(amount):
    """Formats a number to a string representation of a dollar amount.

    :param amount: Number to be formatted for pretty printing.
    :type amount: ``float`` or ``int``
    :returns: A pretty rendition of the amount with a dollar sign, commas,
        and two decimal places.
    :return type: ``str``
    """
    return "$" + format(amount, '0,.2f')
