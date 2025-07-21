import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
import locale

load_dotenv()

locale.setlocale(locale.LC_NUMERIC, 'tr_TR')
# print(locale.localeconv())

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL=os.getenv("TO_EMAIL")

live_url = ("https://www.amazon.com.tr/Tek-Adam-B%C3%BCy%C3%BCk-Kutulu-Tak%C4%B1m/dp/9751419573/"
            "ref=sr_1_1?crid=3O2U42N1JVZJ9&dib=eyJ2IjoiMSJ9.pa5VK1iFEm80uaVKw8i9-SfufCm_vUMEed7sIEmDJAwSu_"
            "ZClAa9Qq0lAZ9WW4t7V2dllT-mfmvEyPacDikknS013jOYBl9U3ZadaS0tEcmctX7xS-"
            "4G1ucfYU44ahWniwgj3dLwDQi5ae1L3RrSlvURBkDpl8zLnSbOQQIxKmgnesDytxIVIPHkDx2uDb5vbJdQjaBngr201GoYw_"
            "WnTjwiAQcN8O6QsxTDGtnLeMWQXo2DskXue50OBwPF96JyyoweGv5hPNj4PqQhgqpVyvGAWS7sJM_7xVk1HWKACrc.1"
            "DbspruEFOrIRqHX2q1UcW4-wbI-dX-bsI8zGHLof94&dib_tag=se&keywords=%C5%9Fevket+s%C3%BCreyya+aydemir"
            "&qid=1753013104&sprefix=%2Caps%2C137&sr=8-1")

# Full header
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "tr-TR,tr;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  }

# Minimal header
header = {
     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
 }

response = requests.get(live_url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="aok-offscreen").get_text().strip().replace("&nbsp;", " ")
title = soup.find(id="productTitle").get_text().strip()
# print(soup.prettify())
# print(price)
# print(title)

price_without_currency = price.strip(" TL")
price_delocalized = locale.delocalize(price_without_currency)
price_as_float = float(price_delocalized) # type is str
# print(price_as_float)

if price_as_float < 2000:
    message = f"Price of {title} has dropped to {price_as_float} TL"

    with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        result = connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Amazon Price Alert! \n\n{message}\n{live_url}".encode("utf-8")
        )