"""Selenium practice."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep the browser open after the script has finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
# driver.get("https://www.amazon.co.uk/Dell-OptiPlex-Desktop-Computer-Windows/dp/B09GPLGG7K/?_encoding=UTF8&pd_rd_w=4ZgVk&content-id=amzn1.sym.a4ac6c4d-6ae7-4d95-b5e0-812c9dcfc72e:amzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=a4ac6c4d-6ae7-4d95-b5e0-812c9dcfc72e&pf_rd_r=VNTD27JT80KAQVH3SS0M&pd_rd_wg=qeRqC&pd_rd_r=627ea4f0-4cf3-403f-a77c-6497961c02c3")

driver.get("https://python.org")


"""
can also use find_elements for multiple elements
Other search options
By.NAME -> element names, such as might be used in form elements :: .tag_name / .get_attribute("attribute")
By.ID -> element id
By.CSS_SELECTOR -> any css selector
By.XPath -> path style address of element. Get XPath from inspect element -> right click -> copy -> copy XPath

https://www.selenium.dev/documentation/webdriver/elements/locators/
"""
# price_pounds = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_pence = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# price_to_pay = driver.find_element(By.CLASS_NAME, value="apexPriceToPay")
# # print(f"The price is £{price_pounds.text}.{price_pence.text}")
# print(f"The price is {price_to_pay.text}")

# Challenge

# upcoming_events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# for el in upcoming_events:
#     print(el.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# events = { event_times[i].text: event_names[i].text for i in range(len(event_times)) }
# events: dict[str, dict[str, str]] = {}
#
# for i in range(len(event_times)):
#     events[str(i)] = {
#             "time": event_times[i].text,
#             "name": event_names[i].text
#             }
#
# print(events)


# NOTE: to click, find the element and use the click method
# find the link - easiest way is to use the link text
# element.click()

# element = driver.find_element(By.LINK_TEXT, "Python 3.13.2 and 3.12.9 now available!")
# element.click()

# NOTE: typing
# select the element and use the send_keys method

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("decorator")


# NOTE: hit enter (or any other key)
# We need to import the Keys class from selenium.webdriver.common.keys
search_bar.send_keys(Keys.ENTER)
# driver.quit()
