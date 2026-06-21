#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;

// Implementacion manual de Bubble Sort
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Particion para Quicksort
int particionar(vector<int>& arr, int bajo, int alto) {
    int pivote = arr[alto];
    int i = (bajo - 1);
    for (int j = bajo; j <= alto - 1; j++) {
        if (arr[j] < pivote) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[alto]);
    return (i + 1);
}

// Implementacion manual de Quicksort
void quickSort(vector<int>& arr, int bajo, int alto) {
    if (bajo < alto) {
        int pi = particionar(arr, bajo, alto);
        quickSort(arr, bajo, pi - 1);
        quickSort(arr, pi + 1, alto);
    }
}

int main() {
    // Tamaños de prueba propuestos
    vector<int> tamanos = {10000, 50000, 100000, 200000, 500000};
    
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000000);

    for (int n : tamanos) {
        vector<int> datos(n);
        for(int i = 0; i < n; i++) datos[i] = dis(gen);

        cout << "Probando con " << n << " elementos:" << endl;

        // Prueba Quicksort
        vector<int> quick_v = datos;
        auto inicio = chrono::high_resolution_clock::now();
        quickSort(quick_v, 0, n - 1);
        auto fin = chrono::high_resolution_clock::now();
        chrono::duration<double> tiempo = fin - inicio;
        cout << " -> Quicksort tardo: " << tiempo.count() << " segundos." << endl;

        // Prueba Bubble Sort (solo si el tamaño es razonable para no bloquear la PC)
        if (n <= 100000) { 
            vector<int> bubble_v = datos;
            inicio = chrono::high_resolution_clock::now();
            bubbleSort(bubble_v);
            fin = chrono::high_resolution_clock::now();
            tiempo = fin - inicio;
            cout << " -> Bubble Sort tardo: " << tiempo.count() << " segundos." << endl;
        } else {
            cout << " -> Bubble Sort saltado (demasiado lento)." << endl;
        }
        cout << "-----------------------------------" << endl;
    }

    return 0;
}