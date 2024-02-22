// Clases en c++

#include <iostream>
#include <string>

using namespace std;

class Persona {
    public: // Atributos de la clase
        string nombre;
        int edad;
        Persona(string, int); // Constructor
    public: // Metodos
        void mostrarDatos(); // Metodo para mostrar los datos
};



int main() {
    Persona p1("Juan", 25);
    p1.mostrarDatos();
    return 0;
}

// Constructur, inicializacion de los atributos de la clase
Persona::Persona(string _nombre, int _edad) { // Constructor de la clase Persona con parametros 
    nombre = _nombre;
    edad = _edad;
}

// 
void Persona::mostrarDatos() { // Metodo para mostrar los datos
    cout << "Nombre: " << nombre << endl;
    cout << "Edad: " << edad << endl;
}
