def create_database():
    account = { 
        "envelopes": {},
        "transactions": {}
    }
    return account



def log_expense(user_db, env, amt):
    try:
        envelope = list(user_db["envelopes"].keys())[env]
    except IndexError:
        print("User choice not in range! Kindly try again")
    
    user_db["envelopes"][envelope] += amt