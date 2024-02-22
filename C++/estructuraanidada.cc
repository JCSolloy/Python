// Estructura anidada

#include <iostream>
using namespace std;

struct Punto {
    int x;
    int y;
};

struct Rectangulo {
    Punto esquina1;
    Punto esquina2;
};

int main() {
    Rectangulo r;
  r.esquina1.x = 3;
  r.esquina1.y = 4;
  r.esquina2.x = 5;
  r.esquina2.y = 6;
  cout << "esquina1.x = " << r.esquina1.x << ", esquina1.y = " << r.esquina1.y << endl;
  cout << "esquina2.x = " << r.esquina2.x << ", esquina2.y = " << r.esquina2.y << endl;
  return 0;
}
