# ATM Source Code


## Improvements:
- Many functions in this implementation display error messages to the user such
as "Not a valid response. Canceling transaction." However, a programmer fixing
and extending this application might wish to throw actual errors and raise
actual exceptions "behind the scenes" for efficient debugging.

- There are several blocks like the following scattered among the modules,
none of them standardized:
```python
        attempts = 0
        while answer not in ["w", "d", "x"]:
            answer = clean(raw_input(retry_instructions))
            attempts += 1
            if attempts >= 3:
                print "Canceling transaction after three attempts."
                break
                return
```
It would be a worthwhile exercise to abstract this behavior. For example, we
could try writing a decorator called `retry()` that would take in a
`max_attempts` argument, then decorate any action allowing more than one try.

- The application is currently small enough to hold the main method,
all modules, and all tests in one folder. However, as it grows, we will need
to introduce cleaner folder structure--perhaps two subfolders called `tests`
and `lib` to start out.

-At this time, only unit tests for the individual modules are
included. A full test suite would also include an end-to-end test for
the application named `test_app.py`.


## Extensions
As this is only a partial implementation, there are many extensions to explore.
A sample:

- In real life, a customer would dip their bank card into a slot. The card
reader would retrieve the customer's information based on this unique card
number, *then* ask for the PIN to confirm the customer's identity.

- Banks typically allow a given customer no more than six withdrawals per month
from their savings account. How can we introduce this rule?

- This prototype reads in seed data from a JSON file, but the data
schema is relatively flat; would it make more sense to store customer
data in a SQL table? If so, how would we implement that?

- The program currently allows the customer only one chance to enter a number
for deposit or withdrawal. We could ask the user to confirm or correct the
amount before proceeding.

- The only transactions allowed at this time are withdrawal and deposit.
Customers with multiple accounts may wish to transfer money between accounts.

- The current user interface is the command line. To make a user-friendly UI,
we would set up routes that a front-end framework could access for programming
buttons and displays.

- Transaction logging is enabled. A next step would be to give the user options
such as printing a more detailed receipt and viewing recent account activity.
