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
    from datetime import datetime

while True:
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    # 🔥 Peak time (9:50 AM – 10:30 AM)
    if current_hour == 9 and current_minute >= 50 or current_hour == 10:
        print("🔥 Peak time — checking fast")
        check_tickets()
        time.sleep(20)  # fast checking

    else:
        print("Normal time — slow checking")
        check_tickets()
        time.sleep(180)  # slow checking (3 min)