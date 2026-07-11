from core.shell import shell

def boot_screen():
    print("""
    ===========      
    PyOS v0.1.0
    ===========
    Loading kernel...
    Loading filesystem...
    Loading users...
    Starting shell...

    Welcome to PyOS!
    Type "help" to see available commands
    """)
    while True:
        shell()


