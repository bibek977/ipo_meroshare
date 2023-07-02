from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from tag_names import *

import time

class Driver:
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)

def logIn(username,password,bank_name):

    Driver.driver.get(main_url)

    assert "Mero Share" in Driver.driver.title

    branch_selection = Driver.wait.until(Ec.presence_of_element_located((By.NAME,branch_selection_name)))
    Driver.driver.find_element(By.NAME,branch_selection_name).click()
    bank_field = Driver.driver.find_element(By.CLASS_NAME,bank_selection_class)
    bank_field.click()
    bank_field.send_keys(bank_name,Keys.ENTER)
    
    username = Driver.driver.find_element(By.NAME,user_name).send_keys(username)
    password = Driver.driver.find_element(By.NAME,password_name).send_keys(password)

    Driver.driver.find_element(By.CLASS_NAME,sign_in_class).click()

    time.sleep(5)


def go_to_asba():

    # Driver.wait.until(Ec.presence_of_element_located((By.TAG_NAME,"app-dashboard")))
    Driver.wait.until(Ec.url_to_be(dashboard))
    Driver.wait.until(Ec.presence_of_element_located((By.XPATH,asba_path)))
    Driver.driver.find_element(By.XPATH,asba_path).click()
    Driver.wait.until(Ec.url_to_be(asba))
    time.sleep(5)

def quit_app():
    Driver.driver.quit()