import smtplib
from email.mime.text 
import MIMEText
import time
import hashlib
import sys
from urllib.error 
import URLError, HTTPError
from urllib.request 
import urlopen, Request
import pygame
pygame.mixer.init()
from datetime import datetime

def send_email():
sender = os.getenv("EMAIL_ADDRESS")
receiver = os.getenv("EMAIL_RECEIVER")
password = os.getenv("EMAIL_PASSWORD")

    now = datetime.now()
    email_time = now.strftime("%Y-%m-%d %H:%M:%S")

    subject = f"Accommodation Website Change Detected! {email_time}"
    body = ("The monitored website has changed. Check immediately. "
            "https://www.stwdo.de/wohnen/aktuelle-wohnangebote#residential-offer-list")

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Email failed: {e}")

def play_alarm():
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()


def check_website():
    retry_attempts = 5  # Number of retry attempts
    wait_time = 5  # Initial wait time (seconds)

    for attempt in range(retry_attempts):
        try:
            # Set a custom timeout to handle server response delay
            response = urlopen(url, timeout=60).read()
            return hashlib.sha224(response).hexdigest()
        except HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            raise
        except URLError as e:
            print(f"Attempt {attempt + 1}: Failed to reach server: {e.reason}")
            if attempt < retry_attempts - 1:
                wait_time *= 2  # Exponentially increase the wait time
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("All retry attempts failed. Exiting.")
                raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    return None

# Setting the URL you want to monitor
url = Request('https://www.stwdo.de/wohnen/aktuelle-wohnangebote#residential-offer-list',
              headers={'User-Agent': 'Mozilla/5.0'})

try:
    currentHash = check_website()
except Exception as e:
    print(f"Initial Error: {e}")
    sys.exit(1)

print("Monitoring website for changes...")

while True:
    try:
        # Wait for 60 seconds between checks
        time.sleep(12)

        newHash = check_website()

        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        if newHash == currentHash:
            print(f"{formatted_time}: No change detected.")
        else:
            print(f"{formatted_time}: ***** Change detected! Playing music *****")
            # play_alarm()
            play_alarm()
            send_email()
            currentHash = newHash

    except (URLError, HTTPError) as e:
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{formatted_time} Error: {e}")
        continue

    except Exception as e:
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{formatted_time} Unexpected error: {e}")
        sys.exit(1)
