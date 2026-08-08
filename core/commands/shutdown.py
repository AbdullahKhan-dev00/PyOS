import sys
import time
from rich.console import Console

console = Console()

TRIGGERS = ("shutdown", "quit", "exit", "6")
DESCRIPTION = "Shutdowns the PyOS"

def run():
    console.print("\n[bold yellow][!] Initiating system shutdown sequence...[/bold yellow]")
    
    # Optional short delay for effect
    time.sleep(0.5) 
    
    console.print("[dim white]Stopping processes and unmounting modules...[/dim white]")
    console.print("[bold red][-] PyOS has stopped.[/bold red]")
    console.print("[bold cyan]Goodbye![/bold cyan]\n")
    
    sys.exit(0)