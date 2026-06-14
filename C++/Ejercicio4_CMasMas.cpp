// =============================================================================
// Ejercicio4: Promedio de 4 números flotantes
// AUTOR: David Lanz
// FECHA DE CREACIÓN: Junio 2026
// DESCRIPCIÓN: Crear un programa que le pida al usuario 4 números flotantes 
// y luego imprima su promedio.
// =============================================================================
//

#include<iostream>

using namespace std;

int main(){


  // 1 - Declaración de variables y entrada de datos
  float num1;
  float num2;
  float num3;
  float num4;


  // 2 - Entrada de datos
  puts("Ingrese 4 numeros flotantes: "); 
  //puts solo sirve para imprimir strings, no variables, es mas rapido que cout
  cin>>num1;
  cin>>num2;
  cin>>num3;
  cin>>num4;


  // 3 - Procesamiento y salida de datos
  puts("promedio: ");
  cout<<(num1+num2+num3+num4)/4<<endl;

  return 0; 
}


// 4 - Fin del programa