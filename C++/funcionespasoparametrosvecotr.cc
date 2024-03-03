// Funcion paso de parametros tipo vector

#include <iostream>
using namespace std;

void duplicar(int &a) {
    a *= 2;
}

void duplicar(int a[], int tam) {
    for (int i = 0; i < tam; i++) {
        a[i] *= 2;
    }
}

int main() {
    int x = 3;
    duplicar(x);
    cout << "x = " << x << endl;

    int v[] = {1, 2, 3, 4, 5};
    duplicar(v, 5);
    for (int i = 0; i < 5; i++) {
        cout << v[i] << " ";
    }
    cout << endl;
    return 0;
}

