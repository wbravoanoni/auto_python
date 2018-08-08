## 1. ¿Que es Flask?

#### Micro Framework que permite levar Python a la web


## ¿Por que usar Flask?

- Solo usamos lo que necesitamos
- Nos permite integrar pruebas unitarias
- De facil comprension
- Uso de cookies
- Manejo de sesiones
- La curva de aprendizaje es baja

## 2. Instalacion en windows

### Comenzaremos con la instalacion de pip

#### ¿Que es PIP?

pip es una herramienta escrita en Python para facilitar la descarga e instalación de paquetes del lenguaje que se encuentren en el Python Package Index (PyPI). Podría suponerse que las siglas provienen de Python Install Package, aunque no hay certeza de esto. Corre en las principales plataformas: Microsoft Windows, Linux y OS X; en CPython 2.6+, 3.x y PyPy.
Instalacion

Primero, descarga el archivo instalador desde este [link](https://bootstrap.pypa.io/get-pip.py "enlace"). Si tu navegador lo abre en lugar de descargarlo, presiona CTRL + S (o CTRL + G) para guardarlo en tu ordenador. Segundo, una vez situado con la terminal (línea de comandos) en donde has guardado get-pip.py, ejecuta el siguiente comando.
~~~~~~~~
python get-pip.py
~~~~~~~~

no debe mostar lo siguiente, si lo muestra es por que falta la instalacion de Python

"no se reconoce como un comando interno o externo, programa o archivo por lotes ejecutable"

Actualizar
Si ya has instalado pip pero deseas actualizarlo a su última versión, deberás ejecutar lo siguiente.
Windows
	
~~~~~~~~
python -m pip install -U pip
~~~~~~~~

Instalar Flask

~~~~~~~~
pip install Flask
~~~~~~~~

### probar archivo

generar un archivo con el siguiente codigo (archivo base)

	
~~~~~~~~
from flask import Flask
app = Flask(__name__) #nuevo objeto
@app.route('/') #wrap o un decorador
def index():
return 'hola mundo' #Regresa un string
app.run() #se encarga de ejecutar el servidor 5000
~~~~~~~~

ir a la ruta del archivo y ejecutar

	
~~~~~~~~
python hola_munto.py
~~~~~~~~



## Cambiar puerto de salida
~~~~~~~~
app.run(port=8000) se encarga de ejecutar el servidor 8000
~~~~~~~~

## Realizar cambios en tiempo real 

~~~~~~~~
app.run(debug = True, port = 8000) cambios en tiempo real
~~~~~~~~

## Condicion solo para main

~~~~~~~~
if __name__ == '__main__':
app.run(debug = True, port = 8000) cambios en tiempo real solo para el main
~~~~~~~~
