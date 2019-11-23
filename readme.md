# Facultad de Ingeniería del Ejército
## Paradigmas de Programacion V
### Trabajo Práctico Integrador
* Titulo: Cartel de Led con wxPython
* Dado por: Ing. Diaz Pais

Dibuja un texto en una matriz de paneles de colores al estilo de un
cartel de LED. Sin mas preambulos:

![alt text](https://raw.githubusercontent.com/carlosmgc2003/led-objects/master/img/led-objects.png)

#### Requerimientos
1. [x]Poder mostrar en la pantalla de led un texto ingresado por el usuario. Dicho texto se va a considerar bien formado (es decir, con los caracteres aceptados solamente y sin espacios extras).
2. [x]Obtener la línea de texto de un archivo definido, llamado data.txt. También se va a considerar bien formado como en el caso 1.
3. [x]Mostrar la pantalla de forma titilante, con el texto establecido. La velocidad default tiene que se alguna que logre leer el texto.
4. [x]Poder configurar la velocidad que titila. No importa la magnitud, sino mostrar algunos casos con velocidad diferentes.
5. [x]Obtener la hora actual y mostrarla en la pantalla de led. Solo HH:MM y sin actualizar.

#### Instalación
1. `git clone https://github.com/carlosmgc2003/led-objects.git`
2. `cd led-objects`
3. `pip install -r requirements.txt`
4. `python main.py`