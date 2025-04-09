#include <stdio.h>
#include <string.h>
from typing import List

# ===== Tablas del algoritmo DES =====

# Permutación inicial # #
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Permutación final # #
FP = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

# Permutación PC-1 (clave 64 bits → 56 bits) #
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Permutación PC-2 (56 bits → 48 bits) #
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# Shifts para generación de subclaves
SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2,
                  1, 2, 2, 2, 2, 2, 2, 1]

# Expansión de 32 a 48 bits # #
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# S-Boxes #
S_BOXES = [
    # S1
    [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
     [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
     [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
     [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
    # S2
    [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
     [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
     [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
     [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
    # S3
    [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
     [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
     [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
     [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
    # S4
    [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
     [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
     [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
     [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
    # S5
    [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
     [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
     [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
     [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
    # S6
    [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
     [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
     [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
     [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
    # S7
    [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
     [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
     [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
     [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
    # S8
    [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
     [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
     [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
     [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]

# Permutación P # #
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

# ====== Funciones auxiliares ======

# Aplicar una permutación genérica a un bloque - tabla - bits del bloque original
def permutacion(bloque, tabla, n_bits):
    result = 0
    for pos in tabla:
        result <<= 1
        result |= (bloque >> (n_bits - pos)) & 1
    return result

# Permutación inicial y final
def permutacion_inicial(bloque):
    return permutacion(bloque, IP, 64)

def permutacion_final(bloque):
    return permutacion(bloque, FP, 64)

# Expansión de un bloque de 32 bits a 48 bits
def expansion(half_block):
    return permutacion(half_block, E, 32)

# Permutación P sobre 32 bits
def permute_p(bloque):
    return permutacion(bloque & 0xFFFFFFFF, P, 32)

# Sustitución S-box
def sustitucion_s_box(bloque):
    result = 0
    for i in range(8):      #Divide en 8 grupos 
        s_input = (bloque >> (42 - 6 * i)) & 0x3F
        fila = ((s_input & 0x20) >> 4) | (s_input & 0x01)
        columna = (s_input >> 1) & 0x0F
        result <<= 4
        result |= S_BOXES[i][fila][columna]     #(OR)
    return result

# Generación de subclaves
def generar_subllaves(llave):
    subllaves = []
    llave = permutacion(llave, PC1, 64)     # Permutación PC-1
    C = (llave >> 28) & 0x0FFFFFFF
    D = llave & 0x0FFFFFFF

    for shift in SHIFTS:                    # Realiza 16 rotaciones definidas en shifts
        C = ((C << shift) | (C >> (28 - shift))) & 0x0FFFFFFF       # Junta C y D, y aplica la permutación PC2 para obtener una subclave de 48 bits.
        D = ((D << shift) | (D >> (28 - shift))) & 0x0FFFFFFF
        CD = (C << 28) | D
        s_llave = permutacion(CD, PC2, 56)
        subllaves.append(s_llave)           # Se generan 16 subclaves para las 16 rondas de DES.
    return subllaves

# Función DES principal
def funcion_DES(bloque, subllaves, is_encrypt = True):    # is_encrypt, booleano: determina si se están aplicando las subclaves en orden directo (para cifrar) o en orden inverso (para descifrar).
    bloque = permutacion_inicial(bloque)    # Divide bloque en miyades de 32 bits
    L = (bloque >> 32) & 0xFFFFFFFF
    R = bloque & 0xFFFFFFFF

    for round in range(16):                 # Itera 16 rondas:
        tempR = R                               # Guarda el valor de R
        expand = expansion(R)                   # Se expande R a 48 bits y se le aplica XOR con la subclave correspondiente.
        rk = subllaves[round] if is_encrypt else subllaves[15 - round]
        R = expand ^ rk
        R = sustitucion_s_box(R)
        R = permute_p(R)
        R ^= L          #equivale a R=R^L(XOR)
        L = tempR

    final_block = (R << 32) | (L & 0xFFFFFFFF)  # Se concatenan R y L (intercambiados) y se aplica la permutación final.
    return permutacion_final(final_block)

# Métodos de cifrado y descifrado
def cifrar(mensaje, llave):
    subllaves = generar_subllaves(llave)
    return funcion_DES(mensaje, subllaves, True)

def descifrar(texto_cifrado, llave):
    subllaves = generar_subllaves(llave)
    return funcion_DES(texto_cifrado, subllaves, False)

# Ejemplo de uso
if __name__ == "__main__":
    mensaje = 0x0123456789ABCDEF
    llave = 0x133457799BBCDFF1
    print(f"Mensaje: 0x{mensaje:016X}") 

    texto_cifrado = cifrar(mensaje, llave)
    print(f"Texto cifrado: 0x{texto_cifrado:016X}")
    
    texto_descifrado = descifrar(texto_cifrado, llave)
    print(f"Texto descifrado: 0x{texto_descifrado:016X}")

    if mensaje == texto_descifrado:
        print("Operación exitosa")
    else:
        print("No se pudo realizar")

#https://www.youtube.com/watch?v=j06nfvF63v8&t=326s <-- Explicación algoritmo