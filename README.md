# secadoras-adecco
App que nos permite visualizar los datos obtenidos de las distintas secadoras de Adecco Agro, filtrarlos por columna, por fecha, etc.
Generar grafico de tendencia de las temperaturas (temperatura y temperatura 2), basado en una fecha y un tipo de secadora.
Generar un reporte en excel de todos los registros de secadoras, dados por los filtros aplicados (entre fechas, en una fecha determinada, segun una columna, etc) o no.
En las configuraciones de la conexion a la base de datos definimos como host la ip de la pc/servidor donde esta corriendo sql server.

Comando para crear el .exe del archivo.py:
pyinstaller.exe --onefile --windowed "nombre_archivo.py"

# Pantalla principal de la App
![PantallaPpal](https://user-images.githubusercontent.com/43302871/166975959-7849824e-b09a-43b4-8082-010909f9d106.PNG)

# Gráfico de tendencias generado
![PantallaTendencias](https://user-images.githubusercontent.com/43302871/166976088-74ae98da-f3dd-446b-b38d-82e1fc51ccb8.PNG)

# Alerta de error por datos erroneos al intentar generar el gráfico de tendencias
![PantallaErrorGrafico](https://user-images.githubusercontent.com/43302871/166976198-c8500526-8b04-4db5-b9c8-38be01dc39b5.PNG)

