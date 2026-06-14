#include <iostream>
#include <string.h>

using namespace std;

int main() {
    const int MaxLength = 1000;
    char input[MaxLength];

    cout << "Ingrese una cadena: ";
    cin.getline(input, MaxLength);

    int length = strlen(input);

    cout << "Cadena invertida: ";
    for (int i = length - 1; i >= 0; i--) {
        cout << input[i];
    }
    cout << '\n';

    return 0;
}