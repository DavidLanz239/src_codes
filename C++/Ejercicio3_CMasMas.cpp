// =============================================================================
// Ejercicio3: Cadena con 'a' al inicio y al final
// AUTOR: David Lanz
// FECHA DE CREACIÓN: Junio 2026
// DESCRIPCIÓN: Crear un programa que le pida al usuario cualquier palabra, secuencia de números u oración para que luego el programa imprima lo mismo # pero con una “a” al principio y una “a” al final.
// =============================================================================
//

#include <cstdio>
#include <iostream>
#include <string>

// 1 - Declaración de variables y entrada de datos
using namespace std;

int main(){

  string entrada;

  // 2 - Entrada datos
  cout<<"Ingrese una cadena de texto: ";
  getline(cin, entrada);
 
 
 // 3 - Procesamiento y salida de dato
  entrada = "a"+entrada+"a";
   cout<<"La cadena con 'a' al inicio y al final es: "<<entrada<<endl;

  return 0; 
}


// 4 - Fin del programa


