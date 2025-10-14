### #########################################################
### Propósito del proyecto
### Esta es la pre entrega del curso de Automation Testing de Talento Tech
### Nombre y Apellido: Leonardo Coscarella


### Tecnologías utilizadas
### Python, Selenium Web Driver, Pytest JavaScript, CSS, DOM, HTML

### Instrucciones de instalación de dependencias
### Se debe importar las siguientes dependencias:
### from utils.ancillary import getDriver,loginSaucedemo,sauceDemoCartUrl

### Comando para ejecutar las pruebas (por ejemplo: pytest -v --html=reporte.html)
### python -m pytest -v --html=reports/reportePreEntrega_V1.html --self-contained-html (cambiar "x" por la version que se testear)
### Los reportes se guardan en la subcarpeta "reports"

### Capturas de pantalla - Evidencia
### Se guardan en formato .png dentro de la subcarpeta "capturas"

### Detalle de funciones
### login(usuario, contraseña): 
### Funcion usada para ingresar al sistema pasandole usuario y contraseña como parámetros.

### comprobar_elementos_inventario(usuario, contraseña):
### Función usada para comprobar la existencia de inventario y utilizar el orde mediante lista desplegable. 
### Se pasa usuario y contraseña como parámetro ya que para acceder al listado se debe estar autenticado.

### agregar_productos(usuario, contraseña):
### Funcion utilizada para agregar productos en el carrito de compras y comprar que se vea dentro de la url del detalle del mismo.
### Se pasa usuario y contraseña como parámetro ya que para acceder al listado se debe estar autenticado.

