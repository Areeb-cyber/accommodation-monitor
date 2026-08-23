-- Accommodation Monitor

A Python-based web monitoring script that checks accommodation availability and helps detect changes on an accommodation website.

-- Overview

Finding student accommodation can be difficult when available rooms are limited and listings change quickly. I created this project to automate the process of monitoring an accommodation website instead of manually checking it repeatedly.

The script periodically checks the website and detects changes in the available accommodation information.

-- Features

1. Automatically monitors an accommodation website
2. Checks for changes at regular intervals
3. Uses web automation to retrieve current information
4. Detects changes in website content
5. Includes error handling for network-related issues
6. Uses hashing to compare previously retrieved content with new content

-- Technologies Used

* Python
* Selenium
* HTTP requests
* Hashing (SHA-256)
* SMTP / Email notifications
* Web automation

-- How It Works

1. The script accesses the accommodation website.
2. It retrieves the relevant webpage information.
3. The retrieved content is processed and compared with the previous result.
4. A change is detected when the content differs.
5. The script can notify the user when a relevant change occurs.
6. The process repeats at defined intervals.

-- Purpose

This project was created as a practical automation project to solve a real-world problem while developing experience with:

1. Python scripting
2. Web automation
3. Monitoring systems
4. Error handling
5. Automation workflows
6. Basic networking concepts

-- Future Improvements

Possible improvements include:

1. Adding configurable monitoring intervals
2. Improving change detection to focus only on relevant accommodation data
3. Adding more notification methods
4. Adding logging
5. Running the monitor automatically using GitHub Actions or another cloud service
6. Supporting multiple accommodation websites

-- Author

Muhammad Areeb

GitHub: Areeb-cyber
