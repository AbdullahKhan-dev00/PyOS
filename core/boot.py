from core.shell import shell
import time

def boot_screen():
    print("""
    ===========      
    PyOS v0.1.0
    ===========
   """)
    print("Loading kernel...")
    time.sleep(2)
    print("Loading filesystem...") 
    time.sleep(2)
    print("Loading users...")
    time.sleep(2)
    print("Starting shell...")
    time.sleep(3)
    print("""Welcome to PyOS!
    Type "help" to see available commands""")
    
    while True:
        shell()


