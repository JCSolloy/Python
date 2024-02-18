// Lectura o entrada de datos

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string nombre;
    int edad;
    cout << "Ingrese su nombre: ";
    cin >> nombre;
    cout << "Ingrese su edad: ";
    cin >> edad;
    cout << "Hola " << nombre << " tienes " << edad << " años." << endl;
    return 0;
}
// En este programa se declara una variable de tipo string llamada nombre y una variable de tipo entero llamada edad.
// Se pide al usuario que ingrese su nombre y su edad, y se almacenan en las variables nombre y edad, respectivamente.
// Luego se imprime un mensaje con el nombre y la edad ingresados.
// El operador >> se utiliza para leer datos desde la entrada estándar (teclado) y el operador << se utiliza para escribir datos en la salida estándar (pantalla).
// El operador << se utiliza para concatenar cadenas de texto y variables.