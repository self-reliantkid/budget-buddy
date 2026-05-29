import time
from storage import save_records, load_records
from utils import clear_screen, exit
from service import create_database, log_expense


user_database = load_records()


def check_records(data):
    if data:
        data = records_menu(data)
    main_menu()



def records_menu(state):
    while True:
        clear_screen()
        print("Saved records found! Want to retrieve?")
        print(" 1. Yes")
        print(" 2. No")

        try:
            user_choice = int(input("\nYour choice: "))

            if user_choice not in range(1, 3):
                clear_screen()
                print("User choice not in range! Kindly try again")
                time.sleep(1)
            else:
                if user_choice == 1:
                    return state
                elif user_choice == 2:
                    state = create_database()
                    return state

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)
    


def main_menu():
    while True:
        clear_screen()
        print("Welcome to Budget Buddy!")
        print(" 1. Add transaction")
        print(" 2. Envelope transfer")
        print(" 3. Manage envelopes")
        print(" 4. View transactions")
        print(" 5. Exit")

        try:
            user_choice = int(input("\nYour choice: "))

            if user_choice not in range(1, 6):
                clear_screen()
                print("User choice not in range! Kindly try again")
                time.sleep(1)
            else:
                if user_choice == 1:
                    add_transaction_menu()
                elif user_choice == 2:
                    envelope_transfer_menu()
                elif user_choice == 3:
                    manage_envelopes_menu()
                elif user_choice == 4:
                    view_transactions_menu()
                elif user_choice == 5:
                    exit()

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)



def add_transaction_menu():
    while True:
        clear_screen()
        print("Select transaction type")
        print(" 1. Log expense")
        print(" 2. Add income")
        print(" 3. Fill from available")

        try:
            user_choice = int(input("\nYour choice: "))

            if user_choice not in range(1, 4):
                clear_screen()
                print("User choice not in range! Kindly try again")
                time.sleep(1)
            else:
                if user_choice == 1:
                    log_expense_menu(user_database)
                elif user_choice == 2:
                    add_income_menu()
                elif user_choice == 3:
                    fill_from_available_menu()

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)



def log_expense_menu(user_data):
    while True:
        clear_screen()
        print("Select envelope")
        try:
            envelope_num = int(input("\nYour choice: "))
            amount = float("Enter amount: ")

            log_expense(user_data, envelope_num, amount)

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)



def add_income_menu():
    while True:
        clear_screen()
        try:
            amount = float(input("Enter amount: "))
            received_from = input("From: ")

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)



def fill_from_available_menu():
    pass



def envelope_transfer_menu():
    while True:
        clear_screen()
        try:
            from_envelope = input("From: ")
            to_envelope = input("To: ")
            amount = float(input("Enter amount: "))

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)




def manage_envelopes_menu():
    pass



def view_transactions_menu():
    pass



if __name__ == "__main__":
    clear_screen(0)
    check_records(user_database)