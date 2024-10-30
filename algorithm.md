# Algorithm Document

1. initialize variables the following variables:
   1. Initial balance equals 1000
   2. SENTINEL equals 'E'
   3. current balance equals initial balance
   4. choice equals ' '
2. create while loop for while choice does not equal SENTINEL:
   1. via the menu function, output to user the different kinds of options they have in the program, which are 
      to view balance, deposit, withdraw or exit. 
   2. ask user to input if they want to view balance, deposit, withdraw or exit
   3. if user entered D:
      1. ask user to input how much they wish to deposit.
      2. call the deposit function, and have the amount user wanted to deposit added to current balance 
   4. if user entered W:
      1. ask user to input how much they wish to withdraw
      2. call the withdraw function, and have the amount user wanted to withdraw subtracted to current balance
      3. if current balance is less than 0:
         1. output to user that their account balance is negative
   5. if user entered V:
      1. output the current balance to the user
   6. if user entered E:
      1. break the loop, and exit the program
   7. else:
      1. output to user that their input was invalid



- Purpose: output to user the different options they have
- Name: menu
- Parameter: none
- Return: none
- Algorithm:
1. output to user list of options they have in the program. options include depositing, withdrawal, viewing balance, and exiting.

- Purpose: ask user to enter the amount they with to either deposit or withdraw
- Name: input amount
- Parameter: none
- Return: integer value of how much user wants to deposit or withdraw
- Algorithm:
1. ask user to input how much they wish to deposit or withdraw
2. if user input is not digits or is less than 0:
   1. return 0
3. else:
   1. return amount user inputted and typecast to integer

- Purpose: calculate addition of value user entered of how much they wish to deposit
- Name: deposit
- Parameter: balance
- Return: updated current balance with amount deposited added
- Algorithm:
1. equal amount to input amount
2. add amount to balance and return result

- Purpose: calculate subtraction of value user entered of how much they wish to withdraw
- Name: withdraw
- Parameter: balance
- Return: updated current balance with amount withdrawn subtracted
- Algorithm: 
1. equal amount to input amount
2. subtract amount to balance and equal result to variable named 'result' 
3. if result is less than 0:
   1. output to user that amount balance is negative
4. return result

- Purpose: allow user to view their balance
- Name: view balance
- Parameter: balance
- Return: none
- Algorithm: 
1. output current balance to user



   

