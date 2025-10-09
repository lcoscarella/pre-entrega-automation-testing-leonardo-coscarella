from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from utils import vars

### python -m tests.def_tests
### python -m def_tests

def login(user,pwd):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(vars.sauceDemoUrl)

    ###print("URL de Login: " + vars.sauceDemoUrl)

    time.sleep(5)
    blnLoginExitoso = True
    

    box_user = driver.find_element(By.ID,"user-name")
    box_pwd =  driver.find_element(By.ID,"password")

    button_login = driver.find_element(By.ID,"login-button")

    box_user.send_keys(user)
    box_pwd.send_keys(pwd)

    print("Enviado keys de user y pwd")

    button_login.click()

    print("Enviado click a boton de Login")

    time.sleep(7)

    if( driver.current_url == vars.landing_url_login_exitoso):
        blnLoginExitoso = True
    else:
        blnLoginExitoso = False
    
    ### print("Resultado Login: " + str(blnLoginExitoso))

    return blnLoginExitoso

print("Login resultado: " + str(login("standard_user","secret_sauce")))

'''
logo_selector = driver.find_element(By.CLASS_NAME,"app_logo")
swag_text = logo_selector.text

title_selector = driver.find_element(By.CLASS_NAME,"title")
title_text = title_selector.text

products = driver.find_elements(By.CLASS_NAME,"inventory_item_name ")
product_count = len(products)

print("Text:" + swag_text)
print("Title:" + title_text)
print("Cantidad de Productos mostrados: " + str(product_count))

'''


### python -m tests.login

