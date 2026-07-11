#The shell of PyOS:
from core.commands.help import help
from core.commands.about import about
from core.commands.clear import clear
from core.commands.shutdown import shutdown
from core.commands.version import version
from core.commands.date_time import date_time
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
    elif commands == "version":
         version()  
    elif commands == "date.time":
          date_time()
    else:
        print(f"""Unknown Command: {commands}
Type "help" to see available commands
""")     

        