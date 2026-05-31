import time
from utils import clear_screen, get_current_date, num_count

def create_database():
    account = {
        "available": 0.00, 
        "envelopes": {},
        "transactions": {}
    }
    return account



def log_expense(user_db, env, amt, purp):
    try:
        envelope = list(user_db["envelopes"].keys())[env-1]
        user_db["envelopes"][envelope] += amt
        print(f"{amt:.2f} has been added to {envelope}!")

        user_db = log_transaction(user_db, "Expense", amt, envelope, purp)
        time.sleep(1.5)
    except IndexError:
        print("User choice not in range! Kindly try again")
    
    return user_db



def view_envelopes(user_db):
    try:
        envelopes = list(user_db["envelopes"].keys())
    except KeyError:
        envelopes = None
        
    if envelopes:
        for i, envelope in enumerate(envelopes, start=1):
            print(f"\t{i}. {envelope.title()} - {user_db["envelopes"][envelope]:.2f}")
    else:
        print("No envelopes available to display")
    return user_db



def add_income(user_db, amt, sender=""):
    try:
        user_db["available"] += amt
        clear_screen()
        print(f"{amt:.2f} added to Available!")

        user_db = log_transaction(user_db, "Add Income", amt, purpose=sender)
        time.sleep(1.5)
    except KeyError:
        print("Invalid!")
    return user_db



def display_available(user_db):
    try:
        avail = user_db["available"]
        print(f"Available: {avail:.2f}")
    except KeyError:
        pass

    return user_db



def envelope_loop(user_db):
    try:
        envelopes = list(user_db["envelopes"].keys())
    except KeyError:
        envelopes = None
        
    if envelopes:
        for envelope in envelopes:
            clear_screen()
            print(f"{envelope.title()} - {user_db["envelopes"][envelope]:.2f}")
            amt = float(input("Amount to add: "))
            user_db["envelopes"][envelope] += amt
            user_db["available"] -= amt
        clear_screen()
        print("All amounts have been added!")
        time.sleep(1.5)
    else:
        print("No envelopes available to display")
    
    return user_db



def envelope_transfer(user_db, frm, to, amt):
    try:
        if amt > user_db["envelopes"][frm]:
            print("Insufficient funds to complete this transaction!")
        else:
            user_db["envelopes"][frm] -= amt
            user_db["envelopes"][to] += amt
            print(f"{amt:.2f} transferred from '{frm}' to '{to}'")
    except KeyError:
        print("Invalid! Try again")

    return user_db



def log_transaction(user_dtb, trans_type, amount, env="", purpose=""):
    transactions = user_dtb["transactions"]
    id = num_count(transactions)
    date = get_current_date()
    example = list()

    if trans_type == "Expense":
        example.extend([trans_type, amount, env, purpose, date])
    elif trans_type == "Add Income":
        example.extend([trans_type, amount, purpose, date])
    else:
        example.extend([trans_type, amount, date])
    
    transactions[id] = example
    return user_dtb



def view_transactions(user_db):
    transactions = user_db["transactions"]

    if transactions:
        for i, value in enumerate(list(transactions.values())[::-1], start=1):
            print(f"{i}.")
            print(f"Transaction type: {value[0]}")
            print(f"Amount: {value[1]}")
            if value[0] == "Expense":
                try: 
                    print(f"Envelope: ")
                    print(f"Purpose: ")
                except:
                    pass
            elif value[0] == "Add Income":
                try:
                    print(f"Received from: {value[2]}")
                except:
                    pass
            print(f"Date: {value[-1]}\n\n")

    else:
        print("No transactions yet!")
    
    return user_db