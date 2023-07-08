from functions import *
from credentials import *


username = username
password = password
bank_name = bank_name

try:
    while Driver.driver.current_url != dashboard:
        logIn(username,password,bank_name)

        if Driver.driver.current_url == dashboard:
            break
        else:
            print("Login Error")

    go_to_asba()
    ipo_list()

except Exception as e:
    print(e)

finally:
    quit_app()