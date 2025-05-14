# TAREA 3 Diffie-Hellman

## Explicación básica
Diffie-Hellman es un protocolo para poder pasar llaves entre usuarios de forma encriptada, consta de un número primo muy grande acordado previamente, una llave publica que es otro numero pero que ambos usuarios pueden observar 

## Descripción del proyecto

El proyecto fue realizado en python, por desgracia, pero con suerte y tiempo libre espere que lo suba en lenguaje C.


## Ejecución del proyecto

El proyecto puede ejecutarse en cualquier ambiente de python ya sea visual studio code pero confío en que tendrá instalado python y por lo tanto podrá ejecutarlo desde terminal de la siguiente manera:

python3 DiffieHellman.py

Le aparecerá algo como lo siguiente:

Ingrese la llave publica A :_

Deberá poner un numero entero para ambas llaves publicas y se les mostrarán los prints de todo el proceso y al final se espera que se llegue a una sola clave compartida entre ambos usuarios. 

## Enserio aún sin python?

Bueno aquí hay unas instrucciones rápidas en linux para cualquier distribución de Ubunutu o Debian

sudo apt update
sudo apt install python3

## Y además aún sin linux? 

Bueno está bien igual se puede instalar en Windows

Descargar el instalador
Ve a la página oficial de Python:
https://www.python.org/downloads/windows/

Descarga la última versión de Python 3 para Windows.

Ejecutar el instalador
Abre el archivo .exe que descargaste.
IMPORTANTE: Marca la opción "Add Python to PATH" (para poder usar Python desde la terminal).
Haz clic en "Install Now" y espera a que termine la instalación.

Verificar la instalación
Después de instalar, abre el Símbolo del sistema (CMD) o PowerShell y escribe:

powershell
Copy
Edit
python --version
Si ves algo como Python 3.x.x, significa que la instalación fue exitosa. 🎉

(Opcional) Instalar pip y probarlo
Python ya viene con pip (el administrador de paquetes), pero puedes verificarlo con:

powershell
Copy
Edit
pip --version
Para probar pip, instala una librería como requests:

powershell
Copy
Edit
pip install requests
