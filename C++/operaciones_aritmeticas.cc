// Operaciones aritmeticas

#include <iostream>

using namespace std;

int main()
{
    int a, b, suma, resta, multiplicacion, division, residuo;
    cout << "Ingrese un numero: ";
    cin >> a;
    cout << "Ingrese otro numero: ";
    cin >> b;
    suma = a + b;
    resta = a - b;
    multiplicacion = a * b;
    division = a / b;
    residuo = a % b;
    cout << "La suma de " << a << " y " << b << " es " << suma << endl;
    cout << "La resta de " << a << " y " << b << " es " << resta << endl;
    cout << "La multiplicacion de " << a << " y " << b << " es " << multiplicacion << endl;
    cout << "La division de " << a << " y " << b << " es " << division << endl;
    cout << "El residuo de la division de " << a << " y " << b << " es " << residuo << endl;
    return 0;
}
