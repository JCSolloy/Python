#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
// Funcion distribucion exponencial
vector<double> exponencialg4(int lambda, long X0) {
  vector<double> exponential_distribution;
  vector<double> random_numbers;
  long n, a, c, m;
  n=10000;
  a=1664525;
  c=0;
  m=2147483647;
  vector<double> numeros;
  // Generación de números aleatorios
  for (int i = 0; i < n; i++) {
    X0 = (a * X0 + c) % m;
    random_numbers.push_back((double)X0 / (double)m);
  }
  numeros = random_numbers;
  for (int i = 0; i < n; i++) {
    exponential_distribution.push_back(-log(1 - numeros[i]) / lambda);
  }
  return exponential_distribution;
}
