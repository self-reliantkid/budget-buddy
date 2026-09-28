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
        user_db["envelopes"][envelope]["balance"] -= amt
        print(f"Expense logged successfully!")

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
    except TypeError:
        envelopes = None
        
    if envelopes:
        yn = True
        for i, envelope in enumerate(envelopes, start=1):
            print(f'\t{i}. {envelope.title()} - (Balance: {user_db["envelopes"][envelope]["balance"]:.2f}) - (Weekly Budget: {user_db["envelopes"][envelope]["budget"]:.2f})')
    else:
        print("No envelopes available to display")
        yn = False

    return user_db, yn, len(envelopes)



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
            print(f'{envelope.title()} - {user_db["envelopes"][envelope]["balance"]:.2f}')
            
            add_bgt = input("Add budgeted amount? (y/n): ").strip().lower()

            if add_bgt == "y":
                user_db["envelopes"][envelope]["balance"] += user_db["envelopes"][envelope]["budget"]
                user_db["available"] -= user_db["envelopes"][envelope]["budget"]
            else:
                clear_screen()
                amt = float(input("Amount to add: "))
                user_db["envelopes"][envelope]["balance"] += amt
                user_db["available"] -= amt
        clear_screen()
        print("All amounts have been added!")
        time.sleep(1.5)
    else:
        print("No envelopes available to display")
    
    return user_db



def envelope_transfer(user_db, frm, to, amt):
    try:
        envelopes_list = list(user_db["envelopes"].keys())
        from_env = envelopes_list[frm - 1]
        to_env = envelopes_list[to - 1]
    
        if amt > user_db["envelopes"][from_env]["balance"]:
            print("Insufficient funds to complete this transaction!")
        elif amt < 0:
            print("Negative funds cannot be transferred!")
        elif frm == to:
            print("Cannot transfer to same envelope!")
        else:
            user_db["envelopes"][to_env]["balance"] += amt
            user_db["envelopes"][from_env]["balance"] -= amt
            print(f"{amt:.2f} transferred from '{from_env}' to '{to_env}'")

            user_db = log_transaction(user_db, "Envelope Transfer", amt, None, None, from_env, to_env)

    except IndexError:
        print("Invalid! Try again")

    return user_db



def log_transaction(user_dtb, trans_type, amount, env="", purpose="", f_env="", t_env=""):
    transactions = user_dtb["transactions"]
    id = num_count(transactions)
    date = get_current_date()
    example = list()

    if trans_type == "Expense":
        example.extend([trans_type, amount, env, purpose, date])
    elif trans_type == "Add Income":
        example.extend([trans_type, amount, purpose, date])
    elif trans_type == "Envelope Transfer":
        example.extend([trans_type, amount, f_env, t_env, date])
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
                    print(f"Envelope: {value[2]}")
                    print(f"Purpose: {value[3]}")
                except:
                    pass

            elif value[0] == "Add Income":
                try:
                    print(f"Received from: {value[2]}")
                except:
                    pass

            elif value[0] == "Envelope Transfer":
                try:
                    print(f"From: {value[2]}")
                    print(f"To: {value[3]}")
                except:
                    pass

            print(f"Date: {value[-1]}\n\n")

    else:
        print("No transactions yet!")
    
    return user_db



def add_envelope(user_db, env_name, wk_budget):
    try:
        envelopes = user_db["envelopes"]

        if env_name in list(envelopes.keys()):
            print("Envelope already exists!")

        else:
            envelopes[env_name] = {}

            envelopes[env_name]["balance"] = 0.00
            envelopes[env_name]["budget"] = wk_budget

            clear_screen()
            print("Envelope created successfully!")
            time.sleep(1.3)
    except:
        pass
    return user_db



def edit_envelope_name(user_db, env, n_name):
    try:
        envelopes = list(user_db["envelopes"].keys())
        envelope = envelopes[env-1]

        if n_name in envelopes:
            print("Cannot edit envelope name to already existing envelope!")
        else:
            user_db["envelopes"] = {(n_name if k == envelope else k): v for k, v in user_db["envelopes"].items()}

    except IndexError:
        print("User choice not in range! Kindly try again")

    return user_db



def edit_envelope_budget(user_db, env, n_budget):
    try:
        envelope = list(user_db["envelopes"].keys())[env-1]
        user_db["envelopes"][envelope]["budget"] = n_budget

    except IndexError:
        print("User choice not in range! Kindly try again")

    return user_db



def delete_envelope(user_db, env):
    try:
        envelope = list(user_db["envelopes"].keys())[env-1]

        if user_db["envelopes"][envelope]["balance"] > 0:
            user_db["available"] += user_db["envelopes"][envelope]["balance"]
            print(f"{envelope} successfully deleted! All remaining funds transferred to Available")
        elif user_db["envelopes"][envelope]["balance"] < 0:
            user_db["available"] -= user_db["envelopes"][envelope]["balance"]
            print(f"{envelope} successfully deleted! Negative balance deducted from Available")
        else:
            print(f"{envelope} successfully deleted!")

        del user_db["envelopes"][envelope]

    except IndexError:
        print("User choice not in range! Kindly try again")

    return user_db