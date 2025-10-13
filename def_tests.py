from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from tests import conftest
import time
from utils import vars


### python -m tests.def_tests
### python -m def_tests

def login(user,pwd):
    # Inicializo web driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Indico url
    driver.get(vars.sauceDemoUrl)

    # Capturo url inicial
    driver.save_screenshot("capturas/url_inicial.png")

    # Establezco pausa
    time.sleep(5)

    # Ingreso usuario, contraseña y click en boton
    box_user = driver.find_element(By.ID,"user-name")
    box_pwd =  driver.find_element(By.ID,"password")
    button_login = driver.find_element(By.ID,"login-button")

    box_user.send_keys(user)
    box_pwd.send_keys(pwd)
    button_login.click()

    # Establezco pausa
    time.sleep(7)

    # Comprueba si la url a donde fuimos dirigidos es la de inventario
    if( driver.current_url != vars.landing_url_login_exitoso):
        return False

    driver.save_screenshot("capturas/url_post_login.png")
    return True
    

def comprobar_elementos_inventario(user,pwd):
    # Inicializo web driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Indico url
    driver.get(vars.sauceDemoUrl)

    # Establezco pausa
    time.sleep(5)

    # Ingreso usuario, contraseña y click en boton
    box_user = driver.find_element(By.ID,"user-name")
    box_pwd =  driver.find_element(By.ID,"password")
    button_login = driver.find_element(By.ID,"login-button")

    box_user.send_keys(user)
    box_pwd.send_keys(pwd)
    button_login.click()

    # Establezco pausa
    time.sleep(7)

    # Comprueba si la url a donde fuimos dirigidos es la de inventario
    if( driver.current_url != vars.landing_url_login_exitoso):
        return False
    
    ### Comineza seccion Inventario

    ### Comprobar que el titluo de inventory.html sea "Swag Labs"
    if(driver.title != "Swag Labs"):
        return False

    ### Comprobar que existe el texto 'Swag Labs'
    if(driver.find_element(By.CLASS_NAME,"app_logo").text.strip() != "Swag Labs"):
        return False

    ### Comprobar que existe el texto 'Products'
    if(driver.find_element(By.CLASS_NAME,"title").text.strip() != "Products"):
        return False

    ### Comprobar que hay listados al menos 1 producto
    if(len(driver.find_elements(By.CLASS_NAME,"inventory_item_name ")) < 1):
        return False

    driver.save_screenshot("capturas/condicionesInventarioPostLogin.png")

    ### Comprobar presencia de menu, filtros
    try:
        driver.find_element(By.CLASS_NAME,"bm-menu")
        ddlSort = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
        ddlSort.select_by_value("za")

        driver.save_screenshot("capturas/inventarioOrdenadoPorNombre.png")

        time.sleep(4)

        ddlSort = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
        ddlSort.select_by_value("lohi")

        driver.save_screenshot("capturas/inventarioOrdenadoPorPrecio.png")

        time.sleep(3)
        return True
    except:
        return False

    return True

def agregar_productos(user,pwd):
    # Inicializo web driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Indico url
    driver.get(vars.sauceDemoUrl)

    # Establezco pausa
    time.sleep(5)

    # Ingreso usuario, contraseña y click en boton
    box_user = driver.find_element(By.ID,"user-name")
    box_pwd =  driver.find_element(By.ID,"password")
    button_login = driver.find_element(By.ID,"login-button")

    box_user.send_keys(user)
    box_pwd.send_keys(pwd)
    button_login.click()

    # Establezco pausa
    time.sleep(7)

    # Comprueba si la url a donde fuimos dirigidos es la de inventario
    if( driver.current_url != vars.landing_url_login_exitoso):
        return False
    
    # Comprobar que hay listados al menos 1 producto
    if(len(driver.find_elements(By.CLASS_NAME,"inventory_item_name ")) < 1):
        return False
    
    # Hacer click en el primer producto encontrado
    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()

    # Establerzco pausa
    time.sleep(3)

    # Comprobar que el contador de productos en el carrito sea igual o mayor a 1
    if(int(driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text) < 1):
        return False

    driver.save_screenshot("capturas/logoCarritoIncremento.png")

    # Dirijo a la url del carrito
    driver.get(vars.cart_url)

    # Establezco pausa
    time.sleep(5)

    # Compruebo que el nombre del producto agregado sea correcto
    if(driver.find_element(By.CLASS_NAME,"inventory_item_name").text != "Sauce Labs Backpack"):
        return False

    driver.save_screenshot("capturas/carritoConProductos.png")
    # Establezco pausa
    time.sleep(5)

    return True

print("resultado: " + str(comprobar_elementos_inventario("standard_user","secret_sauce")))

