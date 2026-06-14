#include <iostream> // input/output
#include <limits>

int main() {
  std::cout << "Ingrese un numero entero positivo: ";
  int numero;
  if (!(std::cin >> numero)) {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cerr << "Entrada invalida." << std::endl;
    return 1;
  }

  if (numero <= 0) {
    std::cout << "El numero debe ser positivo." << std::endl;
    return 1;
  }

  if (numero % 2 == 0) {
    std::cout << "El numero es par." << std::endl;
  } else {
    std::cout << "El numero es impar." << std::endl;
  }

  return 0;
}


