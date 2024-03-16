#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<double> generate_random_numbers(long X0) {
  long n, a, c, m;
  n=10000;
  a=1664525;
  c=0;
  m=2147483647;
  // Generación de números aleatorios
  vector<double> random_numbers;
  for (int i = 0; i < n; i++) {
    X0 = (a * X0 + c) % m;
    random_numbers.push_back((double)X0 / (double)m);
  }
  // media y varianza de los números aleatorios
  double media = 0;
  double varianza = 0;
  for (int i = 0; i < n; i++) {
    media += random_numbers[i];
  }
  media /= n;
  for (int i = 0; i < n; i++) {
    varianza += (random_numbers[i] - media) * (random_numbers[i] - media);
  }
  varianza /= n;
  // cout << "Media: " << media << endl;
  // cout << "Varianza: " << varianza << endl;

  // cout << "Números aleatorios generados: " << endl;
  // for (int i = 0; i < n; i++) {
  //   cout << random_numbers[i] << endl;
  // }
  return random_numbers;
}

// Funcion distribucion exponencial
vector<double> exponencial(int lambda, long X0) {
  vector<double> numeros;
  vector<double> exponential_distribution;
  long n;
  numeros = generate_random_numbers(X0);
  n = numeros.size();
  for (int i = 0; i < n; i++) {
    exponential_distribution.push_back(-log(1 - numeros[i]) / lambda);
  }
  // media y varianza de la distribución exponencial
  double media = 0;
  double varianza = 0;
  for (int i = 0; i < n; i++) {
    media += exponential_distribution[i];
  }
  media /= n;
  for (int i = 0; i < n; i++) {
    varianza += (exponential_distribution[i] - media) * (exponential_distribution[i] - media);
  }
  varianza /= n;
  cout << "Media: " << media << endl;
  cout << "Varianza: " << varianza << endl;
  //print exponential distribution
  // cout << "Distribución exponencial: " << endl;
  // for (int i = 0; i < exponential_distribution.size(); i++) {
  //   cout << exponential_distribution[i] << endl;
  // }
  return exponential_distribution;
}

int main() {
  int lambda = 1;
  long X0=123456789;
  vector <double> exponencial1;
  //generate_random_numbers(X0);

  exponencial1 = exponencial(lambda,X0);
  // // print exponential distribution
  cout << "Distribución exponencial: " << endl;
  for (int i = 0; i < exponencial1.size(); i++) {
     cout << exponencial1[i] << endl;
  }

  return 0;
}