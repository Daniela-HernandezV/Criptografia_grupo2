# Diffie-Hellman
# Este protocolo criptográfico de clave pública (inventado por Whitfield Diffie y Martin Hellman) en 1976
#    funciona para intercambiar claves en un entorno inseguro.
#
# Las partes implicadas generan una nueva clave sin que esta sea interceptada.
#    La información que se intercambia suele llamarse ‘clave’.

import random

def primo(num):
    for n in range(2,num):
        if num % n == 0:
            print("No es primo, ",n," es divisor")
            return false
    print("Es primo")
    return 0

def main():
    p = int(input("Ingresa un numero primo: "))                 # P y g son valores publicos que se compartene en el canal inseguro
    primo(p)                                                    # Valores previamente acordados
    g = int(input("Ingresa una base g menor al numero elegido p: "))
    
    A = int(input("Ingrese la clave privada de A: "))           # A y B disponen de claves privadas cada uno 
    B = int(input("Ingrese la clave privada de B: "))           # Dichas claves nunca se comparten con nadie
    K_pub_A = (g**A)%p
    K_pub_B = (g**B)%p

    print(f"Llave publica A: {K_pub_A}")                        # Las variables anteriores p, g, A y B se pueden sustituir por <var = random.randint(1,10)> por ejemplo
    print(f"Llave publica B: {K_pub_B}")                        #   para obtener cierta aleatoreidad en las llaves.

    K_priv_A = (K_pub_B**A)%p
    K_priv_B = (K_pub_A**B)%p

    print(f"Llave privada de A para B {K_priv_A}")
    print(f"Llave privada de B para A {K_priv_B}")

main()

# *** Ejemplo de ejecución ***

# Ingresa un numero primo: 14891
# Es primo
# Ingresa una base g menor al numero elegido p: 13229
# Ingrese la clave privada de A: 168
# Ingrese la clave privada de B: 14
# Llave publica A: 1476
# Llave publica B: 8233
# Llave privada de A para B 3368
# Llave privada de B para A 3368

#Referencias: https://www.youtube.com/watch?v=rPg6o2nBS_k
