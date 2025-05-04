import time

def send_reminders():
    print("English: Hello! Time to take your medication.")
    print("Español: ¡Hola! Es hora de tomar su medicamento.")
    print("বাংলা: ওষুধ খাওয়ার সময় হয়ে গেছে।")

# Example: Remind every 8 hours
def start_reminder_loop(interval_hours=8):
    while True:
        send_reminders()
        print("Reminder sent. Waiting for next...")
        time.sleep(interval_hours * 3600)  # Convert hours to seconds

# Start the reminder loop
start_reminder_loop()
