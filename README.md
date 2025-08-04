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

Las pruebas se dividen en pasos independientes que validan:

1. Configurar la dirección de origen y destino.
2. Seleccionar la tarifa Comfort.
3. Abrir el pop-up para ingresar el teléfono.
4. Introducir el número de teléfono.
5. Recuperar y enviar el código de confirmación automáticamente desde los logs.
6. Agregar tarjeta de crédito (número y CVV), activando el botón "Agregar" al perder el foco.
7. Verificar que la tarjeta fue agregada correctamente.
8. Escribir un mensaje para el conductor.
9. Pedir una manta y pañuelos.
10. Añadir 2 helados.
11. Buscar un taxi y confirmar que aparece la información del viaje.
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
⦁	TimeoutException: Puede aparecer si la página es lenta o los elementos tardan en mostrarse. Los WebDriverWait ayudan a manejar esto, pero se puede ajustar el tiempo si es necesario.

⦁	ElementClickInterceptedException: Suele pasar por animaciones o elementos que tapan al objetivo. Se soluciona esperando o usando clics por JavaScript.

⦁	Pruebas independientes: Cada test empieza desde un estado inicial limpio, siguiendo buenas prácticas de automatización.



