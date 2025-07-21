# amazon-price-track
📦 GitHub Repository Description 🛒 Track Amazon product prices and get email alerts when prices drop below your set threshold — built with Python, BeautifulSoup, and SMTP.

💸 Amazon Price Tracker with Email Alerts
This Python project allows you to monitor the price of Amazon products and automatically sends you an email notification when the price drops below your target threshold. It works for both Turkish Lira (₺) and US Dollar ($) product pages and supports Gmail SMTP for sending alerts.

🚀 Features
  Scrapes Amazon product pages using BeautifulSoup

  Sends automated email alerts using SMTP

  Supports different currencies (TRY & USD)

  Customizable price threshold

  Keeps credentials secure using a .env file

  Easy to adapt for other e-commerce websites

🛠️ Technologies Used
  Python 3.x

  requests

  BeautifulSoup

  smtplib

  dotenv

📁 Project Structure

  📦 amazon-price-tracker/
  ├── main_with_tl.py       # Tracks Turkish Amazon price
  ├── main_with_usd.py      # Tracks U.S. Amazon price
  ├── .env                  # Contains email credentials (ignored by git)

▶️ How to Use
  1. Clone the repository
     git clone https://github.com/yourusername/amazon-price-tracker.git
     cd amazon-price-tracker

  2. Install required packages
     pip install requests beautifulsoup4 python-dotenv

  3. Create a .env file in the root directory
     Example:
     SMTP_ADDRESS=smtp.gmail.com
     EMAIL_ADDRESS=your_email@gmail.com
     EMAIL_PASSWORD=your_app_password
     TO_EMAIL=recipient_email@example.com

  4. Run the script for your region
      For Amazon Türkiye:
      python main_with_tl.py

      For U.S. Amazon:
      python main_with_usd.py

  5. If the product price is below your threshold, an email will be sent like this:

     Subject: Amazon Price Alert!
     
     Price of [Product Name] has dropped to $79.99
     https://www.amazon.com/example-product

🔐 Security & Tips
Keep your .env and email passwords private

Add this to your .gitignore:
.env
