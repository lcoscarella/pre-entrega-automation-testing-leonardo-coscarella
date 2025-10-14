from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

sauceDemoUrl = 'https://www.saucedemo.com/'
sauceDemoUser = 'standard_user'
sauceDemoPwd = 'secret_sauce'
sauceDemoCartUrl = 'https://www.saucedemo.com/cart.html'

def getDriver():

    #instalacion de driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    time.sleep(5)

    return driver

def loginSaucedemo(driver):

    # Abro la pagina de login
    driver.get(sauceDemoUrl)
    
    # Ingresar usuario, pwd y enviar click en boton Submit
    driver.find_element(By.NAME,'user-name').send_keys(sauceDemoUser)
    driver.find_element(By.NAME,'password').send_keys(sauceDemoPwd)
    driver.find_element(By.ID,'login-button').click()

    time.sleep(5)