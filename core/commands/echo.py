from core.rich_ui import console, CYAN, YELLOW

TRIGGERS = ("echo", "print", "say")
DESCRIPTION = "Prints user text or arguments back to the terminal"

def run(args=None):
    # Handles execution whether args are passed or prompted
    if not args:
        text = console.input(f"[{CYAN}]echo > [/{CYAN}]").strip()
    elif isinstance(args, (list, tuple)):
        text = " ".join(args)
    else:
        text = str(args)

    if text:
        console.print(f"[{YELLOW}]{text}[/{YELLOW}]")