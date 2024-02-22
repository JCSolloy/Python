// Pilas en c++

#include <iostream>
using namespace std;

class Pila {
    private:
        int *pila;
        int tope;
        int capacidad;
    public:
        Pila(int capacidad);
        ~Pila();
        void push(int dato);
        int pop();
        int top();
        bool vacia();
        bool llena();
};

Pila::Pila(int capacidad) {
    this->capacidad = capacidad;
    pila = new int[capacidad];
    tope = -1;
}

Pila::~Pila() {
    delete[] pila;
}

void Pila::push(int dato) {
    if (llena()) {
        cout << "Pila llena" << endl;
        return;
    }
    pila[++tope] = dato;
}


int Pila::pop() {
    if (vacia()) {
        cout << "Pila vacia" << endl;
        return -1;
    }
    return pila[tope--];
}

int Pila::top() {
    if (vacia()) {
        cout << "Pila vacia" << endl;
        return -1;
    }
    return pila[tope];
}

bool Pila::vacia() {
    return tope == -1;
}

bool Pila::llena() {
    return tope == capacidad - 1;
}