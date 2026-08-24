import os
import smtplib
import time
import hashlib
import sys
from datetime import datetime
from email.mime.text import MIMEText
from urllib.error import URLError, HTTPError
from urllib.request import urlopen, Request

import pygame


# Initialize audio
pygame.mixer.init()


# Website to monitor
url = Request(
    "https://www.stwdo.de/wohnen/aktuelle-wohnangebote#residential-offer-list",
    headers={"User-Agent": "Mozilla/5.0"}
)


def send_email():
    """Send an email notification when a website change is detected."""

    sender = os.getenv("EMAIL_ADDRESS")
    receiver = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")

    if not sender or not receiver or not password:
        print("Email credentials are not configured.")
        return

    now = datetime.now()
    email_time = now.strftime("%Y-%m-%d %H:%M:%S")

    subject = f"Accommodation Website Change Detected! {email_time}"

    body = (
        "The monitored website has changed. Check immediately.\n\n"
        "https://www.stwdo.de/wohnen/aktuelle-wohnangebote"
        "#residential-offer-list"
    )

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

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
    """Play an alarm when a website change is detected."""

    try:
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play()
        print("Alarm played.")

    except Exception as e:
        print(f"Alarm failed: {e}")


def check_website():
    """Retrieve the website and return a hash of its content."""

    retry_attempts = 5
    wait_time = 5

    for attempt in range(retry_attempts):
        try:
            response = urlopen(url, timeout=60).read()
            return hashlib.sha224(response).hexdigest()

        except HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            raise

        except URLError as e:
            print(
                f"Attempt {attempt + 1}: "
                f"Failed to reach server: {e.reason}"
            )

            if attempt < retry_attempts - 1:
                wait_time *= 2
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)

            else:
                print("All retry attempts failed. Exiting.")
                raise

        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    return None


# Get the initial website hash
try:
    current_hash = check_website()

except Exception as e:
    print(f"Initial Error: {e}")
    sys.exit(1)


print("Monitoring website for changes...")


# Continuously monitor the website
while True:
    try:
        # Wait 12 seconds between checks
        time.sleep(12)

        new_hash = check_website()

        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        if new_hash == current_hash:
            print(f"{formatted_time}: No change detected.")

        else:
            print(
                f"{formatted_time}: "
                "***** Change detected! *****"
            )

            play_alarm()
            send_email()

            current_hash = new_hash

    except (URLError, HTTPError) as e:
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        print(f"{formatted_time} Error: {e}")
        continue

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        sys.exit(0)

    except Exception as e:
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        print(f"{formatted_time} Unexpected error: {e}")
        sys.exit(1)
