from datetime import datetime
TRIGGERS = ("date", "time", "3")
DESCRIPTION = "Displays current date and time"
def date_time():
    now = datetime.now()
    date_time_format = now.strftime("%B %d, %Y, %I:%M %p")
    print(date_time_format)