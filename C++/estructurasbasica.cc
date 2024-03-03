//Estructuras basicas en c++ struct

#include <iostream>
using namespace std;

struct Punto {
    int x;
    int y;
};

int main() {
    Punto p;
    p.x = 3;
    p.y = 4;
    cout << "x = " << p.x << ", y = " << p.y << endl;
    return 0;
}

