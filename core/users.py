from core.storage import load_users, save_user
from core.rich_ui import console, print_error, print_success

def create_user(default_username=None):
    console.print("\n[bold cyan]=== CREATE NEW USER ===[/bold cyan]")
    user_data = load_users() 
    
    # Pre-fill username if coming from failed login prompt
    if default_username:
        username = default_username
        console.print(f"Creating user: [bold yellow]{username}[/bold yellow]")
    else:
        username = console.input("[bold cyan]Enter new username:[/] ").strip()
    
    if not username:
        print_error("Username cannot be empty!")
        return None

    existing_users = [u["username"] for u in user_data.get("users", [])]
    
    if username not in existing_users:
        password = console.input("[bold yellow]Create Password:[/] ", password=True).strip()
        confirm_password = console.input("[bold yellow]Confirm Password:[/] ", password=True).strip()  
        
        if password and password == confirm_password:
            new_user = {
                "username": username,
                "password": password
            }
            save_user(new_user)
            print_success(f"User '{username}' created successfully!")
            return new_user
        else:
            print_error("Passwords do not match or field was empty!")     
    else:
        print_error("Username already exists!")
    
    return None

def login():
    console.print("\n[bold magenta]=== PyOS SYSTEM LOGIN ===[/bold magenta]")
    user_data = load_users()
    
    username = console.input("[bold cyan]login as:[/] ").strip()
    
    if not username:
        print_error("Username cannot be empty!")
        return None
    
    # Check if user exists
    for user in user_data.get("users", []):
        if username == user["username"]:
            # Give 3 attempts for password
            for attempts_left in range(3, 0, -1):
                password = console.input("[bold yellow]password:[/] ", password=True).strip()
                if password == user["password"]:
                    print_success(f"Welcome back, {username}!\n")
                    return user
                else:
                    if attempts_left - 1 > 0:
                        print_error(f"Access Denied: Incorrect Password! ({attempts_left - 1} attempt(s) remaining)")
                    else:
                        print_error("Access Denied: Maximum attempts reached!")
            return None
                
    # User not found -> Ask to create a new user
    print_error(f"User '{username}' not found!")
    choice = console.input("[bold yellow]Would you like to create this account? (y/n):[/] ").strip().lower()
    
    if choice in ("y", "yes"):
        return create_user(default_username=username)
    else:
        console.print("[dim white]Login aborted.[/dim white]")
        return None