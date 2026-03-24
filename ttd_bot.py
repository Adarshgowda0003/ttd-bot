import requests
import time

BOT_TOKEN = "8796185442:AAE7w2A1CKsRspCoQCUZwzWTaD0L0R7S0WE"
CHAT_ID = "5361281940"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.get(url, params=params)

def check_tickets():
    url = "https://tirupatibalaji.ap.gov.in"

    try:
        response = requests.get(url)

        if "sold out" not in response.text.lower():
            send_message("🔥 POSSIBLE TTD TICKETS AVAILABLE! CHECK NOW!")
        else:
            print("Still sold out")

    except:
        print("Error checking site")

while True:
    check_tickets()
    time.sleep(60)