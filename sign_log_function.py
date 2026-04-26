from main import Session


#functions for sign_up,log_in
accounts=[]
def sign_up():
    global our_user
    try:
        name=input("Enter your name: ")
        if name.strip() == "":
            print("Please enter your name")
            sign_up()
        else:
            password=input("Enter your password: ")
            if password.strip() == "":
                print("Please enter your password")
                password=input("Enter your password: ")
            else:
                while True:
                    if password==name:
                        print("Password can not be as same as name")
                        password=input("Enter your password: ")
                    elif len(password)< 8:
                        print("Password must be 8 or more characters long")
                    else:
                        new_user = Account()
                        new_user.name=name
                        new_user.password=password
                        pass
    except ValueError:
         print("Please try again")
         sign_up()
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