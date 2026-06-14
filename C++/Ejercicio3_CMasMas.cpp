// ===========================================================================
// Ejercicio3: Cadena con 'a' al inicio y al final
// AUTOR: David Lanz
// FECHA DE CREACIÓN: Junio 2026
// DESCRIPCIÓN: Crear un programa que le pida al usuario cualquier palabra, 
// secuencia de números u oración para que luego el programa imprima lo
// mismo # pero con una “a” al principio y una “a” al final.
// ============================================================================
//

#include <iostream>
#include <string>

// 1 - Declaración de variables y entrada de datos
using namespace std;

int main() {
    std::string entrada;

    // 2 - Entrada datos
    std::cout << "Ingrese una cadena de texto: ";
    std::getline(std::cin, entrada);

    // 3 - Procesamiento y salida de dato
    entrada = "a" + entrada + "a";
    std::cout << "La cadena con 'a' al inicio y al final es: " << entrada << std::endl;

    return 0;
}


// 4 - Fin del programa


