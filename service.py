import time
from utils import clear_screen

def create_database():
    account = {
        "available": 0.00, 
        "envelopes": {"Food": 0.00, "Transport": 0.00},
        "transactions": {}
    }
    return account



def log_expense(user_db, env, amt):
    try:
        envelope = list(user_db["envelopes"].keys())[env-1]
        user_db["envelopes"][envelope] += amt
        print(f"{amt:.2f} has been added to {envelope}!")
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



def log_transaction(user_db, type, amt, env):
    pass