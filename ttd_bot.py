import requests
import time

BOT_TOKEN = "YOUR_TOKEN"
CHAT_ID = "5361281940"

last_sent = False  # prevents spam

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

        if "no tickets available" in text or "sold out" in text:
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
    time.sleep(120)  # check every 2 minutes (IMPORTANT)