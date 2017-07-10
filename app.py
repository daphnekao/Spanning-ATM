import json
import argparse

from Session import Session

def main():
    # TO-DO: Provide option of reading in any data file, not just the DS9 one.
    with open('DS9_data.json') as data:
        customer_list = json.load(data)
        session = Session(customer_list)
    session.display_homescreen()




    decision = raw_input(first_transaction_question).strip().lower()
    if decision in TRANSLATOR:
        want_to_transact = TRANSLATOR[decision]
    else:
        print "You must enter y or n."
    while want_to_transact:
        account_choice = raw_input(current_customer.display_account_choices()).strip().lower()
        current_account = current_customer.accounts[ATM.TRANSLATOR[account_choice]]
        current_account.execute_transactions()
        want_to_transact = raw_input(subsesquent_transaction_question).strip().lower()
    print "Thank you for banking with Austin Community Bank. Good bye!"
    # How do I exit the program?

if __name__ == "__main__":
    main()


