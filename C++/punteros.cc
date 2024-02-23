// Punteros en c++

#include <iostream>
using namespace std;


int main() {
    int a = 10; // Variable entera
    int *puntero = &a; // Puntero que apunta a la direccion de memoria de a

    cout << "Valor de a: " << a << endl;
    cout << "Direccion de a: " << &a << endl;
    cout << "Valor de puntero: " << puntero << endl;
    cout << "Direccion de puntero: " << &puntero << endl;
    cout << "Valor al que apunta puntero: " << *puntero << endl;

    return 0;
}

