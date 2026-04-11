from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Edge()
wait=WebDriverWait(driver,30)
driver.get("https://web.whatsapp.com")

input("Scan QR please")
search= WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@aria-label='Search or start a new chat']")
    )
)

contact_name=input("Your Contact Name:")
search.send_keys(contact_name)
search.send_keys(Keys.ENTER)


time.sleep(2)

msg_box=wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,"//footer//div[@contenteditable='true']")
            )
        )
msg_box.click()
msg_box.send_keys("Good Night"+Keys.ENTER)
time.sleep(5)
driver.quit()

