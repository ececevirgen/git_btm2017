import file_manager as fM

def say_hi():
    print("Welcome to potato bank, how can I help you?")

def new_client():
    new_client = input("...New client name: ")
    if not new_client in fM.get_clients():
        fM.add_client(new_client)
        print("Client added !")
    else:
        print("Client already exist !")
    
def new_transaction():
    pass
    
def look_credit():
    pass
