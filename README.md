# Descripción
Este entregable consiste en un menú principal que está conformado por cinco módulos de Python que realizan tareas de ciberseguridad, los cuales son:
- **DataAbuse_module.py** 
- **Hash_module.py**
- **IP_module.py**
- **Ports_module.py**
- **Shodan_module.py**
  
Al ejecutar el script principal (Menu.py), se estará llevando un registro de las acciones que se realicen, esto se hace con el módulo logging.
Después los eventos sean guardados en un archivo txt que lleva por nombre la fecha de ejecución, este se guarda dentro de una caprtea llamada *Logs*.
# Uso de Menú
Al ejecutar el menú, se desplegarán las diferentes tareas que puedes realizar, únicamente tendrás que ingresar la opción que deseas realizar, y se ejecutará el módulo correspondiente.
## Opciones:
### 1-Ver IP (Local o pública)
Aquí puede consultar tu ip local o ip pública, o ambas en caso de que así lo desees.
### 2-Ver puertos abiertos de un dominio o IP
Esta opción realiza un escaneo de puertos para después mostrar cuáles puertos están abiertos.
Para hacer uso de esta opción únicamente se necesita de alguna IP o dominio
Después de ingresar la ip o dominio, tienes que ingresar el puerto en el que comenzará el escaneo y en cuál terminará.
Por último el módulo retornará los puertos que estén abiertos
### 3-API Shodan
Esta opción te permite consultar infomración pública acerca de dispositivos conectados a internet, logrando observar servicios expuestos, puertos abiertos, banners, vulnerabilidades, etcétera.
Este módulo funciona con la API de Shodan, para usarlo primeramente te pide tu Api Key, después la ip que deseas consultar en Shodan.
### 4-API IP Data Abuse
Esta opción verifica si una IP ha sido reportada por actividades maliciosas como spam, escaneo de puertos, ataques DDoS, y te muestra un conteo de cuántas veces ha sido reportada en los últimos x días, donde tú puedes definir el rango de días 
Al igual que en el anterior, se requiere de una Api Key para este módulo, después también se te pedirá la ip que deseas consultar los reportes y el rango de días a considerar los reportes.
### 5-Generar Hashes/Buscar hashes
Dentro de esta opción, hay otro sub menú que te permite elegir diferentes tareas, las cuales son:
  - **Generar Hash:** Genera un hash a partir de una cadena de texto que hayas ingresado, te da la opción de guardar el hash en un diccionario.
  - **Consultar Diccionario:** Te muestra los hashes que hay dentro del diccionario, tú decides cuántos hashes va a mostar.
  - **Buscar Hash dentro de un diccionario:** Se buscará el hash que ingreses dentro de un diccionario, en caso de que haya una coincidencia, se mostrará el texto original.
  - **Verificar si hay coincidencias del Hash en HaveIBeenPwned:** En caso de que quieras verificar si un hash se encuentra dentro de las brechas conocidas por HaveIBeenPwned, puedes utilizar esta opción, ya que hará uso de su Api para comprobarlo, pidiendote únicamente el hash a verificar, ya que no requiere de Api Key.
### 6-Salir
Te permite salir del programa.


