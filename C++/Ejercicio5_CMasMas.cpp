// =============================================================================
// Ejercicio5: Invertir una cadena
// AUTOR: David Lanz
// FECHA DE CREACIÓN: Junio 2026
// DESCRIPCIÓN: Crear un programa que le pida al usuario una cadena de texto 
// y luego imprima la cadena invertida.
// =============================================================================
//

#include <iostream>
#include <string.h>

// 1 - Declaración de variables 
using namespace std;

int main() {
    const int MaxLength = 1000;
    char input[MaxLength];

    // 2 - Entrada de datos
    cout << "Ingrese una cadena: ";
    cin.getline(input, MaxLength);

    int length = strlen(input);


    // 3 - Procesamiento y salida de datos
    cout << "Cadena invertida: ";
    for (int i = length - 1; i >= 0; i--) {
        cout << input[i];
    }
    cout << '\n';

    // 4 - Fin del programa
    return 0;
}