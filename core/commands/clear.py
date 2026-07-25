import os
TRIGGERS = ("clear", "cls", "5")
DESCRIPTION = "Clears the terminal"
def run():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')    