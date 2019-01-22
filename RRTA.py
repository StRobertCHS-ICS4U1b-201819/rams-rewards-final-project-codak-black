
def check_Account():
    try:
        login()
    except FileNotFoundError:
        print("Sorry this account does not exist please create new account")
        signUp()


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    check = open(username + ".txt", "r")
    if check.mode == 'r':
        contents = check.read()
    if contents == password:
        print("login successful")
    else:
        print("Sorry wrong Password. Please try again")

def signUp():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    createAccount = open(username + ".txt", "w+")
    createAccount.write(password)

check_Account()