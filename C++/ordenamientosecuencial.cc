//  busqueda secuencial
#include <iostream>
using namespace std;

int main() {
  int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
  int n = 9;
  int x = 5;
  int i = 0;
  while (i < n && a[i] != x) {
    i++;
  }
  if (i == n) {
    cout << "No se encontro el valor " << x << endl;
  } else {
    cout << "Se encontro el valor " << x << " en la posicion " << i << endl;
  }
  return 0;
}
