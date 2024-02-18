// expresion a/b +1

#include <iostream>
#include <string> // Se incluye la libreria string para poder utilizar variables de tipo string


using namespace std;

int main()
{
    float a, b;
    cout << "La expresion es a/b +1" << endl;
    cout << "Ingrese un numero para a:" << endl;
    cin >> a;
    cout << "Ingrese un numero para b: " << endl;
    cin >> b;
    cout << "El resultado de la expresion es: " << (a/b) + 1 << endl;
    return 0;
}
