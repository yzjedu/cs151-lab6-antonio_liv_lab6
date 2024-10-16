# Algorithm Document

1. Output a welcome message explaining the purpose of the program.

2. Initialize variables:
    - `INITIAL_BALANCE = 1000`
    - `current_balance = INITIAL_BALANCE`
    - `SENTINEL = 'E'` (to exit the loop)
    - `choice = ''` (to store user’s menu choice)

- Name: view_balance
- Parameter: none
- Return: current balance
3. Define function view_balance():
   1. Output current_balance to user.

- Name: deposit 
- Parameter: how much money is being deposited
- Return: updated balance
4. Define function deposit():
    1. Prompt the user to enter the amount to deposit.
       2. Check if the deposit amount is a valid positive integer:
            1. Convert the input to an integer.
            1. If the amount is positive, add it to `current_balance`.
            1. Display the new balance to the user.
       3. otherwise:
             1. Output an error message requesting a valid positive number.

- Name: withdraw
- Parameter: how much money is being withdrawn
- Return: updated balance
5. Define function withdraw():
   1. Prompt the user to enter the amount to withdraw.
       2. Check if the withdrawal amount is a valid positive integer:
            1. Convert the input to an integer.
            1. If the amount is positive, subtract it from `current_balance`.
            1. Display the new balance to the user.
            1. If the `current_balance` becomes negative:
                 1.  Output a warning message indicating that the user will be charged 5% interest.
          3. otherwise:
             1. Output an error message requesting a valid positive number.


- Name: exit
- Parameter: none
- Return: exit message
6. Define function exit(): 
    1. Output a message thanking the user and indicate the program is ending.

- Name: error_checking
- Parameter: none
- Return: error message
7. Define function error_checking():
   1. Output an error message requesting a valid option (D, W, V, or E).

- Name: main
- Parameter: none
- Return: none
8. Define function main():
    1. Start a while loop that continues until the user enters 'E' to exit:
       1. Display the menu options:
           - `D - Deposit`
           - `W - Withdraw`
           - `V - View Balance`
           - `E - Exit`
       2. Prompt the user to input their choice and convert it to uppercase.
    1. if user enters 'D':
       2. Call deposit()
    1. elif user enters 'W':
       2. Call withdraw()
    1. elif user enters 'V':
       2. Call view_balance:
    1. elif user enters 'E':
       2. Call exit():
    1. else:
       2. Call error_checking():