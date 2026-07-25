# 1. Triggers and Description for shell auto-loading
TRIGGERS = ("help", "1")
DESCRIPTION = "Displays all available PyOS commands"

def run(commands_dict):
    """Dynamically prints all loaded commands and their descriptions."""
    print("\nAvailable Commands")
    print("------------------")
    
    # Track functions we've already printed so aliases don't print twice
    seen_functions = set()

    for trigger, func in commands_dict.items():
        if func not in seen_functions:
            seen_functions.add(func)
            
            # Retrieve primary name, triggers, and description attached by shell.py
            triggers = getattr(func, "triggers", (trigger,))
            primary_name = triggers[0]
            desc = getattr(func, "description", "No description available.")
            
            # Format alias list if shortcuts exist (e.g., "(3, cls)")
            aliases = triggers[1:]
            alias_str = f"({', '.join(aliases)})" if aliases else ""
            
            # Print cleanly formatted columns
            print(f"  {primary_name:<14} {alias_str:<12} - {desc}")
            
    print()  # Extra newline for clean spacing
    
