// Clases y objetos en c++

#include <iostream>
#include <string>
using namespace std;

class Persona {
    public:
        string nombre;
        int edad;
        Persona(string n, int e) {
            nombre = n;
            edad = e;
        }
        void saludar() {
            cout << "Hola, soy " << nombre << " y tengo " << edad << " años." << endl;
        }
};

int main() {
    Persona p1("Juan", 25);
    Persona p2("Maria", 30);
    p1.saludar();
    p2.saludar();
    return 0;
}
