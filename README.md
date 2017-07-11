# Spanning-ATM

## Introduction
This is a command line tool written in Python that simulates an
ATM (Automatic Teller Machine) experience. Both the administrator
(person who sets up the ATM) and customers interact with the ATM through
the command line.

## Setup
- Assume that you have Python 2.7 or higher installed on your computer.
- Clone this repo.
- Sample data lives in the `data` folder.
- In your terminal, navigate into the `app` directory. Run:
```sh
python app.py <path_to_data>
```
For example:
```sh
python app.py data/ds9_data.json
```

## Tests
To run all unit tests, navigate to the `tests` folder. Execute:
```python
python app.py unit_tests.py
```

**Note:** At this time, only unit tests for the individual modules are
included. A full test suite would also include an end-to-end test for
the application named `test_app.py`.

## Extensions
As this is only a partial implementation, there are many extensions to explore.
A sample:
- In real life, a customer would dip their bank card into a slot. The card
reader would retrieve the customer's information based on this unique card
number, *then* ask for the PIN to confirm the customer's identity.
- Banks typically allow a given customer no more than six withdrawals per month from their savings account. How can we introduce this rule?
- This prototype reads in seed data from a JSON file, but the data
schema is relatively flat; would it make more sense to store customer
data in a SQL table? If so, how would we implement that?
- The program currently allows the customer only one chance to enter a number for deposit or withdrawal. It would be useful to add a "button" that would ask the user to confirm the amount and provide an opportunity for re-entering or starting over before proceeding.
- The only transactions allowed at this time are withdrawal and deposit.
Customers with multiple accounts may wish to transfer money between accounts.
- The current user interface is the command line. To make a user-friendly UI, we would look into setting up routes that a front-end framework could access for programming buttons and displays.
- Transaction logging is enabled. A next step would be to give the user options
such as printing a more detailed receipt and viewing recent account activity.
- Many functions in this implementation display error messages to the user such as "Not a valid response. Canceling transaction." However,
a programmer fixing and extending this application might wish to throw actual errors and raise actual exceptions "behind the scenes" for efficient
debugging.
