from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time

def autoreply(number:int,contact_name:str,msg:str)->None:
    options=Options()
    options.add_argument(r"user-data-dir=C:\Users\anarp\edge-whatsapp-profile")
    options.add_argument(r"profile-directory=Default")
    driver=webdriver.Edge(options=options)
    wait=WebDriverWait(driver,30)
    driver.get("https://web.whatsapp.com")
    input("Scan QR please / Click Enter:")
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
        msg=input("Enter Your Message:")
        msg_box.send_keys(f"{msg}")
        msg_box.send_keys(Keys.ENTER)
        time.sleep(10)
        print(f"{msg} has been sent to {contact_name}")
    driver.quit()

