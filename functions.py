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

    time.sleep(3)


def go_to_asba():

    # Driver.wait.until(Ec.presence_of_element_located((By.TAG_NAME,"app-dashboard")))
    Driver.wait.until(Ec.url_to_be(dashboard))
    Driver.wait.until(Ec.presence_of_element_located((By.XPATH,asba_path)))
    Driver.driver.find_element(By.XPATH,asba_path).click()
    Driver.wait.until(Ec.url_to_be(asba))
    time.sleep(3)


def ipo_list():

    Driver.wait.until(Ec.presence_of_all_elements_located((By.CLASS_NAME,"company-list")))
    company_list = Driver.driver.find_elements(By.CLASS_NAME,"company-list")
    total_ipo = 0
    for i in company_list:
        Driver.wait.until(Ec.presence_of_element_located((By.CLASS_NAME,"company-name")))
        company_name = i.find_element(By.CLASS_NAME,"company-name")
        share_type = i.find_element(By.CLASS_NAME,"isin")
        print(f"company name : {company_name.text} \n share-type : {share_type}")
        total_ipo += 1



    for j in range(total_ipo):
        apply_btn = Driver.driver.find_element(By.XPATH,'//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[' + str(j+1) +']/div/div[2]/div/div[4]/button')
        apply_btn.click()
        time.sleep(3)

        cancel_btn = Driver.driver.find_element(By.CLASS_NAME,"back-button-block")
        cancel_btn.click()
        time.sleep(3)

def quit_app():
    Driver.driver.quit()