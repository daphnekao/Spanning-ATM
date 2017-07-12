import json
import argparse

from Session import Session

def open_session(path_to_data):
    """
    """
    with open(path_to_data) as data:
        customer_list = json.load(data)
        return Session(customer_list)

def main(path_to_data):
    """(Summary)
    Customers are invited to approach the ATM and do their banking through it.
    When prompted for a PIN, an admin user who knows the secret code 'xxxx'
    can enter this code at any time to shut down the program.
    """
    session = open_session(path_to_data)
    while session.running:
        session.display_homescreen()
        if not session.running:
            print "Shutting down."
            break
        session.login()
        session.serve()
        session.logout()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_data", type=str,
        help="Path to data file for ATM session")
    args = parser.parse_args()
    main(args.path_to_data)
