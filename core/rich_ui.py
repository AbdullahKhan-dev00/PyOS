from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

# ---------------------------------------------------------
# PALETTE CONSTANTS
# ---------------------------------------------------------
CYAN = "#00f0ff"     # Neon Cyan
PURPLE = "#a100ff"   # Electric Purple
GREEN = "#00ff66"    # Cyber Green
RED = "#ff0055"      # Crimson Red
YELLOW = "#ffbe00"   # Amber Yellow
GRAY = "#5c5c5c"     # Muted Slate Gray


def show_boot_banner():
    console.clear()
    
    # Stylized Header
    banner_art = (
        "██████╗ ██╗   ██╗██████╗ ███████╗\n"
        "██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝\n"
        "██████╔╝ ╚████╔╝ ██║  ██║███████╗\n"
        "██╔═══╝   ╚██╔╝  ██║  ██║╚════██║\n"
        "██║        ██║   ██████╔╝███████║\n"
        "╚═╝        ╚═╝   ╚═════╝ ╚══════╝"
    )
    
    banner = Text(banner_art, style=f"bold {CYAN}")
    banner.append("\n\n  [ v0.1.0 - Modular Kernel Architecture ]", style="dim white")
    
    panel = Panel(
        banner,
        title=f"[{PURPLE}]● SYSTEM BOOT ●[/{PURPLE}]",
        subtitle=f"[{CYAN}]STATUS: ONLINE[/{CYAN}]",
        border_style=PURPLE,
        box=box.ROUNDED,
        padding=(1, 4)
    )
    console.print(panel)


def show_welcome():
    welcome_msg = Text()
    welcome_msg.append("Welcome to PyOS!\n", style="bold white")
    welcome_msg.append("Type ", style="dim white")
    welcome_msg.append('"help"', style=f"bold {CYAN}")
    welcome_msg.append(" to see available commands.", style="dim white")

    console.print(
        Panel(
            welcome_msg,
            title=f"[{GREEN}]✓ SUCCESS[/{GREEN}]",
            border_style=GREEN,
            box=box.ROUNDED,
            expand=False
        )
    )


def print_error(msg):
    console.print(f"[{RED}]🗙 [-] {msg}[/{RED}]")


def print_success(msg):
    console.print(f"[{GREEN}]✔ [+] {msg}[/{GREEN}]")


def get_input(username="root"):
    # Mac / Unix terminal style prompt: username@pyos:~ $
    prompt_str = (
        f"[{PURPLE}]{username}[/{PURPLE}]"
        f"[{GRAY}]@[/{GRAY}]"
        f"[{CYAN}]pyos[/{CYAN}]"
        f":[{YELLOW}]~[/{YELLOW}] $ "
    )
    return console.input(prompt_str)