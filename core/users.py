# This is the control file for users
from core.storage import load_users
def create_user():
    user_data = load_users()
    username = input("Enter username: ")
    if username not in user_data:
        password = input("Create Paassword: ").strip()
        confirm_password = input("Enter Password again to confirm: ").strip()  
        if password == confirm_password:
            user = {
                "username" : username,
                "password" : password
            }
            return user
        else:
            print("Password do not match!")     
    else:
        print("Username already exists")    

def login():
    user_data = load_users()
    username = input("Enter username: ").strip()
    for user in user_data["users"]:
        if username == user["username"]:
            password = input("Enter password: ").strip()
            if password == user["password"]:
                print("Logged In Successfuflly!")
                current_user = user
                return current_user
                break
            else:
                print("Incorrect Password!")   
                return None
        else:
            return None
           