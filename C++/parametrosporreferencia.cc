// Funciones paso de parametros por referencia

#include <iostream>
using namespace std;

void duplicar(int &a) {
    a *= 2;
}

int main() {
    int x = 3;
    duplicar(x);
    cout << "x = " << x << endl;
    return 0;
}

