#include<iostream>

using namespace std;

int main(){

  string entrada;

  cout<<"Ingrese una cadena de texto: ";
  getline(cin, entrada);
  entrada = "a"+entrada+"a";
  cout<<"La cadena con 'a' al inicio y al final es: "<<entrada<<endl;

  return 0; 
}


