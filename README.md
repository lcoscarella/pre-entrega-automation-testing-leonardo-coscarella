### #########################################################
### Propósito del proyecto
### Esta es la pre entrega del curso de Automation Testing de Talento Tech


### Tecnologías utilizadas
### Python, Selenium Web Driver, JavaScript, CSS, DOM, HTML

### Instrucciones de instalación de dependencias
### Se debe importar las siguientes dependencias:
### - def_tests y las funciones internas login,comprobar_elementos_inventario,agregar_productos
### - utils y vars

### Comando para ejecutar las pruebas (por ejemplo: pytest -v --html=reporte.html)
### python -m pytest -v --html=reports/reportePreEntrega_Vx.html --self-contained-html

### Detalle de funciones
### login(usuario, contraseña): 
### Funcion usada para ingresar al sistema pasandole usuario y contraseña como parámetros.

### comprobar_elementos_inventario(usuario, contraseña):
### Función usada para comprobar la existencia de inventario y utilizar el orde mediante lista desplegable. 
### Se pasa usuario y contraseña como parámetro ya que para acceder al listado se debe estar autenticado.

### agregar_productos(usuario, contraseña):
### Funcion utilizada para agregar productos en el carrito de compras y comprar que se vea dentro de la url del detalle del mismo.
### Se pasa usuario y contraseña como parámetro ya que para acceder al listado se debe estar autenticado.