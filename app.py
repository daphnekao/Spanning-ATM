import json
import argparse

from Session import Session

def open_session(path_to_data):
    with open(path_to_data) as data:
        customer_list = json.load(data)
        return Session(customer_list)

def main(path_to_data):
    session = open_session(path_to_data)
    session.display_homescreen()
    session.login()
    session.serve()
    session.logout()
    session.display_homescreen()
    # How do I exit the program?

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_data", type=str,
        help="Path to data file for ATM session")
    args = parser.parse_args()
    main(args.path_to_data)


