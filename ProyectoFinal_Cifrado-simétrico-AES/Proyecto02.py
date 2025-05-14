#######################################################################################################
#   Universidad Nacional Autónoma de México - Facultad de Ingeniería
#   Materia Criptografía    Grupo: 02   Semestre:2025-2
#   Proyecto final - Cifrado simétrico AES
# 
#   Integrantes:
#       - Rivera Gonzáles Frida Alison
#       - Frías Hernández Camille Emille Román
#       - Hernández Vázquez Daniela 
#       - Zamudio González Nathalia Danae
# 
#   Fecha de entrega: 18 de mayo de 2025
#######################################################################################################
#   El siguiente programa muestra el algoritmo de cifrado simétrico AES en Python haciendo
#     uso de las librerias ya definisas de python para este algoritmo. 
#     Programa de prueva para validación de resultados.
#######################################################################################################

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

# Clave de 128 bits (16 bytes)
clave = b'abcdefghijklmnop'

# Mensaje a encriptar
mensaje = "Hola como estas mundo"
# Convertir el mensaje a bytes
mensaje_bytes = mensaje.encode('utf-8')

# Asegurarse de que el mensaje tiene el tamaño correcto, en este caso, debe ser múltiplo de 16 (tamaño de bloque de AES)
mensaje_padded = pad(mensaje_bytes, AES.block_size)

# Crear el objeto AES en modo ECB
cipher = AES.new(clave, AES.MODE_ECB)

# Encriptar el mensaje
mensaje_encriptado = cipher.encrypt(mensaje_padded)

# Mostrar el resultado en formato hexadecimal
print("Mensaje encriptado:", binascii.hexlify(mensaje_encriptado).decode())
