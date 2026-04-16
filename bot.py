from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time

def autoreply(number:int,contact_name:str,msg:str)->None:
    options=Options()
    #service = Service("/usr/bin/msedgedriver")
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--user-data-dir=/tmp/edge-profile")
    driver=webdriver.Edge(options=options)
    wait=WebDriverWait(driver,30)
    driver.get("https://web.whatsapp.com")
    #input("Scan QR please / Click Enter:")

    search= WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
        (By.XPATH, "//input[@aria-label='Search or start a new chat']")
        )
            )
    search.send_keys(contact_name)
    search.send_keys(Keys.ENTER)
    for i in range(number):
        msg_box=wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//footer//div[@contenteditable='true']")
                )
            )
        msg_box.click()
        #msg=input("Enter Your Message:")
        msg_box.send_keys(f"{msg}")
        msg_box.send_keys(Keys.ENTER)
        time.sleep(1)
        print(f"{msg} has been sent to {contact_name}")
        time.sleep(10)
    driver.quit()

