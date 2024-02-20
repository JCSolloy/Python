//Condicional sentencia if
#include <iostream>
using namespace std;
int main()
{
    int a;
    cout << "Introduce un número: ";
    cin >> a;
    if (a > 0)
        cout << "El número es positivo" << endl;
    else
        cout << "El número es negativo" << endl;
    return 0;
}
