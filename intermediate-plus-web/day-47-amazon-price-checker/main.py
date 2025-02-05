"""Amazon Price Checker."""

import requests as req

from bs4 import BeautifulSoup
from dotenv import load_dotenv

from .mailer import Mailer
from .blender import Blender

_ = load_dotenv()

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.co.uk/OptiPlex-Desktop-Computer-Windows-Renewed/dp/B09XHQ7Y6F/ref=pd_ci_mcx_mh_mcx_views_2_image?pd_rd_w=WO9QK&content-id=amzn1.sym.d63274d0-bf52-45e7-ae69-2bcf85c5865c%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=d63274d0-bf52-45e7-ae69-2bcf85c5865c&pf_rd_r=D9MZ5TQQVVGPTF1TDRB5&pd_rd_wg=tijGV&pd_rd_r=7e97ebdd-31d2-41ed-a3f8-0589cc34ae72&pd_rd_i=B09XHQ7Y6F"
CURRENCY_SYMBOL = "£"
TARGET_PRICE = 130

blender = Blender()
mailer = Mailer()
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "dnt": "1",
    "priority": "u=0, i",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132"',
    "sec-ch-ua-mobile": "?0",
}
html = req.get(url=URL, headers=headers, timeout=10).text

soup = BeautifulSoup(html, "html.parser")

price = blender.select_elements_content(soup, "span.priceToPay")[0]

if float(price.split(CURRENCY_SYMBOL)[1]) < TARGET_PRICE:
    mailer.send_mail(f"{price}")
