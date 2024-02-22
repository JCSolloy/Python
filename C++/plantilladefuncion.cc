// Plantilla de funcion

#include <iostream>
using namespace std;

template <class T>
T suma(T a, T b) {
    return a + b;
}

int main() {
    int x = 3;
    int y = 4;
    cout << "La suma de " << x << " y " << y << " es " << suma(x, y) << endl;
    return 0;
}

