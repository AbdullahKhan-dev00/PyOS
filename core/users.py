# This is the control file for users
from core.storage import save_user
def create_user():
    username = input("Enter username: ")
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
    
