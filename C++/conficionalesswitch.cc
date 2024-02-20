// Condicionales con switch
#include <iostream>
using namespace std;
int main()
{
    int a;
    cout << "Introduce un número: ";
    cin >> a;
    switch (a)
    {
    case 1:
        cout << "El número es 1" << endl;
        break;
    case 2:
        cout << "El número es 2" << endl;
        break;
    case 3:
        cout << "El número es 3" << endl;
        break;
    default:
        cout << "El número no es 1, 2 ni 3" << endl;
    }
    return 0;
}

