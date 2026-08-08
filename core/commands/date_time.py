from datetime import datetime
from zoneinfo import ZoneInfo
from core.rich_ui import console, CYAN, YELLOW

TRIGGERS = ("date", "time", "datetime", "3")
DESCRIPTION = "Displays current system date and time"

def run():
    # Set explicitly to PKT (Asia/Karachi)
    now = datetime.now(ZoneInfo("Asia/Karachi"))
    formatted = now.strftime("%A, %B %d, %Y | %I:%M %p")
    
    console.print(f"[{CYAN}]🕒 System Clock:[/{CYAN}] [{YELLOW}]{formatted}[/{YELLOW}]")