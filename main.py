#Liv Oakes and Antonio
#Dr. Yalew
#CS151
#10/23/24
#Lab 6
#Purpose: Create an atm program where the user can enter D: deposit, W: Withdraw, V: View balance, E: Exit
#         and the program will do as prompted and output the updated balance.

INITIAL_BALANCE = 1000
SENTINEL = 'E'

def menu():
    print("\nPlease select an option:"
          "\n\t D - Deposit"
          "\n\t W - Withdraw"
          "\n\t V - View Balance"
          "\n\t E - Exit")

def deposit(balance):
    amount = input_amount()
    return balance + amount

def withdraw(balance):
    amount = input_amount()
    result = balance - amount
    if result < 0:
        print('Your balance is negative')
    return result

def input_amount():
    amount = input('Enter the amount: ')
    if not amount.isdigit() or int(amount) < 0:
        return 0
    else:
        return int(amount)

#view balance function
def view_balance(balance):
    print(f'Your current balance is {balance:.2f}')

#main function
def main():

    current_balance = INITIAL_BALANCE
    choice = ''

    while choice != SENTINEL:

        menu()
        choice = input('Enter your choice: ').upper().strip()

        if choice == 'D':
            current_balance = deposit(current_balance)
        elif choice == 'W':
            current_balance = withdraw(current_balance)
        elif choice == 'V':
            view_balance(current_balance)
        elif choice == 'E':
            exit(0)
        else:
            print('Invalid choice')

main()






