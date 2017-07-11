import json
import argparse

from Session import Session

def open_session(path_to_data):
    with open(path_to_data) as data:
        customer_list = json.load(data)
        return Session(customer_list)

def main(path_to_data):
    # TO-DO: Allow multiple customers to use ATM in same session, not just one.
    # Admin boots up a session with a specific customer database.
    session = open_session(path_to_data)
    # Customers are invited to approach the ATM and do their banking through it.
    session.display_homescreen()
    session.login()
    session.serve()
    session.logout()
    session.display_homescreen()
    # TO-DO: Right now, as soon as the customer enters "n", the terminal
    # prints the good by message and exits the program entirely. We need to
    # keep it open for the next user.
    # The Admin can shut down the session at any time.

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_data", type=str,
        help="Path to data file for ATM session")
    args = parser.parse_args()
    main(args.path_to_data)
