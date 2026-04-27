from main import Session


#functions for sign_up,log_in
accounts=[]
def sign_up():
    pass
def log_in():
    name = input("Enter your name:")
    if name.strip() == "":
        print("Please enter a valid name")
        log_in()
    password = input("Enter your password:")
    for x in accounts:
        if x.name == name and x.password == password:
            name = x.name.capitalize()
            Session.our_user = x
            print(f"Welcome our dear user : {name}!")
            return True
    print("Please enter a correct username and password")
    print("If you do not have an account create a new one")
    return False
def my_profile():
    pass