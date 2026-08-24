-- Accommodation Monitor

A Python-based web monitoring script that checks an accommodation website for changes and provides notifications when a change is detected.

-- Overview

Finding student accommodation can be difficult when available rooms are limited and listings change quickly. I created this project to automate the process of monitoring an accommodation website instead of manually checking it repeatedly.

The script periodically retrieves the website content, generates a hash of the response, and compares it with the previous result. When a change is detected, the script can play an alarm and send an email notification.

-- Features

- Automatically monitors an accommodation website
- Checks for changes at regular intervals
- Uses HTTP requests to retrieve website content
- Uses SHA-224 hashing to detect changes
- Sends email notifications when changes are detected
- Plays an audio alarm when a change occurs
- Includes retry logic for connection failures
- Handles HTTP and network-related errors
- Runs continuously until stopped

-- Technologies Used

- Python
- urllib
- hashlib
- SMTP
- Pygame
- Error handling
- Web monitoring
- Automation

-- How It Works

1. The script connects to the accommodation website.
2. The website response is downloaded.
3. A SHA-224 hash is generated from the response.
4. The hash is stored as the current reference.
5. The script waits before checking the website again.
6. A new hash is generated.
7. The new hash is compared with the previous hash.
8. If the hashes are different, a change has been detected.
9. An audio alarm is played and an email notification is sent.
10. The new hash becomes the reference for the next check.

-- Email Configuration

Email credentials are not stored directly in the source code.

The script reads the following environment variables:

- EMAIL_ADDRESS
- EMAIL_RECEIVER
- EMAIL_PASSWORD

This approach helps prevent email credentials from being exposed in the public repository.

-- Purpose

This project was created as a practical automation project to solve a real-world problem while developing experience with:

- Python scripting
- Web monitoring
- Automation
- Hash-based change detection
- Email notifications
- Error handling
- Basic networking concepts

-- Future Improvements

Possible improvements include:

- Adding configurable monitoring intervals
- Detecting only relevant accommodation changes instead of any website change
- Adding more notification methods
- Adding structured logging
- Adding a configuration file
- Running the monitor as a background service
- Adding automated testing
- Supporting multiple accommodation websites

-- Author

Muhammad Areeb

GitHub: Areeb-cyber
