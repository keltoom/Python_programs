import requests
from bs4 import BeautifulSoup
#import lxml
import smtplib

headers = {
    "Accept-Language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 OPR/75.0.3969.171"
}
URL = "https://www.amazon.com/Dell-Inspiron-LED-Backlit-Processor-Bluetooth/dp/B08X1D9WWJ?ref_=Oct_s9_apbd_onr_hd_bw_b2N0e&pf_rd_r=KABT69VMCEF6P4HG9CB9&pf_rd_p=b2e34a42-7eb2-50c2-8561-292e13c797df&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=565108"
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

# print(soup.prettify())
price_tag = soup.find(id="priceblock_ourprice").getText()
price = price_tag.split("$")[1]
print(price)
price_as_float = float(price)
print(price_as_float)

title = soup.find(id="productTitle").getText().strip()
print(title)

BUY_PRICE = 399

EMAIL = "email"
PASSWORD = "password"
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price_tag}"
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode('utf-8'))
