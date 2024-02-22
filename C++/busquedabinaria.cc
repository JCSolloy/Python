//busqueda binaria

#include <iostream>
using namespace std;

int main() {
  int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
  int n = 9;
  int x = 5;
  int i = 0;
  int j = n - 1;
  int m;
  while (i <= j) {
    m = (i + j) / 2;
    if (a[m] == x) {
      break;
    } else if (a[m] < x) {
      i = m + 1;
    } else {
      j = m - 1;
    }
  }
  if (i <= j) {
    cout << "Se encontro el valor " << x << " en la posicion " << m << endl;
  } else {
    cout << "No se encontro el valor " << x << endl;
  }
  return 0;
}

