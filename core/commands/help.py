from rich.table import Table
from core.rich_ui import console, show_boot_banner, get_input, show_welcome, print_error, print_success


# 1. Triggers and Description for shell auto-loading
TRIGGERS = ("help", "1")
DESCRIPTION = "Displays all available PyOS commands"

def run(commands_dict):
    """Dynamically prints all loaded commands and their descriptions using Rich."""
    table = Table(
        title="PyOS Available Commands", 
        border_style="cyan", 
        header_style="bold magenta",
        expand=False
    )
    
    table.add_column("Command", style="bold green", no_wrap=True, justify="left")
    table.add_column("Aliases", style="yellow", justify="left")
    table.add_column("Description", style="white", justify="left")
    
    # Track functions we've already printed so aliases don't print twice
    seen_functions = set()

    for trigger, func in commands_dict.items():
        if func not in seen_functions:
            seen_functions.add(func)
            
            # Retrieve primary name, triggers, and description attached by shell.py
            triggers = getattr(func, "triggers", (trigger,))
            primary_name = triggers[0]
            desc = getattr(func, "description", "No description available.")
            
            # Format alias list if shortcuts exist
            aliases = triggers[1:]
            alias_str = f"({', '.join(aliases)})" if aliases else ""
            
            table.add_row(primary_name, alias_str, desc)
            
    console.print(table)
    console.print()  # Extra spacing
    
