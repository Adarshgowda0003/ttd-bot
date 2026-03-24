import asyncio
from playwright.async_api import async_playwright
import requests

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

async def check_tickets():
    global last_sent

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            await page.goto("https://tirupatibalaji.ap.gov.in", timeout=60000)
            content = await page.content()
            text = content.lower()

            if "sold out" in text or "no tickets available" in text:
                print("❌ No tickets")
                last_sent = False
            else:
                if not last_sent:
                    send_message("🟢 REAL ALERT! TTD tickets may be available NOW!")
                    last_sent = True

        except Exception as e:
            print("Error:", e)

        await browser.close()

async def main():
    while True:
        await check_tickets()
        await asyncio.sleep(120)  # every 2 min

asyncio.run(main())