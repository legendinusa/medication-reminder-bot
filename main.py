import time
import json
import os

def load_message(language_code):
    filepath = f"locales/{language_code}.json"
    if not os.path.exists(filepath):
        filepath = "locales/en.json"  # fallback to English
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("reminder", "Time to take your medication.")

def send_reminder(message):
    print(f">>> {message}")

def start_reminder_loop(language="en", interval_hours=8):
    message = load_message(language)
    while True:
        send_reminder(message)
        print("Reminder sent. Waiting for next...\n")
        time.sleep(interval_hours * 3600)

# Example usage
if __name__ == "__main__":
    user_language = input("Enter language code (en, bn, es): ").strip().lower()
    start_reminder_loop(language=user_language)
