// raiz cuadrada y potencia

#include <iostream>
#include <cmath> // Se incluye la libreria cmath para poder utilizar funciones matematicas

using namespace std;

int main()
{
    float a, raiz, potencia;
    cout << "Ingrese un numero: ";
    cin >> a;
    raiz = sqrt(a);
    potencia = pow(a, 2);
    cout << "La raiz cuadrada de " << a << " es " << raiz << endl;
    cout << "La potencia de " << a << " es " << potencia << endl;
    return 0;
}
