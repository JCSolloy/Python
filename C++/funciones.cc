// Funciones en c++

#include <iostream>
using namespace std;

int suma(int a, int b) {
    return a + b;
}   

int main() {
    int x = 3;
    int y = 4;
    cout << "La suma de " << x << " y " << y << " es " << suma(x, y) << endl;
    return 0;
}

