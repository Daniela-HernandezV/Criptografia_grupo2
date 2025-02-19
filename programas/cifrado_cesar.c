// // // // // // // // // // // // // // // // // // // //
// 														                           //
// Criptografía - Grupo 2							               		 //
// Profesor: Dr. Alfonso Francisco De Abiega L'Eglisse	 //
// Alumno: Hernández Vázquez Daniela			         			 //
// 													               	         		 //
// // // // // // // // // // // // // // // // // // // //

#include <stdio.h>
#include <string.h>

//Función para cifrar el texto.

void cifrado(char mensaje[], char tex[]){

    int desplazamiento;
    int letra;
    int iterador=0;

    printf("\nIngresa el numero correspondiente a el desplazamiento de las letras para el cifrado: ");
    scanf("%d",&desplazamiento);

    printf("\nEl texto cifrado es: ");

    while(tex[iterador] != '\n'){
        for(int j = 0; j < 26; j++){
            if(tex[iterador]==' '){
                printf(" ");
                break;
            }
            if( tex[iterador] == mensaje[j]){
                printf("%c", mensaje[(j+desplazamiento)%26]);
                break;
            }
        }
        iterador++;
    }
    printf("\n");
}

//Función para decifrar texto

void decifrado(char mensaje[],char tex[]){

    int desplazamiento;
    int letra;
    int iterador=0;

    printf("\nIngresa el número correspondiente a el desplazamiento de las letras para el decifrado: ");
    scanf("%d",&desplazamiento);

    printf("\nEl texto decifrado es: ");

    while(tex[iterador] != '\n'){
        for(int j = 0; j < 26; j++){
            if(tex[iterador]==' '){
                printf(" ");
                break;
            }
            if( tex[iterador] == mensaje[j]){
                if(j-desplazamiento < 0)
                    printf("%c", mensaje[(j-desplazamiento)+26]);
                else
                    printf("%c", mensaje[(j-desplazamiento)%26]);
                break;
            }
        }
        iterador++;
    }
    printf("\n");
}

int main(){

    int opcion;
    char abedecario[26]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    char texto[100];

        printf("\nAbecedario reconocido:\n");
        printf("ABCDEFGHIJKLMOPQRSTUVWXYZ\n");


        printf("\nBienvenido, Ingresa el texto con el que desees trabajar: \n");fflush(stdin);
        fgets(texto,100,stdin);

        //Menú
        printf("\n1. Cifrar un texto.");
        printf("\n2. Decifrar un texto.");
        printf("\n3. Salir.\n");
        printf("\nElige una opcion:");

        scanf("%d",&opcion);
        switch (opcion)
        {
            case 1:{
                printf("\n**** CIFRADO ****");
                cifrado(abedecario,texto);
                break;
            }
            case 2:{
                printf("\n**** DECIFRADO ****");
                decifrado(abedecario,texto);
                break;
            }
        }

    printf("\nHasta Luego!\n");
    return 0;
}
