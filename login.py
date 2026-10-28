# Login Module with Authentication
def login():
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "1234":
        print("Access Granted")
    else:
        print("Access Denied")