import time
from storage import save_records, load_records
from utils import clear_screen, exit
from service import create_database, log_expense, add_income, envelope_transfer, view_envelopes, display_available, envelope_loop


user_database = load_records()


def check_records(data):
    if data:
        data = records_menu(data)
    else:
        data = create_database()
    return data



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
    


def main_menu(data):
    data = check_records(data)
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
                    add_transaction_menu(data)
                elif user_choice == 2:
                    envelope_transfer_menu(data)
                elif user_choice == 3:
                    manage_envelopes_menu(data)
                elif user_choice == 4:
                    view_transactions_menu(data)
                elif user_choice == 5:
                    exit()

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)



def add_transaction_menu(data):
    while True:
        clear_screen()
        print("Select transaction type")
        print(" 1. Log expense")
        print(" 2. Add income")
        print(" 3. Fill from available")
        print(" 0. Back")

        try:
            user_choice = int(input("\nYour choice: "))

            if user_choice not in range(0, 4):
                clear_screen()
                print("User choice not in range! Kindly try again")
                time.sleep(1)
            else:
                if user_choice == 1:
                    log_expense_menu(data)
                elif user_choice == 2:
                    add_income_menu(data)
                elif user_choice == 3:
                    fill_from_available_menu(data)
                elif user_choice == 0:
                    return

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)



def log_expense_menu(user_data):
    while True:
        clear_screen()
        print("Select envelope\n")
        user_data = view_envelopes(user_data)
        print("\n 0. Back")

        try:
            envelope_num = int(input("\nYour choice: "))
            if envelope_num == 0:
                return

            clear_screen()
            amount = float(input("Enter amount: "))

            user_data = log_expense(user_data, envelope_num, amount)
            return user_data

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)



def add_income_menu(user_data):
    while True:
        clear_screen()
        try:
            amount = float(input("Enter amount: "))
            clear_screen()
            received_from = input("Received from: ").title()

            user_data = add_income(user_data, amount, received_from)
            return user_data

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)



def fill_from_available_menu(user_data):
    while True:
        clear_screen()
        user_data = display_available(user_data)
        try:
            user_choice = input("\nProceed to fill each envelope? (y/n): ").lower().strip()

            if user_choice == "y":
                user_data = envelope_loop(user_data)
            elif user_choice == "n":
                return

        except ValueError:
            clear_screen()
            print("Invalid input! Try again")
            time.sleep(1)



def envelope_transfer_menu(user_data):
    while True:
        clear_screen()
        print("Your envelopes\n")
        user_data = view_envelopes(user_data)
        try:
            user_choice = input("\nWant to proceed with transfer? (y/n): ").lower().strip()

            if user_choice == "y":
                clear_screen()
                from_envelope = input("From: ").title().strip()
                to_envelope = input("To: ").title().strip()
                amount = float(input("Enter amount: "))

                user_data = envelope_transfer(user_data, from_envelope, to_envelope, amount)
                return user_data
            
            elif user_choice == "n":
                return

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
    main_menu(user_database)