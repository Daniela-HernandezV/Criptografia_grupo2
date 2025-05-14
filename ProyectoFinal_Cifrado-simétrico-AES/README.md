# Proyecto Final - Cifrado simétrico AES

## Explicación básica
El algoritmo de cifrado AES (Advanced Encryption Standard) es un algoritmo de cifrado simétrico por bloques ampliamente utilizado para proteger la confidencialidad de la información. Cifra datos en bloques de 128 bits utilizando claves de 128, 192 o 256 bits. 
Es considerado uno de los algoritmos más seguros, resistente a ataques de fuerza bruta y otros tipos de criptoanálisis. 
Se utiliza en diversas aplicaciones, incluyendo la seguridad de conexiones en la web (HTTPS), la protección de datos en routers (WPA2) y la seguridad de datos en el almacenamiento en la nube. 

## Descripción del proyecto

El siguiente proyecto fue realizado en python y muestra, de forma desglosada el algoritmo de cifrado simétrico AES sin el uso de las librerias predefinidas por ptyhon para este algoritmo.
Adicionalmente se coloca un segundo proyecto "Proyecto02" que hace uso de dichas librerias para hacer pruebas y comprobar los resultados entregados por "Proyecto01"

## Ejecución del proyecto

El proyecto puede ejecutarse en cualquier ambiente de python ya sea visual studio code pero confío en que tendrá instalado python y por lo tanto podrá ejecutarlo desde terminal de la siguiente manera:

python3 Proyecto01.py

Le aparecerá algo como lo siguiente:

Ingresa el texto a cifrar: <ingresa tu texto ej.Hola como estas mundo>
Ingresa la clave (16 caracteres): <ingresa tu clave ej.abcdefghijklmnop>
Mensaje cifrado (hex): <Resultado:256777525682CCE870D848F951F0444442FDBF99FC37CD083697D9FEC4F03CBC>

Si ejecutas el programa Proyecto 02 con el mismo mensaje y clave observarás como dan el mismo resultado 

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
