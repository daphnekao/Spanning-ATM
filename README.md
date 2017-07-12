# Spanning-ATM
This is a command line tool written in Python that simulates an
ATM (Automatic Teller Machine) experience. Both the administrator
(person who sets up the ATM) and customers interact with the ATM through
the command line.

## Setup
1. You must have Python 2.7.2 or higher installed on your computer (any Mac
will suffice, for example).

1. Clone or download this repository.

1. In your terminal, navigate into the `src` directory. Run:
```sh
python app.py <path_to_data>
```
where `path_to_data` points to the seed data that you want to initialize an
ATM session with. For example:
```sh
python app.py ../data/DS9_data.json
```

## Interacting with the Program
Once the application is up and running, multiple customers can log in with
their PIN numbers and log out when they are done banking. However, if you are
privy to a secret admin code, then you can shut down the session entirely. This
code is "xxxx"; enter it the next time the program prompts you for a PIN.

## Data
Two seed data sets live in the `data` folder. The program will ingest any JSON
file that meets the spec exemplified in these files.

Here are the PINs for the Deep Space Nine crew:

| Name          | PIN  |
| ------------- |:----:|
| Benjamin Sisko| 0333 |
| Odo           | 5922 |
| Quark         | 7843 |
| Jadzia Dax    | 4477 |
| Julian Bashir | 2325 |
| Miles O'Brien | 0420 |
| Kira Nerys    | 6196 |

And here are the PINs for the Next Generation crew:

| Name            | PIN  |
| -------------   |:----:|
| Jean-Luc Picard | 4145 |
| Worf            | 0121 |
| William T. Riker| 8508 |
| Deanna Troi     | 7777 |
| Data            | 2748 |
| Geordi La Forge | 1132 |
| Beverly Crusher | 5221 |
| Guinan          | 3873 |


## Tests
To run all unit tests, stay in the `src` folder and execute:
```sh
python unit_tests.py
```

