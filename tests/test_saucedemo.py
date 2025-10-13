from def_tests import login,comprobar_elementos_inventario,agregar_productos
import pytest
from utils import vars

### python -m pytest -v

### Comprueba login existoso
def test_login():
    assert login(vars.userLogin,vars.pwdLogin) == True

### Comprueba elementos del inventario
def test_inventario():
    assert comprobar_elementos_inventario(vars.userLogin,vars.pwdLogin) == True

### Comprueba elementos del inventario
def test_agregaProductos():
    assert agregar_productos(vars.userLogin,vars.pwdLogin) == True


