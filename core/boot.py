import time
from core.shell import shell
from core.users import login, create_user
from core.rich_ui import console, show_boot_banner, get_input, show_welcome, print_error, print_success

def boot_screen():
    show_boot_banner()
    
    with console.status("[bold green]Loading kernel...", spinner="dots"):
        time.sleep(1)
    with console.status("[bold green]Loading filesystem...", spinner="dots"):
        time.sleep(1)
    with console.status("[bold green]Loading users...", spinner="dots"):
        time.sleep(1)
        
    current_user = login()     
    
    if current_user:
        show_welcome()
        while True:
            shell(current_user)