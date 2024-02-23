//Ordenamiento por seleccion
#include <iostream>
using namespace std;

int main()
{
    int numeros[] = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
    int i, j, aux, min;
    for (i = 0; i < 10; i++)
    {
        min = i;
        for (j = i + 1; j < 10; j++)
        {
            if (numeros[j] < numeros[min])
            {
                min = j;
            }
        }
        aux = numeros[i];
        numeros[i] = numeros[min];
        numeros[min] = aux;
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
