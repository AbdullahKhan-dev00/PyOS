#The shell of PyOS:
from core.commands.help import help
from core.commands.about import about
from core.commands.clear import clear
from core.commands.shutdown import shutdown
def shell():
    commands = input("PyOS> ").lower().strip()
    if commands == "help":
        help()
    elif commands == "about":
        about()
    elif commands == "clear":
        clear()
    elif commands == "shutdown":
        shutdown()       
    else:
        print(f"""Unknown Command: {commands}
Type "help" to see available commands
""")     

        