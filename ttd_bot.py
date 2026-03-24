import requests
import time


BOT_TOKEN = "8796185442:AAE7w2A1CKsRspCoQCUZwzWTaD0L0R7S0WE"
CHAT_ID = "5361281940"

last_sent = False

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.get(url, params=params)

def check_tickets():
    global last_sent

    url = "https://tirupatibalaji.ap.gov.in"

    try:
        response = requests.get(url, timeout=10)
        text = response.text.lower()

        if "sold out" in text or "no tickets available" in text:
            print("❌ No tickets")
            last_sent = False
        else:
            if not last_sent:
                send_message("🟢 CHECK NOW! Possible TTD availability!")
                last_sent = True

    except Exception as e:
        print("Error:", e)

while True:
    check_tickets()
    time.sleep(120)