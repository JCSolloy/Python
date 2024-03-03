// Metodo ordenamiento por insercion
#include <iostream>
using namespace std;

int main()
{
    int numeros[] = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
    int i, pos, aux;
    for (i = 0; i < 10; i++)
    {
        pos = i;
        aux = numeros[i];
        while ((pos > 0) && (numeros[pos - 1] > aux))
        {
            numeros[pos] = numeros[pos - 1];
            pos--;
        }
        numeros[pos] = aux;
    }
    cout << "Orden Ascendente:";
    for (i = 0; i < 10; i++)
    {
        cout << numeros[i] << " ";
    }
    cout << endl;
    cout << "Orden Descendente:";
    for (i = 9; i >= 0; i--)
    {
        cout << numeros[i] << " ";
    }
    return 0;
}

