# Adeco Agro
App que nos permite: 

- Visualizar los datos obtenidos de las distintas secadoras de Adeco Agro, filtrarlos por columna, por fecha o la combinacion de estas dos.
- Generar grafico de tendencia de las temperaturas (temperatura y temperatura 2), basado en una fecha y un tipo de secadora, ademas de generar las lineas horizontales guia, que representen los limites de temperaturas minimas y maximas.
- Generar un reporte en excel de todos los registros de secadoras, dados por los filtros aplicados (entre fechas, en una fecha determinada, segun una columna o la combinacion de las anteriores).

- La interfaz de usuario fue creada en Qt Designer, herramienta grafica de python para creacion de pantallas. En la carpeta "ui" esta ubicado el archivo main.ui, pantalla principal de la aplicacion. Para poder visualizarla y modificarla deberiamos instalar Qt Designer y abrir el archivo desde el mismo.
- En "Registros secadoras.py" creamos la clase principal Weather, donde llamamos y cargamos la interfaz grafica "main.ui". Luego definimos las variables que utilizamos y si se requiere de la utilizacion de algun objeto de la pantalla, se llama al mismo por su objectName (se puede ver el mismo en Qt Designer).
- En la carpeta resources almacenamos todas aquellas imagenes que utilizamos en la interfaz grafica. En este caso se encuentra el logo de la empresa (MSI) en formato png.

# Paquetes y programas necesarios para que la aplicacion funcione correctamente:

- Descargar e instalar **python3**.
- Instalar **pip** de python.
- Un IDE, en lo posible **Visual Estudio Code**
- Instalar con pip las siguientes librerias: pyqt5, pyqt5-tools, pandas, mysql, pyinstaller.
- Instalar la **extension de python** en VSCode para poder ejecutar el codigo mediante el boton de "run". Otra alternativa es ejecutar el comando **python 'Registros secadoras.py'** por consola, desde la carpeta raiz.
- Contar con **MySQL Workbench 8.0 CE** instalado, con la base de datos ya creada (registro_temp) y los datos insertados en la tabla (temperaturas). Para crear la base de datos y la tabla con los datos ya predefinidos, tenemos el archivo "Adecco db.sql" donde estan todos los scripts MySQL necesarios.
- Tambien es necesario instalar **MySQL Server**.


Comando para crear el .exe del archivo.py (por consola, estando en la carpeta raiz del proyecto):
**pyinstaller.exe --onefile --windowed "nombre_archivo.py"**

Si el comando se ejecuta correctamente, se creara una carpeta llamada **dist** con el archivo .exe dentro. Deberiamos moverlo a la carpeta raiz del proyecto para que no existan problemas con respecto a las rutas de conexion de bd y llamadas de modulos.

# Pantalla principal de la App
![PantallaPpal](https://user-images.githubusercontent.com/43302871/166975959-7849824e-b09a-43b4-8082-010909f9d106.PNG)

# Gráfico de tendencias generado
![PantallaTendencias](https://user-images.githubusercontent.com/43302871/166976088-74ae98da-f3dd-446b-b38d-82e1fc51ccb8.PNG)

# Alerta de error por datos erroneos al intentar generar el gráfico de tendencias
![PantallaErrorGrafico](https://user-images.githubusercontent.com/43302871/166976198-c8500526-8b04-4db5-b9c8-38be01dc39b5.PNG)

