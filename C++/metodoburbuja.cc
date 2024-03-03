//Metodo de ordenamiento burbuja
#include <iostream>
using namespace std;
int main()
{
    int numeros[] = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
    int i, j, aux;
    for (i = 0; i < 10; i++)
    {
        for (j = 0; j < 10; j++)
        {
            if (numeros[j] > numeros[j + 1])
            {
                aux = numeros[j];
                numeros[j] = numeros[j + 1];
                numeros[j + 1] = aux;
            }
        }
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
