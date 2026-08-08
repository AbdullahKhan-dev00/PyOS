import importlib
import pkgutil
import shlex
import core.commands
from core.rich_ui import console, show_boot_banner, get_input, show_welcome, print_error, print_success

COMMANDS = {}

def load_commands():
    COMMANDS.clear()
    
    console.print("[dim white][*] Scanning kernel modules...[/dim white]")
    
    for _, module_name, _ in pkgutil.iter_modules(core.commands.__path__):
        full_module_name = f"core.commands.{module_name}"
        module = importlib.import_module(full_module_name)
        
        triggers = getattr(module, "TRIGGERS", (module_name,))
        run_func = getattr(module, "run", None)
        
        if run_func:
            setattr(run_func, "description", getattr(module, "DESCRIPTION", "No description."))
            setattr(run_func, "triggers", triggers)

            for trigger in triggers:
                COMMANDS[trigger.lower()] = run_func

    print_success(f"Loaded {len(COMMANDS)} command triggers into memory.\n")

load_commands()


def shell(active_user):
    """Gets user input using the active user's username for the prompt."""
    username = active_user.get("username", "root") if isinstance(active_user, dict) else "root"
    
    # Renders: username@pyos:~ $
    user_input = get_input(username).strip()
    
    if not user_input:
        return

    # Split command from arguments safely (preserving quoted strings)
    try:
        parts = shlex.split(user_input)
    except ValueError:
        parts = user_input.split()

    cmd_name = parts[0].lower()
    args = parts[1:]

    handler = COMMANDS.get(cmd_name)
    
    if handler:
        # If run() expects arguments (like echo or help)
        if handler.__code__.co_argcount > 0:
            # Pass args if available, otherwise fallback to COMMANDS dict for help.py
            if args:
                handler(args)
            else:
                handler(COMMANDS)
        else:
            handler()
    else:
        print_error(f'Command not found: "{cmd_name}"')
        console.print('[dim white]Type [bold cyan]"help"[/bold cyan] to list all registered system commands.[/dim white]\n')