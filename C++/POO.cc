// Programacion orientada a objetos en C++

#include <iostream>
using namespace std;

class Persona {
    private:
        string nombre;
        int edad;
    public:
        Persona(string, int);
        void mostrarDatos();
};

Persona::Persona(string _nombre, int _edad) {
    nombre = _nombre;
    edad = _edad;
}

void Persona::mostrarDatos() {
    cout << "Nombre: " << nombre << endl;
    cout << "Edad: " << edad << endl;
}

int main() {
    Persona persona1 = Persona("Juan", 20);
    persona1.mostrarDatos();

    return 0;
}



