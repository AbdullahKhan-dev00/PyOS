import importlib
import pkgutil
import core.commands

# The active command registry
COMMANDS = {}

def load_commands():
    """Scans core/commands/ and populates the COMMANDS registry."""
    COMMANDS.clear()
    
    for _, module_name, _ in pkgutil.iter_modules(core.commands.__path__):
        full_module_name = f"core.commands.{module_name}"
        module = importlib.import_module(full_module_name)
        
        triggers = getattr(module, "TRIGGERS", (module_name,))
        run_func = getattr(module, "run", None)
        
        if run_func:
            # Attach description & triggers for help.py to inspect dynamically
            setattr(run_func, "description", getattr(module, "DESCRIPTION", "No description."))
            setattr(run_func, "triggers", triggers)

            for trigger in triggers:
                COMMANDS[trigger.lower()] = run_func

# Automatically load commands ONCE when shell.py is imported by boot.py
load_commands()


def shell():
    """Gets user input and dispatches the command (called repeatedly by boot.py)."""
    user_input = input("PyOS> ").lower().strip()
    
    if not user_input:
        return

    handler = COMMANDS.get(user_input)
    
    if handler:
        # Pass COMMANDS dict if run() accepts arguments (like help.py does)
        handler(COMMANDS) if handler.__code__.co_argcount > 0 else handler()
    else:
        print(f'Unknown Command: "{user_input}"\nType "help" to see available commands\n')

        