#The shell of PyOS:
from core.commands.help import help
from core.commands.about import about
from core.commands.clear import clear
from core.commands.shutdown import shutdown
from core.commands.version import version
from core.commands.date_time import date_time
from core.users import create_user
from core.storage import save_user
def shell():
    commands = input("PyOS> ").lower().strip()
    if commands in  {"help", "1"}:
        help()
    elif commands in {"about", "2"}:
        about()
    elif commands in {"clear", "3", "cls"}:
        clear()
    elif commands in {"shutdown", "quit", "4"}:
        shutdown()
    elif commands in {"version", "5"}:
         version()  
    elif commands in {"date.time", "6"}:
          date_time()
    elif commands in {"create_user", "7"}:
          save_user(create_user())
    else:
        print(f"""Unknown Command: {commands}
Type "help" to see available commands
""")     

        