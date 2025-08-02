Proyecto Sprint 8:  Urban Routes - Automatización de pruebas

Descripción

Este proyecto fue desarrollado como parte de una práctica de automatización de pruebas. El objetivo fue verificar el flujo completo para pedir un taxi dentro de la aplicación web Urban Routes, utilizando pruebas funcionales automatizadas con Python y Selenium.

La automatización cubre desde la selección de ruta y tarifa hasta la adición de una tarjeta de crédito, la petición de artículos adicionales y la espera del conductor asignado.

 Tecnologías utilizadas

- Python 3.13  
- Selenium WebDriver  
- Pytest  
- Google Chrome (para pruebas locales)  
- PyCharm (como entorno de desarrollo)

Estructura del proyecto

⦁	qa-project-Urban-Routes-es/
⦁	 main.py : Contiene las pruebas automatizadas
⦁	 utils.py : Métodos y localizadores de elementos
⦁	 data.py : Datos constantes usados en las pruebas
⦁	 README.md : Este archivo


Flujo cubierto por las pruebas

Las pruebas automatizadas ejecutan las siguientes acciones en orden:

1. Establecer ruta: se rellenan los campos de origen y destino.
2. Seleccionar tarifa Comfort
3. Ingresar número de teléfono
4. Obtener y enviar código de confirmación: interceptado automáticamente desde los logs.
5. Agregar tarjeta de crédito: se completa el número y CVV, forzando el desenfoque para activar el botón "Agregar".
6. Escribir mensaje al conductor
7. Pedir manta y pañuelos
8. Agregar 2 helados
9. Buscar taxi y confirmar que aparece información del viaje

Cada uno de estos pasos está validado dentro de pruebas individuales y puede ejecutarse de forma independiente.

Cómo ejecutar las pruebas

1.	Clona el repositorio:
git clone https://github.com/tu-usuario/qa-project-Urban-Routes-es.git
2. Abre PyCharm
3. Ve a File > Open, busca la carpeta donde clonaste el repositorio y selecciona los archivos (data.py, main.py, utils.py, y README.md).
4.Abre el archivo main.py
5.Asegúrate de que es el archivo actual (current file)
6.Presiona ▶ (play) para comenzar la ejecución del programa main.py

Recomendaciones y problemas comunes
⦁	TimeoutException: Asegúrate de que todos los elementos estén visibles antes de ejecutar acciones. Se usan WebDriverWaits en el proyecto para evitarlo.

⦁	ElementClickInterceptedException: Esto puede pasar por animaciones o solapamiento de elementos. En algunos pasos se usa JavaScript para hacer clic directo y evitar bloqueos.
