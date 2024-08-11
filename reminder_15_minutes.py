import time
from datetime import datetime, timedelta
from reminder import get_time_input
        
def main():
    task = input("Enter your task: ")
    reminder_time = get_time_input()
    
    # Get the current date and set the reminder datetime
    now = datetime.now()
    reminder_datetime = datetime.combine(now.date(), reminder_time)
    
    # Check if the reminder time is in the past for the current day, if so, set it for the next day
    if reminder_datetime < now:
        reminder_datetime += timedelta(days=1)
    
    reminder_datetime_15min_before = reminder_datetime - timedelta(minutes=15)
    
    print(f"You will be reminded {reminder_datetime_15min_before} 15 minutes before at {reminder_datetime.strftime('%Y-%m-%d %I:%M')}")
    
    # Wait until 15 minutes before the reminder time
    while True:
        now = datetime.now()
        if now >= reminder_datetime_15min_before:
            print(f"Your task '{task}' is due in 15 minutes!")
            time.sleep(1)  
            time.sleep(15 * 60)
            print(f"Reminder: You have a task '{task}' now at {reminder_time.strftime('%I:%M')}")
            # time.sleep(900)
            break        
 