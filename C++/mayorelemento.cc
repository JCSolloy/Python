//elemento mayor en un array

#include <iostream>
using namespace std;

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int mayor = arr[0];

    for (int i = 1; i < 5; i++) {
        if (arr[i] > mayor) {
            mayor = arr[i];
        }
    }
    cout << "El mayor elemento es: " << mayor << endl;

    return 0;
}