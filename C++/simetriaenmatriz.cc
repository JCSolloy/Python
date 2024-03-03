//Determinar si una matriz es simetrica

#include <iostream>
using namespace std;

int main() {
    int matriz[3][3] = {{1, 2, 3}, {2, 4, 5}, {3, 5, 6}};
    bool simetrica = true;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (matriz[i][j] != matriz[j][i]) {
                simetrica = false;
                break;
            }
        }
    }

    if (simetrica) {
        cout << "La matriz es simetrica" << endl;
    } else {
        cout << "La matriz no es simetrica" << endl;
    }

    return 0;
}
