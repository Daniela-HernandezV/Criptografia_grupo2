// // // // // // // // // // // // // // // // // // // //
// 														 //
// Criptografía - Grupo 2								 //
// Profesor: Dr. Alfonso Francisco De Abiega L'Eglisse	 //
// Alumno: Hernández Vázquez Daniela					 //
// 														 //
// // // // // // // // // // // // // // // // // // // //

#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Función para cifrar el texto usando Vigenere
void cifrado(char mensaje[], char tex[], char clave[]) {
    int iterador = 0, clave_len = strlen(clave);
    printf("\nEl texto cifrado es: ");

    for (int i = 0; tex[i] != '\n' && tex[i] != '\0'; i++) {
        if (tex[i] == ' ') {
            printf(" ");
            continue;
        }
        int mensaje_pos = toupper(tex[i]) - 'A'; 
        int clave_pos = toupper(clave[iterador % clave_len]) - 'A';
        printf("%c", mensaje[(mensaje_pos + clave_pos) % 26]);
        iterador++;
    }
    printf("\n");
}

// Función para descifrar el texto usando Vigenère
void decifrado(char mensaje[], char tex[], char clave[]) {
    int iterador = 0, clave_len = strlen(clave);
    printf("\nEl texto decifrado es: ");

    for (int i = 0; tex[i] != '\n' && tex[i] != '\0'; i++) {
        if (tex[i] == ' ') {
            printf(" ");
            continue;
        }
        int mensaje_pos = toupper(tex[i]) - 'A';
        int clave_pos = toupper(clave[iterador % clave_len]) - 'A';
        printf("%c", mensaje[(mensaje_pos - clave_pos + 26) % 26]);
        iterador++;
    }
    printf("\n");
}

int main() {
    int opcion;
    char abecedario[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    char texto[100], clave[100];

    printf("\nAbecedario reconocido:\n");
    printf("ABCDEFGHIJKLMOPQRSTUVWXYZ\n");

    printf("\nBienvenido, Ingresa el texto con el que desees trabajar: \n");
    fflush(stdin);
    fgets(texto, 100, stdin);

    printf("\nIngresa la clave para el cifrado/descifrado: \n");
    scanf("%s", clave);

    // Menú
    printf("\n1. Cifrar un texto.");
    printf("\n2. Descifrar un texto.");
    printf("\n3. Salir.\n");
    printf("\nElige una opcion:");

    scanf("%d", &opcion);
    getchar(); // Consumir el salto de línea

    switch (opcion) {
        case 1:
            printf("\n**** CIFRADO ****");
            cifrado(abecedario, texto, clave);
            break;
        case 2:
            printf("\n**** DESCIFRADO ****");
            decifrado(abecedario, texto, clave);
            break;
        default:
            printf("\nOpción no válida. Saliendo...\n");
            break;
    }

    printf("\nHasta Luego!\n");
    return 0;
}
