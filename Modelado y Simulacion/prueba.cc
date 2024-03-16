#include "g4.cc"
#include <vector>

int main() {
  int lambda = 1;
  long X0=33;
  vector <double> exponencial1;
  //generate_random_numbers(X0);

  exponencial1 = exponencialg4(lambda,X0);
  // // print exponential distribution
  cout << "Distribución exponencial: " << endl;
  for (int i = 0; i < exponencial1.size(); i++) {
     cout << exponencial1[i] << endl;
  }

  return 0;
}

