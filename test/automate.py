from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from credentials import *
from tag_names import *

import time


driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(main_url)


username = username
password = password
bank_name = bank_name


assert "Mero Share" in driver.title

wait = WebDriverWait(driver, 30)

try:
    branch_selection = wait.until(Ec.presence_of_element_located((By.NAME,branch_selection_name)))

    try:
        driver.find_element(By.NAME,branch_selection_name).click()
        bank_field = driver.find_element(By.CLASS_NAME,bank_selection_class)
        bank_field.click()
        bank_field.send_keys(bank_name,Keys.ENTER)
        
        username = driver.find_element(By.NAME,user_name).send_keys(username)
        password = driver.find_element(By.NAME,password_name).send_keys(password)

        driver.find_element(By.CLASS_NAME,sign_in_class).click()

        try:
            full_name = wait.until(Ec.presence_of_element_located((By.CLASS_NAME,full_name_class)))
            print(full_name.text)

        except Exception as e:
            print(e)

    except Exception as e:
        print(e)

except Exception as e:
    print(e)

