import json
import argparse

from Session import Session

def open_session(path_to_data):
    """Opens a new ATM session with specific seed data.

    :param path_to_data: The relative path to the JSON file.
    :type path_to_data: ``str``

    :returns: A session file containing customers' information from
        the specified JSON file.
    :return type: :py:class:`Session.Session`
    """
    with open(path_to_data) as data:
        customer_list = json.load(data)
        return Session(customer_list, "Austin Community Bank")

def main(path_to_data):
    """Main point of entry for the application.
    Customers are invited to approach the ATM and do their banking through it.
    When prompted for a PIN, an admin user who knows the secret code 'xxxx'
    can enter this code at any time to shut down the program.
    """
    session = open_session(path_to_data)
    while session.running:
        session.display_homescreen()
        session.get_customer()
        if not session.running:
            print "Shutting down."
            break
        session.greet_customer()
        session.serve()
        session.logout()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_data", type=str,
        help="Path to data file for ATM session")
    args = parser.parse_args()
    main(args.path_to_data)
