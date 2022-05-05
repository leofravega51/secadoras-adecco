# secadoras-adecco
App que nos permite visualizar los datos obtenidos de las distintas secadoras de Adecco Agro, filtrarlos por columna, por fecha, etc.
Generar grafico de tendencia de las temperaturas (temperatura y temperatura 2), basado en una fecha y un tipo de secadora.
Generar un reporte en excel de todos los registros de secadoras, dados por los filtros aplicados (entre fechas, en una fecha determinada, segun una columna, etc) o no.
En las configuraciones de la conexion a la base de datos definimos como host la ip de la pc/servidor donde esta corriendo sql server.

Comando para crear el .exe del archivo.py:
pyinstaller.exe --onefile --windowed "nombre_archivo.py"