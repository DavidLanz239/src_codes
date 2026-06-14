/* =============================================================================
 Ejercicio2: Número Par o Impar
 AUTOR: David Lanz
 FECHA DE CREACIÓN: Junio 2026
 DESCRIPCIÓN: Crear un programa que detecte si un número entero ingresado por el usuario es par o impar.
 ============================================================================ */

#include <iostream>
#include <limits>

// 1 - Entrada de datos
int main() {
  std::cout << "Ingrese un numero entero positivo: ";
  int numero;

// 2 - Validar la entrada del usuario
  if (!(std::cin >> numero)) {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cerr << "Entrada invalida." << std::endl;
    return 1;
  }

  if (numero <= 0) {
    std::cout << "El numero debe ser positivo.\n";
    return 1;
  }

// 3 - Procesamiento y salida de datos
  if (numero % 2 == 0) {
    std::printf("El numero es par.\n");
  } else {
    std::printf("El numero es impar.\n");
  }

  return 0;
}


// 4 - Fin del programa


