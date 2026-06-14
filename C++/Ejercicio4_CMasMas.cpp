#include<iostream>

using namespace std;

int main(){

  float num1;
  float num2;
  float num3;
  float num4;
  puts("Ingrese 4 numeros flotantes: "); 
  //puts solo sirve para imprimir strings, no variables, es mas rapido que cout
  cin>>num1;
  cin>>num2;
  cin>>num3;
  cin>>num4;
  puts("promedio: ");
  cout<<(num1+num2+num3+num4)/4<<endl;

  return 0; 
}


