// Estructuras en c++ struct
// Path: C%2B%2B/estructuras.cc

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
