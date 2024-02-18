// programa que intercambie los valores de dos variables.

#include <iostream>
#include <string> // Se incluye la libreria string para poder utilizar variables de tipo string

using namespace std;

int main()
{
    float a, b, temp;
    cout << "Ingrese un numero para a:" << endl;
    cin >> a;
    cout << "Ingrese un numero para b: " << endl;
    cin >> b;
    temp = a;
    a = b;
    b = temp;
    cout << "El valor de a es: " << a << endl;
    cout << "El valor de b es: " << b << endl;
    return 0;
}
