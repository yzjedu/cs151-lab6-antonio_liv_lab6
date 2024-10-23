#Liv Oakes and Antonio
#Dr. Yalew
#CS151
#10/23/24
#Lab 6
#Purpose: Create an atm program where the user can enter D: deposit, W: Withdraw, V: View balance, E: Exit
#         and the program will do as prompted and output the updated balance.

initial_balance = 1000
current_balance = initial_balance
sentinel = 'E'.lower()
choice = ''

#deposit function
def deposit(current_balance):
    deposit_amount = int(input('Enter amount to deposit: '))
    if deposit_amount > 0:
         current_balance += deposit_amount
         print(f'Your balance is {current_balance} dollars.')
    else:
        input('Please enter a positive amount.')

#withdraw function
def withdraw(current_balance):
    withdraw_amount = int(input('Enter amount to withdraw: '))
    if withdraw_amount > 0:
           current_balance -= withdraw_amount
           print(f'Your balance is {current_balance} dollars.')
    elif current_balance < 0:
            print('Your balance is negative, you will be charged 5 % interest')
    else:
           input('Please enter a positive amount.')

#view balance function
def view_balance(current_balance):
    print(current_balance)

#exit function
def exit():
    print('Thank you!')

#error check function
def error():
    choice = input('Please enter:  D: deposit, W: Withdraw, V: View balance, E: Exit: ')

#main function
def main():
        while True:
            print('\nD - Deposit \nW - Withdraw \nV - View balance \nE - Exit ')
            choice = input('Please select an option: ').lower()
            if choice == 'd' or choice == 'deposit':
                deposit(current_balance)
            elif choice == 'w' or choice == 'withdraw':
                withdraw(current_balance)
            elif choice == 'v' or choice == 'view balance':
                view_balance(current_balance)
            elif choice == 'e' or choice == 'exit':
                exit()
                break
            else:
                error()
main()






